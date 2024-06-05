import tkinter as tk
from view.login_view import LoginView
from database.database import create_tables

def main():
    create_tables()

    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
