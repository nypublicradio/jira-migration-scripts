import sys
import psycopg2
from flask import Flask

app = Flask(__name__)



@app.route('/')
def home():
    return 'the jira archive'

@app.route('/issue/<issue_key>')
def issue(issue_key):
    try:
        conn = psycopg2.connect(host="jiradatabase", database="jira",
                                user="docker", password="docker")
    except Exception as e:
        sys.exit(e)

    if conn is not None:
        print('Connection established to PostgreSQL.')

        cur = conn.cursor()

        cur.execute(f"SELECT * FROM jira where issue_key0='{issue_key}';")

        get_all_data = cur.fetchall()

        conn.close()
    else:
        print('Connection not established to PostgreSQL.')

    return str(get_all_data)

