from flask import Flask, render_template, jsonify
import os
import sys

# Aggiungi la directory principale al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Crea l'app Flask
app = Flask(__name__, 
           static_folder='../static',
           template_folder='../templates')

app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

@app.route('/', methods=['GET'])
def home():
    """Render the main bibliography generator page"""
    return render_template('index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint for Vercel"""
    return jsonify({"status": "ok"})