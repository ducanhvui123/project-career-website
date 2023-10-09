# ***THE HEARTHSTONE TAVERN***
#### Video Demo:  <URL HERE>
#### Description:

## CS50
>This was my final project for conclude the CS50 Introduction to Computer Sciense course.

>Language and framework that I use in my project: python, flask,sqlalchemy, html, css, javascript, dotenv, gunicorn, pymysql.


## Explaining the project and the database

My final project is a website that provide some job opportunity for worker. But instead of doing a normal job hunting website, I used my imagination to create a Medieval Tavern instead which provide lots of quest and mission for Adventurer to choose which one will fit their abilities and from that for the ultra goal is: Making money. And the website does provide a quest accept for people who have problem or quest that need our adventurer help too.

### SQLalchemy and mySQL:
I need 2 tables for my database:
1. Jobs table, Where I put id, title, location, salary, currency, responsibilities, requirements. id is primary key
2. Applications table, where I put job_id, full_name, email, profession, abilities, experience. job_id is primary key

So basically all information about the quest and updated quest input by user will be stored in jobs table and all the applications from adventurer that input by user will be stored in applications table.
i use sqlalchemy to connect database and mySQL to application to manage her.

### Code Explaining
#### Templates folder:
Contain html with jinja syntax to show the website to the world. I have learned a lot from this. Like this block of code in questpage.html
`
<h4>Requirements</h4>
        <ul>
            {% for line in job['requirements'].split(".") %}
            <li>{{ line }}</li>
            {% endfor %}
        </ul>
        <h4>Responsibilities</h4>
        <ul>
            {% for line in job['responsibilities'].split(".") %}
            <li>{{ line }}</li>
            {% endfor %}
        </ul>
        <h4>Salary</h4>
        <p>{{ job['salary'] }} {{ job['currency'] }}</p>
        {% include 'application_form.html' %}
    </div>
    {% include 'footer.html' %}
`
#### It actually take the data from app.py into a job dictionary and for every line in the dictionary let split them out whenever u meet the "." to make a new line for the tag.

`
            <div>
                <a href="quest/request" type="button" class="btn btn-danger">You have quest that need our Adventurer to handle? Click here</a>
            </div>
`
and this button for re-direct to a quest submit for people who have quest and mission for the tavern to handle
`
 ####here is what inside app.py code to handle the data which is prompt by user
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
`
#### and the loaded function inside database
`
def add_new_quest_to_db(data):
    with engine.connect() as conn:
        query = text("INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements) VALUES (:title, :location, :salary, :currency, :responsibilities, :requirements)")

        conn.execute(query,
                     title = data["title"],
                     location = data["location"],
                     salary = data["salary"],
                     currency = data["currency"],
                     responsibilities = data["responsibilities"],
                     requirements = data["requirements"])
`
#### this code snippet is for putting all of the information from the database, stored in a dictionary call job
`
<div class="border-bottom row" style="margin-bottom: 16px; padding-bottom: 8px;">
   <div class="col-9">
        <h4 class="job-title">{{ job['title'] }}</h4>
        <div class="job-location">
            <b>Location: </b>{{ job['location'] }}
        </div>
        <div class="job-location">
            <b>Salary:</b> {{ job['salary'] }} {{ job['currency'] }}
        </div>
    </div>
    <div class="col-3">
        <a href="/quest/{{job['id']}}" id="embark" type="button" class="btn btn-success">Embark</a>
    </div>
</div>
`
 ####this code snippet from quest_submitted.html work exactly the same as the one above
`
 <div id="container">
        <img style="margin-bottom: 30px;" id="banner" src="/static/banner2.jpeg" alt="tavern-banner">
        <h1>Hearthstone Tavern</h1>

        <p style="text-align: center;">Your request for the quest of <b>{{ data['title']}}</b> at Hearthstone Tavern has been submitted, We will get back to you soon</p>
        <b class="mb-0">Quest title</b>
        <div class="mb-2">{{data['title']}}</div>

        <b>Quest location</b>
        <div class="mb-2">{{ data['location'] }}</div>

        <b>Quest payout</b>
        <div class="mb-2">{{ data['salary'] }}</div>

        <b>Quest payout currency</b>
        <div class="mb-2">{{ data['currency'] }}</div>

        <b>Quest responsibilities</b>
        <div class="mb-2">{{ data['responsibilities'] }}</div>

        <b>Quest requirements</b>
        <div class="mb-2">{{ data['requirements'] }}</div>
    </div>
`
#### and here is the app.py code for it
`@app.route("/quest/<id>/apply", methods=["POST"])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    # store in db
    add_application_to_db(id, data)
    # display data and acknowledgement
    return render_template("application_submitted.html", application = data, job = job)`
### for future upgrade
I'm trying to improve my website more by trying to deploy it into a web service, and also trying to make a log in log out session and do more CSS and styling to the web page so it can look more nice and clean.

also trying to make a register to become a hero too so that you can become a adventure and trying to make a admin page as well to control the website directly.

That is all for future plan

#### This is really a small milestone in my way to become a developer and I have learned a lot from this project. Thank you cs50 for handling me this opportunity

### Acknownledgement and thank you
#### About CS50

CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.
This was CS50