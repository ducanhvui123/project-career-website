from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
app = Flask(__name__)


@app.route("/")
def index():
    # call the function to load the information from database
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

@app.route("/api/quest")
def list_quest():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)