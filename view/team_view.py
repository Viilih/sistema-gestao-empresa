import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controller.team_controller import TeamController

class TeamView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciar Equipes")
        self.root.geometry('1280x720')
        self.root.configure(bg="#333333")
        self.controller = TeamController(self)

        self.create_table()
        self.create_buttons()

    def create_table(self):
        teams = self.controller.get_all_teams()
        self.table = ttk.Treeview(self.root, columns=('id', 'name'), show='headings')
        self.table.heading('id', text='ID')
        self.table.heading('name', text='Nome')

        self.table.column('id',anchor=tk.CENTER)
        self.table.column('name',anchor=tk.CENTER)

        for team in teams:
            data = team[:2]
            self.table.insert('', tk.END, values=data)

        self.table.pack(pady=20)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.configure(bg="#333333")
        button_frame.pack()

        self.add_team_button = tk.Button(button_frame, text="Adicionar Equipe", bg="#FF3399", fg="#ffffff", command=self.open_add_team_window)
        self.add_team_button.pack(side=tk.LEFT, padx=10)

        self.delete_team_button = tk.Button(button_frame, text="Excluir Equipe", bg="#FF3399", fg="#ffffff", command=self.delete_team)
        self.delete_team_button.pack(side=tk.LEFT, padx=10)

        self.update_team_button = tk.Button(button_frame, text="Atualizar Equipe", bg="#FF3399", fg="#ffffff", command=self.update_team)
        self.update_team_button.pack(side=tk.LEFT, padx=10)

        close_button = tk.Button(button_frame, text="Fechar", command=self.root.destroy, bg="#FF3399", fg="#ffffff")
        close_button.pack(side=tk.LEFT, padx=10)

    def open_add_team_window(self):
       add_team_window = tk.Toplevel(self.root, bg="#333333")
       add_team_window.geometry('400x400')
       add_team_window.title("Adicionar Equipe")

       main_frame = tk.Frame(add_team_window, bg="#333333", padx=20, pady=20)
       main_frame.pack(fill=tk.BOTH, expand=True)
       main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

       tk.Label(main_frame, text="Nome da equipe:", bg="#333333", fg='#ffffff').grid(row=0, column=0, sticky=tk.W)
       self.name_entry = tk.Entry(main_frame)
       self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

       add_button = tk.Button(main_frame, text="Adicionar", command=self.add_team, width=30, bg="#FF3399", fg="#ffffff")
       add_button.grid(row=1, column=0, columnspan=2, pady=10)

       close_button = tk.Button(main_frame, text="Fechar", command=add_team_window.destroy, width=30, bg="#FF3399", fg="#ffffff")
       close_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_team(self):
        name = self.name_entry.get()
        if name:
            self.controller.add_team(name)
            self.refresh_team_list()
            self.name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome da equipe.")

    def delete_team(self):
        selected_item = self.table.selection()
        if selected_item:
            team_id = self.table.item(selected_item)['values'][0]
            self.controller.delete_team(team_id)
            self.refresh_team_list()
        else:
            messagebox.showerror("Erro", "Por favor, selecione uma equipe para excluir.")

    def update_team(self):
        selected_item = self.table.selection()
        if selected_item:
            team_id = self.table.item(selected_item)['values'][0]
            team_data = self.controller.get_team_by_id(team_id)
            if team_data:
                self.open_update_team_window(team_data)
            else:
                messagebox.showerror("Erro", f"Equipe com ID {team_id} não encontrada.")
        else:
            messagebox.showerror("Erro", "Por favor, selecione uma equipe para atualizar.")

    def open_update_team_window(self, team_data):
       update_team_window = tk.Toplevel(self.root, bg="#333333")
       update_team_window.geometry('400x400')
       update_team_window.title("Atualizar Equipe")

       main_frame = tk.Frame(update_team_window, bg="#333333", padx=20, pady=20)
       main_frame.pack(fill=tk.BOTH, expand=True)
       main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

       tk.Label(main_frame, text="Nome da equipe:", bg="#333333", fg='#ffffff').grid(row=0, column=0, sticky=tk.W)
       self.update_name_entry = tk.Entry(main_frame)
       self.update_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
       self.update_name_entry.insert(0, team_data[1])

       update_button = tk.Button(main_frame, text="Atualizar", command=lambda: self.update_team_data(team_data[0], update_team_window), width=30, bg="#FF3399", fg="#ffffff")
       update_button.grid(row=1, column=0, columnspan=2, pady=10)

       close_button = tk.Button(main_frame, text="Fechar", command=update_team_window.destroy, width=30, bg="#FF3399", fg="#ffffff")
       close_button.grid(row=2, column=0, columnspan=2, pady=10)

    def update_team_data(self, team_id, update_team_window):
        name = self.update_name_entry.get()

        if name:
            self.controller.update_team(team_id, name)
            self.refresh_team_list()
            update_team_window.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome da equipe.")

    def refresh_team_list(self):
        for child in self.table.get_children():
            self.table.delete(child)

        teams = self.controller.get_all_teams()
        for team in teams:
            self.table.insert('', tk.END, values=team[:2])

if __name__ == "__main__":
    root = tk.Tk()
    app = TeamView(root)
    root.mainloop()
