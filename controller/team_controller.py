from model.team import Team
from tkinter import messagebox

class TeamController:
    def __init__(self, view):
        self.view = view

    def add_team(self, name):
        if not name:
            messagebox.showerror("Erro", "O nome da equipe não pode estar vazio.")
            return
        
        try:
            success = Team.add(name)
            if success:
                messagebox.showinfo("Sucesso", "Equipe adicionada com sucesso.")
                self.view.refresh_team_list()
            else:
                messagebox.showerror("Erro", "Erro ao adicionar equipe.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao adicionar a equipe: {e}")
            print(f'Erro ao adicionar um time: {e}')

    def update_team(self, team_id, name):
        if not name:
            messagebox.showerror("Erro", "O nome da equipe não pode estar vazio.")
            return
        
        try:
            success = Team.update(team_id, name)
            if success:
                messagebox.showinfo("Sucesso", "Equipe atualizada com sucesso.")
                self.view.refresh_team_list()
            else:
                messagebox.showerror("Erro", "Erro ao atualizar equipe.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao atualizar a equipe: {e}")
            print(f'Erro ao atualizar um time: {e}')

    def delete_team(self, team_id):
        try:
            success = Team.delete(team_id)
            if success:
                messagebox.showinfo("Sucesso", "Equipe deletada com sucesso.")
                self.view.refresh_team_list()
            else:
                messagebox.showerror("Erro", "Erro ao deletar equipe.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao deletar a equipe: {e}")
            print(f'Erro ao excluir um time: {e}')


    def get_all_teams(self):
        try:
            return Team.get_all()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao obter as equipes: {e}")
            return None

    def get_team_by_id(self, id):
        try:
            return Team.get_team_by_id(id)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao obter a equipe: {e}")
            return None
