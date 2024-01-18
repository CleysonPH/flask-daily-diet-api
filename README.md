# Daily Diet API

Projeto de API para controle de dieta diária feito como resolução do desafio referente ao módulo: Desenvolvimento Avançado com Flask da Rocketseat.

## Sobre o desafio

Nesse desafio desenvolveremos uma API para controle de dieta diária, a Daily Diet API.

### Regras da aplicação

- Deve ser possível registrar uma refeição feita, com as seguintes informações:
  - Nome
  - Descrição
  - Data e Hora
  - Está dentro ou não da dieta
- Deve ser possível editar uma refeição, podendo alterar todos os dados acima
- Deve ser possível apagar uma refeição
- Deve ser possível listar todas as refeições de um usuário
- Deve ser possível visualizar uma única refeição
- As informações devem ser salvas em um banco de dados

## Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

## Como executar o projeto

Com o Poetry instalado, execute os comandos abaixo:

```bash
# Clonar o repositório
git clone https://github.com/CleysonPH/flask-daily-diet-api.git

# Entrar no diretório
cd flask-daily-diet-api

# Criar o arquivo .env
cp .env.example .env

# Criar um ambiente virtual com Poetry
poetry shell

# Instalar as dependências
poetry install

# Iniciar o banco de dados com o Docker Compose
docker-compose up -d

# Executar as migrações
poetry run flask db upgrade

# Iniciar a aplicação
poetry run flask run
```

Caso não queira utilizar o Poetry, execute os comandos abaixo:

```bash
# Clonar o repositório
git clone https://github.com/CleysonPH/flask-daily-diet-api.git

# Entrar no diretório
cd flask-daily-diet-api

# Criar o arquivo .env
cp .env.example .env

# Criar um ambiente virtual
python -m venv .venv

# Ativar o ambiente virtual
source .venv/bin/activate

# Instalar as dependências de desenvolvimento
pip install -r requirements-dev.txt

# Iniciar o banco de dados com o Docker Compose
docker-compose up -d

# Executar as migrações
flask db upgrade

# Iniciar a aplicação
flask run
```

## Como executar os testes

```bash
# Executar os testes
poetry run pytest
```

## Como executar o lint

```bash
# Executar o lint
poetry run flake8
```