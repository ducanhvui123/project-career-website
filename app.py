from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Hunt the Mischievous Slimes',
        'location': 'The Murky Marshlands',
        'salary': '10 Gold Pieces'
    },
    {
        'id': 2,
        'title': 'Medicinal Herb Gathering ',
        'location': 'The Enchanted Forest',
        'salary': ' 50 Silver Shillings'
    },
    {
        'id': 3,
        'title': 'Dragon Slaying',
        'location': 'The Volcanic Peaks',
        'salary': '1,000 Gold Pieces'
    },
    {
        'id': 4,
        'title': 'Wagon Escort ',
        'location': 'The Bandit-Infested Pass',
        'salary': '100 Gold Pieces'
    },
]

@app.route("/")
def index():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/quest")
def list_quest():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

@app.route("/login")
def login():
    return render_template("login.html")