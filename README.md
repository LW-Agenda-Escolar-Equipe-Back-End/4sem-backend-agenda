# API Agenda Acadêmica

API REST para gerenciamento de agenda acadêmica de alunos. Desenvolvida com FastAPI, SQLAlchemy e PostgreSQL.

## Pré-requisitos

- Python 3.10+
- pip ou poetry
- PostgreSQL (opcional - pode usar SQLite para desenvolvimento)
- Git

## Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/MarcosAlves90/4sem-backend-agenda.git
cd 4sem-backend-agenda
```

### 2. Crie um ambiente virtual

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

Edite `.env` conforme necessário (padrão já usa SQLite):

```env
DATABASE_URL=sua-url-do-banco
SECRET_KEY=sua-chave-secreta-aqui
```

### 5. Crie as tabelas

Descomente a linha em `app/main.py`:

```python
Base.metadata.create_all(bind=engine)
```

Então execute uma vez e recomente.

### 6. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: [`http://localhost:8000`](http://localhost:8000)

## Documentação

Acesse a documentação interativa:

- **Swagger UI:** [`http://localhost:8000/docs`](http://localhost:8000/docs)
- **ReDoc:** [`http://localhost:8000/redoc`](http://localhost:8000/redoc)
- **Health Check:** [`http://localhost:8000/api/v1/health`](http://localhost:8000/api/v1/health)

## Estrutura do Projeto

```text
4sem-backend-agenda/
├── app/
│   ├── main.py              # Aplicação principal
│   ├── database.py          # Configuração do BD
│   ├── models.py            # Modelos ORM
│   ├── crud.py              # Operações CRUD
│   ├── schemas.py           # Schemas Pydantic
│   └── routers/             # Rotas da API
├── templates/
│   └── index.html           # Página inicial
├── requirements.txt         # Dependências
├── README.md                # Este arquivo
└── .gitignore
```

## Tecnologias

- **FastAPI** - Framework web assíncrono
- **SQLAlchemy** - ORM para banco de dados
- **Pydantic** - Validação de dados
- **Uvicorn** - ASGI server
- **Tailwind CSS** - Estilização (frontend)

## Variáveis de Ambiente

Um arquivo `.env.example` é fornecido como template. Para usar:

1. Copie para `.env`:

```bash
cp .env.example .env
```

1. Configure as variáveis conforme seu ambiente:
   - `DATABASE_URL` - URL de conexão do banco (SQLite ou PostgreSQL)
   - `SECRET_KEY` - Chave secreta para criptografia (gere com `openssl rand -hex 32`)

## Licença

Este projeto está sob licença MIT.
