from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://tqpgtb7b7w1xkpc5r4u8:pscale_pw_hrFSoS3FxSpzXki4X5BV6lJHf05KIs0mZae1pQC2oUs@gcp.connect.psdb.cloud/hearthstonetavern?charset=utf8mb4"
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
