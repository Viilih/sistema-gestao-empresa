import tkinter as tk
from view.employee_view import EmployeeView
from view.team_view import TeamView
from tkinter import ttk

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x400')
        self.root.configure(bg="#333333")
        self.root.title("Sistema de Gestão da Empresa")
    
        self.button_frame = tk.Frame(root, bg="#333333")
        self.button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.rowconfigure(0, weight=1)
        self.button_frame.rowconfigure(1, weight=1)

        self.employee_button = tk.Button(self.button_frame, text="Gerenciar Funcionários", command=self.open_employee_view, width=20, bg="#FF3399", fg="#ffffff")
        self.team_button = tk.Button(self.button_frame, text="Gerenciar Equipes", command=self.open_team_view, width=20, bg="#FF3399", fg="#ffffff")
        self.close_button = tk.Button(self.button_frame, text="Fechar", command=self.root.destroy, width=20, bg="#FF3399", fg="#ffffff")

        self.employee_button.grid(row=0, column=0, pady=10)
        self.team_button.grid(row=1, column=0, pady=10)
        self.close_button.grid(row=2, column=0, pady=10)

        self.employee_window = None

    def open_employee_view(self):
        if self.employee_window is None or not tk.Toplevel.winfo_exists(self.employee_window):
            self.employee_window = tk.Toplevel(self.root)
            EmployeeView(self.employee_window)
        else:
            self.employee_window.lift()

    def open_team_view(self):
        team_root = tk.Toplevel(self.root)
        TeamView(team_root)
