from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# secure your db_connection_information
load_dotenv()
db_connection_string = os.getenv("DATABASE_URL")

# engine connect
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_jobs_from_db():
    # connect database:
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        rows = result.fetchall()  # Use fetchall() to retrieve all rows
        # create a job dictionary
        jobs = []

        for row in rows:
            # Create a dictionary for each row by combining column names and values
            job = dict(zip(row.keys(), row))
            jobs.append(job)
        return jobs
