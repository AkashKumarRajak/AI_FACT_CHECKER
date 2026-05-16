import sqlite3


# ==================================================
# CONNECT DB
# ==================================================

def connect_db():

    conn = sqlite3.connect(
        "database/database.db",
        check_same_thread=False
    )

    return conn


# ==================================================
# INIT DATABASE
# ==================================================

def init_db():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        claim TEXT,

        result TEXT,

        confidence REAL,

        category TEXT,

        risk TEXT,

        source_trust REAL

    )

    """)

    conn.commit()

    conn.close()


# ==================================================
# SAVE RESULT
# ==================================================

def save_result(
    claim,
    result,
    confidence,
    category,
    risk,
    source_trust
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO history (

        claim,
        result,
        confidence,
        category,
        risk,
        source_trust

    )

    VALUES (?, ?, ?, ?, ?, ?)

    """, (

        claim,
        result,
        confidence,
        category,
        risk,
        source_trust

    ))

    conn.commit()

    conn.close()


# ==================================================
# GET HISTORY
# ==================================================

def get_history():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM history

    ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==================================================
# DELETE HISTORY
# ==================================================

def delete_history(record_id):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM history WHERE id = ?",

        (record_id,)

    )

    conn.commit()

    conn.close()