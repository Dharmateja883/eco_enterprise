import mysql.connector
from db_config import get_db_connection

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES LIKE 'issues'")
    result = cursor.fetchone()
    if result:
        print("Table 'issues' exists.")
    else:
        print("Table 'issues' does not exist. Creating it...")
        cursor.execute("""
            CREATE TABLE issues (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                location VARCHAR(255),
                issue_type VARCHAR(255),
                description TEXT
            )
        """)
        conn.commit()
        print("Table 'issues' created.")
    conn.close()
except mysql.connector.Error as err:
    if err.errno == 1049: # Unknown database
        print("Database 'eco_db' does not exist. Creating it...")
        # Connect without DB to create it
        temp_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Teja@nov22"
        )
        temp_cursor = temp_conn.cursor()
        temp_cursor.execute("CREATE DATABASE eco_db")
        temp_conn.close()
        print("Database 'eco_db' created. Please run this script again.")
    else:
        print(f"Error: {err}")
