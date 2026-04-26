from db_config import get_db_connection

def add_issue(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO issues (name, location, issue_type, description) VALUES (%s,%s,%s,%s)",
        data
    )

    conn.commit()
    conn.close()


def get_issues():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM issues")
    data = cursor.fetchall()

    conn.close()
    return data