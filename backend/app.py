from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Import and register routes
from routes.task_routes import task_routes
app.register_blueprint(task_routes)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "To-Do List API is Running!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
