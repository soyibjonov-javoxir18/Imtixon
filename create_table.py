
from connection import connect_db

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS harajatlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            summa REAL NOT NULL,
            sana TEXT NOT NULL,
            kategoriya TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
