from database.database import get_db_connection
import sqlite3

class Team:
    
    def add(name):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO teams (name) VALUES (?)", (name,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            conn.close()
        return True

    
    def update(team_id, name):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE teams SET name = ? WHERE id = ?", (name, team_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            conn.close()
        return True

    
    def delete(team_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM teams WHERE id = ?", (team_id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            conn.close()
        return True
    
    def get_all():
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM teams")
            teams = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            conn.close()
        return teams

    
    def get_team_by_id(id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM teams WHERE id = ?", (id,))
            team = cursor.fetchone()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            conn.close()
        return team
