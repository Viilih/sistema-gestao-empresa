from database.database import get_db_connection
import sqlite3

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def validate(username, password):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = cursor.fetchone()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            conn.close()
        return user is not None


    def create(username, password):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            conn.close()
        return True
