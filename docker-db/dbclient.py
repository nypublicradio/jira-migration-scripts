import psycopg2

try:
    conn = psycopg2.connect(host="localhost", database="jira",
                            user="docker", password="docker")
except Exception as e:
    print(e)
    exit(0)


if conn is not None:
    print('Connection established to PostgreSQL.')

    cur = conn.cursor()

    # cur.execute('SELECT * FROM jira LIMIT 3;')
    issue_key = 'DEVO-123'
    cur.execute(f"SELECT * FROM jira where issue_key0='{issue_key}';")

    get_all_data = cur.fetchall()

    print(get_all_data)

    conn.close()
else:
    print('Connection not established to PostgreSQL.')

