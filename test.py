import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Azure Web App Python</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 if PORT not set
    app.run(host='0.0.0.0', port=port)