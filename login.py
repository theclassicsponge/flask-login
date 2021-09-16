from flask import Flask, render_template, request, session, redirect, url_for, g
import psycopg2
import psycopg2.extras
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret-key'

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = ""

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route("/")
def login():
    return render_template("index.html")


@app.route("/forgot")
def forgot():
    return render_template("forgot.html")


@app.route("/create", methods=['GET', 'POST'])
def create():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # check if "username", "password", "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'password' in request.form and 'email' in request.form:
        # create variables for easy access
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        _hashed_password = generate_password_hash(password)

        print(fullname)
        print(_hashed_password)
        print(username)
        print(email)
    return render_template("create.html")


@app.route("/main")
def details():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
    main()
