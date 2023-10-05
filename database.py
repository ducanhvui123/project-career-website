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

# def load_jobs_from_db():
#     # connect database:
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from jobs"))
#         # create a job dictionary
#         jobs = []

#         for row in result:
#             # Create a dictionary for each row by combining column names and values
#             jobs.append(dict(row))
#         return jobs
    
def load_jobs_from_db():
    # Connect to the database
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        
        # Create a list of dictionaries
        jobs = [dict(row) for row in result]
        
    return jobs