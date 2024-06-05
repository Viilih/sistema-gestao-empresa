import datetime

from model.user import User

class RegisterController:
    def __init__(self, view):
        self.view = view

    def register(self):
        try:

            username = self.view.username_entry.get()
            password = self.view.password_entry.get()
            if not username or not password:
                self.view.show_message("Por favor, preencha ambos os campos corretamente")
                return
            
            success = User.create(username, password)
            
            if success:
                self.log_register(username)
                self.view.show_message("Cadastro de usuário realizado com sucesso")
            else:
                self.view.show_message("Erro ao cadastrar usuário")
        
        except Exception as e:
            self.view.show_message(f"Ocorreu um erro: {e}")
    def log_register(self, username):
        try:
            with open("logs/user_log.txt", "a") as log_file:
                log_file.write(f"{datetime.datetime.now()} - Usuario {username} foi criado\n")
        except IOError as e:
            self.view.show_message(f"Falha ao escrever no log: {e}")