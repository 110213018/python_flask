from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector


HWApp = Flask(__name__) # Create a Flask application instance
CORS(HWApp) # Enable CORS for all routes

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flask"
)

cursor = db.cursor() # Create a cursor object to interact with the database

# =========================
# 接收 JSON 並寫入 MySQL
# =========================
@HWApp.route("/")
def hello_world():
    return "Hello, World!"

@HWApp.route("/users", methods=["POST"])
def create_user():
    # 1️. 接收前端 JSON
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "name 與 email 不可為空"}), 400

    # 2️. SQL INSERT
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)

    cursor.execute(sql, values)
    db.commit()

    # 3. 回傳結果
    return jsonify({
        "message": "User created successfully",
        "name": name,
        "email": email
    }), 201

if __name__ == "__main__":      # Check if the script is being run directly
    HWApp.run(host="127.0.0.1", port=5000, debug=True)  # Run the Flask application on localhost at port 5000 with debug mode enabled    
