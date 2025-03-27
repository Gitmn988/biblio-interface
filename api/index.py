from flask import Flask, request, Response
import os
import sys

# Add the root directory to the path so we can import from app.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app as flask_app

def handler(request):
    """Handle a request to the Flask app."""
    # Prepare environ from vercel request
    environ = {
        'REQUEST_METHOD': request.get('method', ''),
        'SCRIPT_NAME': '',
        'PATH_INFO': request.get('path', ''),
        'QUERY_STRING': request.get('query', ''),
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.input': None,
        'wsgi.errors': sys.stderr,
        'wsgi.version': (1, 0),
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
        'wsgi.url_scheme': 'https',
        'SERVER_NAME': request.get('headers', {}).get('host', ''),
        'HTTP_HOST': request.get('headers', {}).get('host', ''),
    }
    
    # Add request headers
    for key, value in request.get('headers', {}).items():
        key = key.upper().replace('-', '_')
        if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            key = 'HTTP_' + key
        environ[key] = value
    
    # Capture the response
    response_headers = []
    response_body = []
    
    def start_response(status, headers):
        response_headers.append(status)
        response_headers.extend(headers)
    
    # Call the Flask application
    result = flask_app.wsgi_app(environ, start_response)
    
    # Convert the result to bytes if it's not already
    for data in result:
        if isinstance(data, str):
            response_body.append(data.encode('utf-8'))
        else:
            response_body.append(data)
    
    # Extract status code
    status_parts = response_headers[0].split(' ')
    status_code = int(status_parts[0])
    
    # Extract headers
    headers = {}
    for header, value in response_headers[1:]:
        headers[header] = value
    
    # Combine response body parts
    body = b''.join(response_body)
    if isinstance(body, bytes):
        body = body.decode('utf-8', errors='ignore')
    
    # Return the response
    return {
        'statusCode': status_code,
        'headers': headers,
        'body': body
    }