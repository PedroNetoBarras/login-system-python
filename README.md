# Sistema de Login em Python

Este projeto é um sistema básico de login em Python, que utiliza `CustomTkinter` para a interface gráfica e `sqlite3` para gerenciamento de usuários. O sistema permite que usuários se registrem e façam login, armazenando informações de usuários e senhas criptografadas em um banco de dados SQLite.

## Funcionalidades

1. **Registro de Usuários**
   - Permite que novos usuários se registrem com um nome de usuário e senha.
   - Armazena o nome de usuário e a senha criptografada no banco de dados SQLite.

2. **Login de Usuários**
   - Permite que os usuários façam login com suas credenciais (nome de usuário e senha).
   - Verifica as credenciais no banco de dados SQLite.

3. **Interface Gráfica**
   - Interface gráfica para registro e login de usuários usando `CustomTkinter`.

4. **Banco de Dados**
   - Integra a criação e validação de usuários e senhas a um banco de dados SQLite3.

## Requisitos

- Python 3.x
- `CustomTkinter` - Para a interface gráfica. Instale com: `pip install customtkinter`
- `bcrypt` - Para criptografia de senhas. Instale com: `pip install bcrypt`

## Instalação e Execução

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/your-username/login-system-python.git
   ```

2. **Navegue até o Diretório do Projeto**

   ```bash
   cd login-system-python
   ```

3. **Instale as Dependências**

   Certifique-se de ter o `CustomTkinter` e `bcrypt` instalados:

   ```bash
   pip install customtkinter bcrypt
   ```

4. **Execute o Script**

   Execute o script Python principal para iniciar o sistema de login:

   ```bash
   python seu_script.py
   ```

## Como Funciona

- Ao iniciar o aplicativo, uma janela principal será exibida com opções para "Registrar" e "Login".
- Clique em "Registrar" para abrir a janela de registro, onde você pode criar um novo usuário.
- Clique em "Login" para abrir a janela de login, onde você pode autenticar um usuário existente.

## Estrutura do Código

- `main()`: Inicializa a interface principal e a criação do banco de dados.
- `create_db()`: Cria o banco de dados SQLite e a tabela de usuários, se não existirem.
- `register_user(username, password)`: Registra um novo usuário com senha criptografada.
- `login_user(username, password)`: Verifica as credenciais do usuário para login.
- `show_register()`: Exibe a janela de registro.
- `show_login()`: Exibe a janela de login.

## Contribuições

Se você deseja contribuir com este projeto, sinta-se à vontade para fazer um fork do repositório e enviar pull requests com melhorias ou correções.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para mais informações, entre em contato com [backuppedron@gmail.com](mailto:backuppedron@gmail.com).
