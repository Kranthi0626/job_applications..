from flask import Flask, render_template
import sqlite3

job = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect("job_tracker.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS JobApplications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            job_title TEXT NOT NULL,
            starting_date TEXT NOT NULL,
            ending_date TEXT NOT NULL,
            job_description TEXT NOT NULL,
            job_link TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@job.route('/')
def index():
    conn = sqlite3.connect("job_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, company_name, job_title, starting_date, ending_date, job_description, job_link FROM JobApplications")
    jobs = cursor.fetchall()
    conn.close()
    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    job.run(debug=True)
