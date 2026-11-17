
from connection import connect_db

def add_harajat(nom, summa, sana, kategoriya):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO harajatlar
        (nom, summa, sana, kategoriya)
        VALUES (?, ?, ?, ?)
    """, (nom, summa, sana, kategoriya))

    conn.commit()
    conn.close()

def get_harajatlar():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM harajatlar")
    data = cursor.fetchall()

    conn.close()
    return data

def jami_harajat():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(summa) FROM harajatlar")
    jami = cursor.fetchone()[0]

    conn.close()
    return jami or 0
