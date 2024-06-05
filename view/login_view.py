import tkinter as tk
from controller.login_controller import LoginController
from controller.register_controller import RegisterController
from view.main_view import MainView

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login / Registrar")
        self.root.geometry("340x340")
        self.root.configure(bg="#333333")

        self.controller = LoginController(self)
        self.register_controller = RegisterController(self)

        self.create_login_widgets()

    def create_login_widgets(self):
        self.clear_widgets()

        self.username_label = tk.Label(self.root, text="Nome de Usuário", bg="#333333", fg="white")
        self.username_label.pack(pady=(10, 5))
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=(0, 10))

        self.password_label = tk.Label(self.root, text="Senha", bg="#333333", fg="white")
        self.password_label.pack(pady=(10, 5))
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(pady=(0, 20))
        

        self.login_button = tk.Button(self.root, text="Entrar", command=self.controller.login, bg="#FF3399", fg="#ffffff", width=20)
        self.login_button.pack(pady=(0, 10))

        self.register_button = tk.Button(self.root, text="Registrar", command=self.create_register_widgets,bg="#FF3399", fg="#ffffff", width=20)
        self.register_button.pack(pady=(0, 10))


        self.close_button = tk.Button(self.root, text="Fechar", command=self.root.destroy,bg="#FF3399", fg="#ffffff", width=20)
        self.close_button.pack(pady=(0, 10))


        self.message = tk.Label(self.root, text="", fg="white", bg="#333333")
        self.message.pack(pady=(10, 10))

    def create_register_widgets(self):
        self.clear_widgets()

        self.username_label = tk.Label(self.root, text="Nome de Usuário", bg="#333333", fg="white")
        self.username_label.pack(pady=(10, 5))
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=(0, 10))

        self.password_label = tk.Label(self.root, text="Senha", bg="#333333", fg="white")
        self.password_label.pack(pady=(10, 5))
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(pady=(0, 10))

        self.confirm_password_label = tk.Label(self.root, text="Confirmar Senha", bg="#333333", fg="white")
        self.confirm_password_label.pack(pady=(10, 5))
        self.confirm_password_entry = tk.Entry(self.root, show='*')
        self.confirm_password_entry.pack(pady=(0, 20))

        self.register_button = tk.Button(self.root, text="Registrar", command=self.register, bg="#FF3399", fg="#ffffff",width=20)
        self.register_button.pack(pady=(0, 10))

        self.back_button = tk.Button(self.root, text="Voltar", command=self.create_login_widgets, bg="#FF3399", fg="#ffffff",width=20)
        self.back_button.pack(pady=(0, 10))

        self.message = tk.Label(self.root, text="", fg="green", bg="#333333")
        self.message.pack(pady=(10, 10))

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register(self):
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            self.show_message("As senhas não coincidem")
        else:
            self.register_controller.register()

    def show_message(self, message):
        self.message.config(text=message)

    def redirect_main_page(self):
        self.root.destroy()
        main_root = tk.Tk()
        MainView(main_root)
        main_root.mainloop()
