from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

DB = "database.db"

# -------------------
# DB SETUP
# -------------------
def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            category TEXT,
            description TEXT,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -------------------
# HOME PAGE (LIST)
# -------------------
@app.route("/")
def index():
    search = request.args.get("search")

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    if search:
        like = f"%{search}%"
        cur.execute("""
            SELECT * FROM complaints
            WHERE name LIKE ? OR email LIKE ? OR phone LIKE ? OR category LIKE ? OR description LIKE ?
            ORDER BY id DESC
        """, (like, like, like, like, like))
    else:
        cur.execute("SELECT * FROM complaints ORDER BY id DESC")

    data = cur.fetchall()
    conn.close()

    return render_template("index.html", complaints=data, search=search)


# -------------------
# ADD COMPLAINT
# -------------------
@app.route("/add", methods=["GET", "POST"])
def add_complaint():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        category = request.form["category"]
        description = request.form["description"]

        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO complaints (name, email, phone, category, description, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, email, phone, category, description, datetime.now().isoformat()))
        
        conn.commit()
        conn.close()

        flash("Complaint added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_complaint.html")


# -------------------
# EDIT COMPLAINT
# -------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_complaint(id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaints WHERE id=?", (id,))
    data = cur.fetchone()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        category = request.form["category"]
        description = request.form["description"]

        cur.execute("""
            UPDATE complaints
            SET name=?, email=?, phone=?, category=?, description=?
            WHERE id=?
        """, (name, email, phone, category, description, id))

        conn.commit()
        conn.close()

        flash("Complaint updated!", "info")
        return redirect(url_for("index"))

    conn.close()
    return render_template("edit_complaint.html", complaint=data)


# -------------------
# DELETE COMPLAINT
# -------------------
@app.route("/delete/<int:id>")
def delete_complaint(id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM complaints WHERE id=?", (id,))
    conn.commit()
    conn.close()

    flash("Complaint deleted!", "danger")
    return redirect(url_for("index"))


# -------------------
# VIEW COMPLAINT
# -------------------
@app.route("/view/<int:id>")
def view_complaint(id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaints WHERE id=?", (id,))
    data = cur.fetchone()
    conn.close()
    return render_template("view_complaint.html", complaint=data)


if __name__ == "__main__":
    app.run(debug=True)
