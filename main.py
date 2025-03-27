from app import app

# Required for Vercel serverless functions
application = app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
