# Sistema de Gerenciamento de Empresa

Este é um sistema de gerenciamento desenvolvido para adicionar funcionários e times, onde cada funcionário está associado a um time.

## Funcionalidades

- Adicionar, Atualizar, Excluir e Visualizar Funcionários
- Adicionar, Atualizar, Excluir e Visualizar Times
- Criação de cadastros
- Login
- Registro de informações de login e cadaastro em um arquivo de log em formato txt

## Tecnologias Utilizadas

- Python
- Tkinter
- Banco de Dados: SQLite

## Como Executar o Projeto

1. Realize o clone do projeto:
```
git clone https://github.com/Viilih/sistema-gestao-empresa.git
```
2. Execute o comando:
```
python main.py
```


## Regras de Negócio

- Não é possível usar a aplicação sem criar um usuário; portanto, ao iniciar a aplicação, é necessário criar um usuário na seção de registro.
- Um funcionário não pode ser criado sem estar vinculado a um time existente.
- Um funcionário não pode ser criado e vinculado a um time que não existe.
- Todas as ações de cadastro e de login são salvas no arquivo user_log.txt
