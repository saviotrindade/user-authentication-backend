<div align="center">

# Backend de Autenticação de Usuário com FastAPI e MongoDB

</div>

Este é o backend de uma aplicação de autenticação de usuário, desenvolvida em Python com FastAPI e integrada com um banco de dados MongoDB usando Beanie para gerenciamento de modelos.

## Requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python (versão 3.10 ou superior)
- MongoDB

## Instalação

1. Clone este repositório:
git clone https://github.com/saviotrindade/user-authentication-backend

2. Navegue até o diretório do projeto:
cd user-authentication-backend

3. Instale as dependências:
pip install -r requirements.txt

## Configuração

1. Renomeie o arquivo `.env.example` para `.env` e defina as variáveis de ambiente necessárias, como a URL do banco de dados MongoDB e a Secret Key.

## Uso

1. Acesse a pasta 'app':
cd ./app

2. Inicie o servidor:
uvicorn app:app --reload

3. O servidor estará disponível em `http://localhost:8000`.

## Funcionalidades

- **Registro de Usuário**: Endpoint para registrar novos usuários.
- **Login de Usuário**: Endpoint para autenticar usuários e gerar tokens de acesso.
- **Validação de Token**: Endpoint para validar tokens de acesso.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).