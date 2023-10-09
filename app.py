from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, add_new_quest_to_db

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'


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

@app.route("/quest/<id>")
def show_quest(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('questpage.html', job=job)

@app.route("/quest/<id>/apply", methods=["POST"])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    # store in db
    add_application_to_db(id, data)
    # display data and acknowledgement
    return render_template("application_submitted.html", application = data, job = job)

@app.route("/quest/request", methods=['GET', 'POST'])
def quest_request():
    if request.method == 'POST':
        # store form data into a dictionary
        data = request.form
        #store new data into the database
        add_new_quest_to_db(data)
        return render_template("quest_submitted.html", data = data)
    else:
        return render_template("quest_request.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
