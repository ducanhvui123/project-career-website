from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from dotenv import load_dotenv
import os


# secure your db_connection_information
load_dotenv()
db_connection_string = os.getenv("DATABASE_URL")
app = Flask(__name__)


@app.route("/")
def index():
    # call the function to load the information from database
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

@app.route("/api/quest")
def list_quest():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
