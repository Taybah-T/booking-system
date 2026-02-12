from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    db = sqlite3.connect("database.db")
    db.row_factory = sqlite3.Row
    return db


@app.route("/")
def home():
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=="POST":
    
        db = get_db()
        
        fname = request.form["fname"]
        lname=request.form["lname"]
        email = request.form["email"]
        password = request.form["password"]
            
        db.execute(
                    "INSERT INTO users (fname, lname, email, password) VALUES (?, ?, ?, ?)",
                    (fname, lname, email, password))
        
        db.commit()
        
        return render_template("login.html")

    return render_template("signup.html")


    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        
        db = get_db()
        
        email = request.form.get("email")
        password = request.form.get("password")

    
        # learn this bro
        cursor = db.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        
        if user is not None:
             return render_template("home.html")
            
        else:
            return render_template("home.html")
        
    return render_template("login.html")

@app.route("/home", methods=["GET"])
def front_page():
    return render_template("home.html")

@app.route("/about", methods=["GET"])
def about_us():
    return render_template("about.html")

@app.route("/event", methods=["GET"])
def events():
    return render_template("events.html")

@app.route("/logout")
def log_out():
    return redirect(url_for("login"))

@app.route("/booking")
def ur_bookings():
    return render_template("booking.html")


    
if __name__ == "__main__":
    app.run(debug=True)