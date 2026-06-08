import re
import sqlite3
import bcrypt

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash
)

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/")
def home():
    return """
    <h2>Secure Login System</h2>

    <a href='/register'>Register</a><br><br>

    <a href='/login'>Login</a>
    """


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Password Validation
        if len(password) < 8:
            flash("Password must be at least 8 characters long", "danger")
            return redirect("/register")

        if not re.search(r"[A-Z]", password):
            flash("Password must contain at least one uppercase letter", "danger")
            return redirect("/register")

        if not re.search(r"[a-z]", password):
            flash("Password must contain at least one lowercase letter", "danger")
            return redirect("/register")

        if not re.search(r"[0-9]", password):
            flash("Password must contain at least one number", "danger")
            return redirect("/register")

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        try:

            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users(username, email, password) VALUES (?, ?, ?)",
                (
                    username,
                    email,
                    hashed_password.decode("utf-8")
                )
            )

            conn.commit()
            conn.close()

            flash("Registration Successful!", "success")
            return redirect("/login")

        except sqlite3.IntegrityError:

            flash("Username or Email already exists!", "danger")
            return redirect("/register")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            stored_password = user[3]

            if bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password.encode("utf-8")
            ):

                session["user"] = username

                flash("Login Successful!", "success")
                return redirect("/dashboard")

        flash("Invalid Username or Password", "danger")
        return redirect("/login")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


@app.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully", "success")

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)