from model.employee import Employee
from tkinter import messagebox

class EmployeeController:
    def __init__(self, view):
        self.view = view

    def add_employee(self, name, age, position, team_id):
        try:
             Employee.add(name, age, position, team_id)
             messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso.")

          
        except Exception as e:
             messagebox.showinfo("Erro", "Erro ao adicionar funcionário")
             print(f'Erro ao adicionar funcionario: {e}')
        else:
            self.view.refresh_employee_list()

    def update_employee(self, emp_id, name, age, position, team_id):
        try:
            Employee.update(emp_id, name, age, position, team_id)
            messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso.")
        except Exception as e:
            messagebox.showinfo("Erro", "Erro ao atualizar funcionário")
            print(f'Erro ao atualizar funcionario: {e}')
        else:
            self.view.refresh_employee_list()

    def delete_employee(self, emp_id):
        try:
            Employee.delete(emp_id)
            messagebox.showinfo("Sucesso", "Funcionário excluid com sucesso.")
        except Exception as e:
            messagebox.showinfo("Erro", "Erro ao excluir funcionário")
            print(f"Erro ao deletar funcionário: {e}")
        else:
            self.view.refresh_employee_list()

    def get_all_employees(self):
        try:
            return Employee.get_all()
        except Exception as e:
            print(f"Erro ao obter todos os funcionários: {e}")
            return None
    
    def get_employee_by_id(self, id):
        try:
            return Employee.get_employee_by_id(id)
        except Exception as e:
            print(f"Erro ao obter funcionário pelo ID: {e}")
            return None
