import sqlite3

def init_db():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  message TEXT)''')
    conn.commit()
    conn.close()

def insert_feedback(name, message):
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()

def get_feedback():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute("SELECT name, message FROM feedback")
    data = c.fetchall()
    conn.close()
    return data
