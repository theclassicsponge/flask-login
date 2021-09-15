from flask import Flask, render_template, request, session, redirect, url_for, g
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = 'secret-key'

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "london2000"

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
    # check 
    return render_template("create.html")


@app.route("/main")
def details():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
    main()
