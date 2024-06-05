import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controller.employee_controller import EmployeeController
from controller.team_controller import TeamController

class EmployeeView:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x720')
        self.root.title("Manage Employees")
        self.root.configure(bg="#333333")
        self.controller = EmployeeController(self)
        self.controller_teams = TeamController(self)
    
        self.create_table()
        self.create_buttons()

    def create_table(self):
        employees = self.controller.get_all_employees()
        self.table = ttk.Treeview(self.root, columns=('id', 'name', 'age', 'position','team_id'), show='headings')
        self.table.heading('id', text='ID',anchor='center')
        self.table.heading('name', text='Nome')
        self.table.heading('age', text='Idade')
        self.table.heading('position', text='Função')
        self.table.heading('team_id', text='Id Time')

        self.table.column('id',anchor=tk.CENTER)
        self.table.column('name',anchor=tk.CENTER)
        self.table.column('age',anchor=tk.CENTER)
        self.table.column('position',anchor=tk.CENTER)
        self.table.column('team_id',anchor=tk.CENTER)

        for employee in employees:
            data = employee[:5]
            self.table.insert(parent='', index=0, values=data)

        self.table.pack(pady=20)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.configure(bg="#333333")
        button_frame.pack()

        self.add_employee_button = tk.Button(button_frame, text="Adicionar funcionário", bg="#FF3399", fg="#ffffff", command=self.open_add_employee_window)
        self.add_employee_button.pack(side=tk.LEFT, padx=10)

        self.delete_employee_button = tk.Button(button_frame, text="Deletar funcionário", bg="#FF3399", fg="#ffffff", command=self.delete_employee)
        self.delete_employee_button.pack(side=tk.LEFT, padx=10)

        self.update_employee_button = tk.Button(button_frame, text="Atualizar funcionário", bg="#FF3399", fg="#ffffff", command=self.update_employee)
        self.update_employee_button.pack(side=tk.LEFT, padx=10)

        close_button = tk.Button(button_frame, text="Fechar", command=self.root.destroy, bg="#FF3399", fg="#ffffff")
        close_button.pack(side=tk.LEFT, padx=10)


    def open_add_employee_window(self):
        
        add_employee_window = tk.Toplevel(self.root, bg="#333333")
        add_employee_window.geometry('400x400')
        add_employee_window.title("Adicionar funcionário")


        main_frame = tk.Frame(add_employee_window, bg="#333333", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(main_frame, text="Nome:", bg="#333333",fg='#ffffff').grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(main_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        tk.Label(main_frame, text="Idade:",bg="#333333",fg='#ffffff').grid(row=1, column=0, sticky=tk.W)
        self.age_entry = tk.Entry(main_frame)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        tk.Label(main_frame, text="Função:",bg="#333333",fg='#ffffff').grid(row=2, column=0, sticky=tk.W)
        self.position_entry = tk.Entry(main_frame)
        self.position_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        tk.Label(main_frame, text="Id do Time:",bg="#333333",fg='#ffffff').grid(row=3, column=0, sticky=tk.W)
        self.team_entry = tk.Entry(main_frame)
        self.team_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        add_button = tk.Button(main_frame, text="Adicionar", command=self.add_employee,width=30,bg="#FF3399", fg="#ffffff")
        add_button.grid(row=4, column=0, columnspan=2, pady=10)
        close_button = tk.Button(main_frame, text="Fechar", command=add_employee_window.destroy, width=30, bg="#FF3399", fg="#ffffff")
        close_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_employee(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        position = self.position_entry.get()
        team_id = self.team_entry.get()
        team_Ids_controller = self.controller_teams.get_all_teams()
        team_ids = [team[0] for team in team_Ids_controller]
        if not (name and age and position and team_id):
            tk.messagebox.showerror("Error", "Preencha todos os campos corretamente")
            return
        if not age.isdigit() or int(age) <= 0:
            tk.messagebox.showerror("Error", "Idade inválida, insira uma idade válida")
            return 
        if int(team_id) not in team_ids:
             tk.messagebox.showerror("Error", "Um time com esse Id ainda nao foi encontrado")
             return
           
        self.controller.add_employee(name, age, position, team_id)
        self.refresh_employee_list()
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)
        self.team_entry.delete(0, tk.END)

    def delete_employee(self):
        selected_item = self.table.selection()
        if selected_item:
            employee_id = self.table.item(selected_item)['values'][0]
            self.controller.delete_employee(employee_id)
            self.refresh_employee_list()
        else:
            tk.messagebox.showerror("Error", "Você precisa selecionar um funcionário para ser removido, basta clicar em algum elemento na tabela")

    def refresh_employee_list(self):
        for child in self.table.get_children():
            self.table.delete(child)

        employees = self.controller.get_all_employees()
        for employee in employees:
            self.table.insert("", tk.END, values=employee)
    def update_employee(self):
        selected_item = self.table.selection()
        if selected_item:
            employee_id = self.table.item(selected_item)['values'][0]
            employee_data = self.controller.get_employee_by_id(employee_id)
            if employee_data:
                self.open_update_employee_window(employee_data)
            else:
                messagebox.showerror("Error", f"Funcionário com id {employee_id} não foi encontrado.")
        else:
            messagebox.showerror("Error", "Você precisa selecionar um funcionário para editar, para isso, selecione algum elemento da tabela.")

        
    def open_update_employee_window(self, employee_data):
        update_employee_window = tk.Toplevel(self.root,bg="#333333")
        update_employee_window.geometry('400x400')
        update_employee_window.title("Atualiizar funcionário")


        main_frame = tk.Frame(update_employee_window, padx=20, pady=20,bg="#333333")
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        tk.Label(main_frame, text="Nome:",bg="#333333",fg='#ffffff').grid(row=0, column=0, sticky=tk.W)
        self.update_name_entry = tk.Entry(main_frame)
        self.update_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self.update_name_entry.insert(0, employee_data[1])

        tk.Label(main_frame, text="Idade:",bg="#333333",fg='#ffffff').grid(row=1, column=0, sticky=tk.W)
        self.update_age_entry = tk.Entry(main_frame)
        self.update_age_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        self.update_age_entry.insert(0, employee_data[2])

        tk.Label(main_frame, text="Função:",bg="#333333",fg='#ffffff').grid(row=2, column=0, sticky=tk.W)
        self.update_position_entry = tk.Entry(main_frame)
        self.update_position_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self.update_position_entry.insert(0, employee_data[3])

        tk.Label(main_frame, text="Id do Time:",bg="#333333",fg='#ffffff').grid(row=3, column=0, sticky=tk.W)
        self.update_team_id_entry = tk.Entry(main_frame)
        self.update_team_id_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        self.update_team_id_entry.insert(0, employee_data[4])

        update_button = tk.Button(main_frame, text="Atualizar", command=lambda: self.update_employee_data(employee_data[0], update_employee_window),width=30,bg="#FF3399", fg="#ffffff")
        update_button.grid(row=4, column=0, columnspan=2, pady=10)
        close_button = tk.Button(main_frame, text="Fechar", command=update_employee_window.destroy, width=30, bg="#FF3399", fg="#ffffff")
        close_button.grid(row=5, column=0, columnspan=2, pady=10)

    def update_employee_data(self, employee_id, update_employee_window):
        name = self.update_name_entry.get()
        age = self.update_age_entry.get()
        position = self.update_position_entry.get()
        team_id = self.update_team_id_entry.get()
        team_Ids_controller = self.controller_teams.get_all_teams()
        team_ids = [team[0] for team in team_Ids_controller]

        if not (name and age and position and team_id):
            messagebox.showerror("Error", "Preencha todos os campos corretamente")
            return

        if not age.isdigit() or int(age) <= 0:
            messagebox.showerror("Error", "Idade inválida, insira uma idade válida")
            return

        if int(team_id) not in team_ids:
            messagebox.showerror("Error", "Um time com esse ID ainda não foi encontrado")
            return

        self.controller.update_employee(employee_id, name, age, position, team_id)
        self.refresh_employee_list()
        update_employee_window.destroy()

