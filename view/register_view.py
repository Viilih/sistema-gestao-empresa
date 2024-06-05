import tkinter as tk
from controller.register_controller import RegisterController

class RegisterView:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar")
        self.controller = RegisterController(self)

        self.username_label = tk.Label(root, text="Nome de usuário")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Senha")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack()

        self.register_button = tk.Button(root, text="Registrar", command=self.controller.register, bg="#FF3399", fg="#ffffff", width=30)
        self.register_button.pack()

        self.message = tk.Label(root, text="", fg="green")
        self.message.pack()

    def show_message(self, message):
        self.message.config(text=message)
