from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    db = sqlite3.connect("database.db")
    db.row_factory = sqlite3.Row
    return db


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


    
@app.route("/login", methods=["POST"])
def login():
    db = get_db()
    data = request.get_json()
    
    email = data["email"]
    password = data["password"]
    
    # learn this bro
    cursor = db.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    
    if user:
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False})
    
if __name__ == "__main__":
    app.run(debug=True)