# API FastAPI com Docker e Poetry

Projeto desenvolvido como atividade prática do curso Desenvolvedor Full Stack Python da EBAC.

## Tecnologias utilizadas

- Python 3.12
- FastAPI
- Docker
- Docker Compose
- Poetry
- Uvicorn

## Funcionalidades

A API permite:

- Listar tarefas
- Cadastrar tarefas
- Excluir tarefas
- Consultar a documentação interativa da API

## Como executar

### 1. Pré-requisitos

Ter Docker e Docker Compose instalados.

### 2. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/fastapi-docker-poetry.git
cd fastapi-docker-poetry
```

Substitua `SEU-USUARIO` pelo usuário do GitHub onde o projeto for publicado.

### 3. Construir e iniciar o container

```bash
docker compose up --build -d
```

### 4. Acessar a aplicação

API: http://localhost:8000

Documentação Swagger: http://localhost:8000/docs

### 5. Visualizar os logs

```bash
docker compose logs -f api
```

### 6. Encerrar a aplicação

```bash
docker compose down
```

## Gerenciamento de dependências

O projeto utiliza Poetry para instalar e gerenciar as dependências Python diretamente no container.

O arquivo `pyproject.toml` define as dependências e o `poetry.lock` registra suas versões resolvidas.

## Desenvolvimento

O Docker Compose configura um volume que sincroniza os arquivos locais com o container.

O Uvicorn utiliza `--reload` para atualizar a aplicação durante o desenvolvimento.

## Observações

Os dados das tarefas são armazenados temporariamente em memória.

Projeto desenvolvido para fins educacionais.
