from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

events = {
    1: {"name": "Python Beginner", "date": "25/10/26"},
    2: {"name": "Python Intermediate", "date": "25/10/26"},
    3: {"name": "Game Development", "date": "25/10/26"}
}


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("login.html")



@app.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Users WHERE Email = ? AND Password = ?""", (email, password))
        user = cur.fetchone()
        conn.close()

        if user:
            return redirect("/events")
        else:
            return "Invalid email or password"
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def create_user_account():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        try:
            cur.execute("""
                INSERT INTO Users (UserName, Email, Password)
                VALUES (?, ?, ?)
                """, (name, email, password))
            conn.commit()
            conn.close()

            return redirect("/login")
        except:
            return "Email already exists"
    return render_template("signup.html")


@app.route("/about")
def about_us():
    return render_template("about.html")

@app.route("/events")
def events_page():
    return render_template("events.html")

@app.route("/logout")
def log_out():
    return redirect("/login")


@app.route("/book-event/<int:event_id>")
def book_event(event_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO bookings (event_name, event_date)
        VALUES (?, ?)
    """, (events[event_id]["name"], events[event_id]["date"]))

    conn.commit()
    conn.close()

    return redirect("/bookings")

@app.route("/bookings")
def bookings_page():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM bookings")
    bookings = cur.fetchall()

    conn.close()

    return render_template("bookings.html", bookings=bookings)

@app.route("/delete-booking/<int:id>")
def delete_booking(id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM bookings WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect("/bookings")

@app.route("/feedback")
def feedback_page():
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)
