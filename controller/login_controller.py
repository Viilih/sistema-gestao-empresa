import datetime
from model.user import User

class LoginController:
    def __init__(self, view):
        self.view = view

    def login(self):
        try:
            username = self.view.username_entry.get()
            password = self.view.password_entry.get()
            if User.validate(username, password):
                self.log_login(username)
                self.view.show_message("Login realizado com sucesso")
                self.view.redirect_main_page()
            else:
                self.view.show_message("Credenciais inválidas")
        except Exception as e:
            self.view.show_message(f"Ocorreu um erro durante o login: {e}")

    def log_login(self, username):
        try:
            with open("logs/user_log.txt", "a") as log_file:
                log_file.write(f"{datetime.datetime.now()} - Usuário {username} fez login\n")
        except IOError as e:
            self.view.show_message(f"Falha ao escrever no log: {e}")
