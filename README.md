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

### Acknownledgement and thank you
#### About CS50

CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.
This was CS50