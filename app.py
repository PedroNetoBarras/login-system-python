import sqlite3
import bcrypt
import customtkinter as ctk
from tkinter import messagebox

# Função para criar o banco de dados e a tabela de usuários
def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para registrar um novo usuário
def register_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_pw))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Nome de usuário já existe!")
    conn.close()

# Função para autenticar o usuário
def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos!")

# Função para exibir a tela de registro
def show_register():
    def submit_registration():
        username = entry_username.get()
        password = entry_password.get()
        if username and password:
            register_user(username, password)
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    register_window = ctk.CTkToplevel()
    register_window.title("Registrar")

    ctk.CTkLabel(register_window, text="Nome de Usuário").pack(pady=5)
    entry_username = ctk.CTkEntry(register_window)
    entry_username.pack(pady=5)

    ctk.CTkLabel(register_window, text="Senha").pack(pady=5)
    entry_password = ctk.CTkEntry(register_window, show="*")
    entry_password.pack(pady=5)

    ctk.CTkButton(register_window, text="Registrar", command=submit_registration).pack(pady=10)

# Função para exibir a tela de login
def show_login():
    def submit_login():
        username = entry_username.get()
        password = entry_password.get()
        if username and password:
            login_user(username, password)
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    login_window = ctk.CTkToplevel()
    login_window.title("Login")

    ctk.CTkLabel(login_window, text="Nome de Usuário").pack(pady=5)
    entry_username = ctk.CTkEntry(login_window)
    entry_username.pack(pady=5)

    ctk.CTkLabel(login_window, text="Senha").pack(pady=5)
    entry_password = ctk.CTkEntry(login_window, show="*")
    entry_password.pack(pady=5)

    ctk.CTkButton(login_window, text="Login", command=submit_login).pack(pady=10)

# Função principal
def main():
    create_db()

    root = ctk.CTk()
    root.title("Sistema de Login")

    ctk.CTkButton(root, text="Registrar", command=show_register).pack(pady=10)
    ctk.CTkButton(root, text="Login", command=show_login).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
