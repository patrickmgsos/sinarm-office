# SINARM Office Backend

Backend do ERP juridico SINARM Office.

## Stack

- Python 3.13
- Django 5.2
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Pytest
- Ruff
- Black
- Mypy
- Docker

## Arquitetura

O backend usa Django com configuracoes por ambiente e apps organizadas por
contextos do produto. A fundacao esta preparada para Clean Architecture e DDD
pragmatico, sem regras de negocio implementadas nesta etapa.

## Execucao Local

```powershell
cd sinarm-office-backend
..\.venv\Scripts\python.exe manage.py check
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py runserver
```

No PowerShell, com o ambiente virtual ativado:

```powershell
python manage.py check
python manage.py migrate
python manage.py runserver
```

## Docker

```bash
docker compose up --build
```

## Apps Iniciais

- accounts
- clientes
- armas
- processos
- documentos
- modelos
- auditoria
- workflows
- ia
- dashboard
- core
- common
- health
- identity
- organization
- audit
- configuration
- notification

## Endpoints Tecnicos

- `GET /health/`: verifica se o processo Django responde.
- `GET /health/db/`: verifica conexao com o banco principal.
- `GET /health/redis/`: verifica cache/Redis.
- `GET /health/celery/`: verifica configuracao Celery.
- `GET /health/storage/`: verifica storage padrao.
