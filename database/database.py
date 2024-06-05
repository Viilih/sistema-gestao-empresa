import sqlite3

def get_db_connection():
    conn = sqlite3.connect('company_management.db')
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )''')

    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    admin_user = cursor.fetchone()
    
    if admin_user is None:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin123'))

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        position TEXT NOT NULL,
        team_id INTEGER,
        FOREIGN KEY (team_id) REFERENCES teams (id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
