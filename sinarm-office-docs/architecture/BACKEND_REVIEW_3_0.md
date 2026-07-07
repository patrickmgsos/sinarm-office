# Backend Review 3.0

## Status

Aprovada.

## Data

2026-07-07

## Branch Revisada

`feat/backend-3-reference-data`

## Commits Revisados

- `24bfcef feat: add firearm reference data`
- `434ab30 feat: add geographic reference data`
- `35ef627 feat: add reference type catalogs`

## Objetivo

Revisar o dominio tecnico `reference_data` antes da abertura de PR,
confirmando que a sprint adicionou apenas catalogos de referencia e nao
entidades juridicas ou operacionais reais.

## Escopo

- `sinarm-office-backend/apps/reference_data`
- migrations de `reference_data`
- testes de `reference_data`
- `sinarm-office-backend/config/settings`
- `sinarm-office-docs/architecture`

## Resultado Executivo

A Sprint Backend 3 esta adequada para seguir para PR.

O app `reference_data` concentra dados referenciais tecnicos para:

- fabricantes, calibres e modelos de arma, sem criar `Firearm`;
- paises, estados e cidades;
- tipos/categorias para caso, documento, workflow e status, sem criar `Case`,
  `Document` ou `Workflow` real.

## Achados

### Bloqueadores

Nenhum.

### Nao Bloqueantes

1. As migrations de `reference_data` possuem
   `migrations.swappable_dependency(settings.AUTH_USER_MODEL)` porque os modelos
   herdam `BaseModel`, que inclui user stamps. No codigo do app, a dependencia
   direta permanece restrita a `common` e ao proprio `reference_data`.

2. As migrations `0002` e `0003` usam `# ruff: noqa: I001` para preservar a
   formatacao gerada/formatada pelo Django/Ruff sem conflitar com a ordenacao de
   imports em arquivo gerado. O lint e o format check passam.

## Checklist De Revisao

| Item | Resultado | Evidencia |
| --- | --- | --- |
| Nenhuma entidade real criada | Aprovado | Busca por `class Customer`, `class Firearm(`, `class Case(`, `class Document(` e `class Workflow(` nao encontrou entidades reais em `apps/reference_data` |
| Sem dependencia de apps juridicos | Aprovado | Imports de `reference_data` restritos a Django, `apps.common` e `apps.reference_data` |
| `Manufacturer` | Aprovado | UUID/BaseModel, arquivavel, `name` unico, pais opcional e observacoes |
| `Caliber` | Aprovado | UUID/BaseModel, arquivavel, `name` unico, categoria e descricao opcionais |
| `FirearmModel` | Aprovado | Referencia `Manufacturer` e `Caliber` opcional; unico por `manufacturer + name`; nao cria `Firearm` |
| `Country` | Aprovado | UUID/BaseModel, arquivavel, `iso2` unico, `iso3` unico, phone code opcional |
| `State` | Aprovado | FK para `Country`; unico por `country + name`; code opcional |
| `City` | Aprovado | FK para `State`; unico por `state + name`; `ibge_code` opcional |
| `CaseType` | Aprovado | Catalogo com `name`, `code`, `description`, `is_system`; sem criar `Case` |
| `DocumentType` | Aprovado | Catalogo com `name`, `code`, `description`, `is_system`; sem criar `Document` |
| `WorkflowType` | Aprovado | Catalogo com `name`, `code`, `description`, `is_system`; sem criar `Workflow` |
| `StatusType` | Aprovado | Catalogo com `name`, `code`, `description`, `is_system` |
| Admin | Aprovado | Todos os modelos registrados com filtros, buscas e readonly fields |
| Services | Aprovado | Criacao e arquivamento de registros referenciais; sem regras de dominio juridico |
| Selectors | Aprovado | Query helpers para ativos e escopos naturais |
| Tests | Aprovado | Testes cobrem models, services, selectors e unicidades |
| Migrations | Aprovado | `0001`, `0002` e `0003` aplicam em banco limpo com settings de teste |

## Dependencias

```text
reference_data
  -> apps.common
  -> apps.reference_data
```

Nao ha imports para `apps.clientes`, `apps.armas`, `apps.processos`,
`apps.documentos` ou `apps.workflows`.

## Revisao Por Grupo

### Firearm Reference Data

`Manufacturer`, `Caliber` e `FirearmModel` modelam catalogos necessarios para
futuro cadastro de armas. `FirearmModel` e apenas referencia; nao possui numero
de serie, proprietario, registro, processo ou qualquer atributo de arma real.

### Geographic Reference Data

`Country`, `State` e `City` formam hierarquia geografica simples. As unicidades
evitam duplicidade nos escopos corretos sem antecipar regras de endereco,
cliente ou processo.

### Case, Document, Workflow And Status Types

`CaseType`, `DocumentType`, `WorkflowType` e `StatusType` sao catalogos
independentes. Eles definem nomes/codigos para uso futuro, mas nao implementam
casos, documentos, workflows, status de processo, transicoes ou regras
juridicas.

## Migrations

O grafo de migrations esta coerente:

- `0001_initial`: fabricantes, calibres e modelos de arma referenciais.
- `0002_country_state_city_and_more`: paises, estados e cidades.
- `0003_casetype_documenttype_statustype_workflowtype`: catalogos de tipos.

Todas aplicam em banco limpo usando `config.settings.test`.

## Comandos Executados

```powershell
..\.venv\Scripts\python.exe manage.py check
..\.venv\Scripts\python.exe manage.py makemigrations --check --dry-run --settings=config.settings.test
..\.venv\Scripts\pytest.exe apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification apps/reference_data tests -q --no-migrations
..\.venv\Scripts\ruff.exe check apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification apps/reference_data config --no-cache
..\.venv\Scripts\ruff.exe format --check --no-cache apps/reference_data
..\.venv\Scripts\mypy.exe apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification apps/reference_data config
..\.venv\Scripts\python.exe manage.py migrate --settings=config.settings.test --noinput
```

## Resultados De Validacao

| Comando | Resultado |
| --- | --- |
| `manage.py check` | Passou, sem issues |
| `makemigrations --check --dry-run --settings=config.settings.test` | Passou, sem mudancas pendentes |
| `pytest ... --no-migrations` | Passou, 73 testes |
| `ruff check ... --no-cache` | Passou |
| `ruff format --check --no-cache apps/reference_data` | Passou |
| `mypy ...` | Passou, 102 arquivos |
| `migrate --settings=config.settings.test --noinput` | Passou, migrations aplicadas em banco limpo |

## Decisao

Backend 3.0 aprovado para PR.

Proxima etapa apos merge: avancar para os primeiros dominios operacionais usando
os catalogos de referencia como base, sem misturar catalogo com entidade real.
