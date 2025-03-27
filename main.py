from app import app

# Required for Vercel serverless functions
# Vercel looks for a variable named 'app'
# The 'application' variable was previously here for WSGI platforms like gunicorn

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
