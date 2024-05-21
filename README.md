### Aplicação de Login Minimalista com Flask :lock:

Este é um projeto de uma aplicação web minimalista desenvolvida com Flask, que oferece funcionalidades de registro e login de usuários, conectada a um banco de dados SQLite. :computer:

## Funcionalidades :hammer_and_wrench:
- Registro de Usuário
- Login de Usuário
- Mensagens de feedback usando flash
- Hashing de senhas para segurança

## Requisitos :clipboard:
- Python 3.7+
- Flask
- SQLite
- Werkzeug

## Estrutura de Arquivos :file_folder:
minimalist-flask-login/
├── app.py
├── init_db.py
├── templates/
│ ├── base.html
│ ├── login.html
│ └── register.html
├── static/
│ └── style.css
├── venv/
└── README.md

## Descrição dos Arquivos :page_with_curl:
- **app.py**: Arquivo principal da aplicação contendo a lógica do Flask, rotas e lógica de login e registro.
- **init_db.py**: Script para inicializar o banco de dados SQLite com a tabela users.
- **templates/**: Diretório contendo os templates HTML.
  - **base.html**: Template base estendido pelos outros templates.
  - **login.html**: Template da página de login.
  - **register.html**: Template da página de registro.
- **static/**: Diretório para arquivos estáticos como CSS.
  - **style.css**: Arquivo de estilos para a aplicação.
- **venv/**: Diretório do ambiente virtual.
- **README.md**: Este arquivo README.

## Licença :scroll:
Este projeto está licenciado sob a licença MIT.
