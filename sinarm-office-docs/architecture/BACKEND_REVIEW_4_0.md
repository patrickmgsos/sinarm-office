# Backend Review 4.0

## Status

Aprovada.

## Data

2026-07-07

## Branch Revisada

`feat/backend-4-customer-domain`

## Commits Revisados

- `c1baaaf docs: define customer domain architecture decisions`
- `06e8af8 feat: implement customer aggregate root`
- `ba03cf5 feat: add find customer by cpf`
- `c1ca9ce feat: add customer archive lifecycle`
- `e2019b8 feat: add customer addresses`
- `4dbe134 feat: add customer contacts`

## Objetivo

Revisar o inicio do Backend 4, confirmando que o dominio `customers` entrega
capacidades de negocio pequenas e explicitas sem antecipar Firearm, Case,
Document, Workflow real ou automacoes juridicas.

## Escopo

- `sinarm-office-backend/apps/customers`
- migrations de `customers`
- testes de `customers`
- integracao opcional com `reference_data` geografico
- `sinarm-office-docs/adr`
- `sinarm-office-docs/governance`
- `sinarm-office-docs/roadmap`

## Resultado Executivo

A Sprint Backend 4 esta adequada para seguir.

O dominio `customers` foi introduzido como primeiro dominio operacional da
plataforma, com `Customer` como Aggregate Root e casos de uso nomeados em
linguagem de negocio:

- Register New Customer;
- Find Customer By CPF;
- Archive Customer;
- Restore Customer;
- Add Customer Address;
- Add Customer Contact.

Nao foram criados CRUDs genericos, telas, APIs, Firearm, Case, Document,
Workflow real ou Legal Automation.

## Achados

### Bloqueadores

Nenhum.

### Nao Bloqueantes

1. O comando amplo de `ruff format --check` em todos os apps apontou arquivos
   herdados de migrations antigas fora do escopo do Backend 4:
   `apps/audit/migrations/0001_initial.py` e
   `apps/organization/migrations/0001_initial.py`. O format check focado em
   `apps/customers` passou. Nao foram alterados arquivos antigos para evitar
   churn fora do dominio revisado.

2. `CustomerAddress` referencia `Country`, `State` e `City` de
   `reference_data` de forma opcional. Essa dependencia e intencional para
   evitar duplicar catalogos geograficos.

3. `ArchiveCustomerService` usa `apps.identity.models.CustomUser` somente em
   `TYPE_CHECKING` para tipar `archived_by`. Em runtime, a relacao continua
   vindo do `ArchivableModel` via `settings.AUTH_USER_MODEL`.

## Checklist De Revisao

| Item | Resultado | Evidencia |
| --- | --- | --- |
| Sem Firearm real | Aprovado | Nenhuma entidade `Firearm` foi criada em `apps/customers` |
| Sem Case real | Aprovado | Nenhuma entidade `Case` foi criada em `apps/customers` |
| Sem Document real | Aprovado | Nenhuma entidade `Document` foi criada em `apps/customers` |
| Sem Workflow real | Aprovado | Nenhuma entidade `Workflow` foi criada em `apps/customers` |
| Sem Legal Automation | Aprovado | Nenhum modulo/regra de automacao juridica foi criado |
| Sem GenericForeignKey | Aprovado | Busca por `GenericForeignKey` nao encontrou uso em `apps/customers` |
| Customer Aggregate Root | Aprovado | `Customer` concentra identidade UUID, CPF/CNPJ e ciclo de vida |
| CPF/CNPJ | Aprovado | `document_number` e unico e indexado; UUID permanece identidade primaria |
| Register New Customer | Aprovado | Service, repository, policy, specification, event e testes implementados |
| Find Customer By CPF | Aprovado | Service/selector/repository com normalizacao de CPF |
| Archive/Restore | Aprovado | Services usam `ArchivableModel`; nao ha hard delete |
| CustomerAddress | Aprovado | FK explicita para `Customer`; adicionado via service do dominio |
| CustomerContact | Aprovado | FK explicita para `Customer`; unicidade por cliente/tipo/valor |
| Repositories | Aprovado | Services usam `CustomerRepository` para escrita/leitura persistente |
| Selectors | Aprovado | Queries de leitura para clientes, enderecos e contatos |
| Admin | Aprovado | Customer, Address e Contact registrados com filtros/buscas |
| Tests | Aprovado | Cobrem registro, busca, lifecycle, endereco, contato e selectors |
| Migrations | Aprovado | `0001`, `0002` e `0003` aplicam em banco limpo |

## Dependencias

```text
customers
  -> apps.common
  -> apps.reference_data  (Country, State, City opcionais)
  -> apps.identity        (TYPE_CHECKING para archived_by)
```

Nao ha dependencia de `Customer` para Firearm, Case, Document, Workflow real ou
qualquer modulo juridico futuro.

## Revisao Por Capacidade

### Customer Aggregate Root

`Customer` usa `BaseModel` e `ArchivableModel`, portanto possui UUID,
timestamps, user stamps e status de arquivamento. O CPF/CNPJ e armazenado em
`document_number` com unicidade e indice, mas nao e chave natural.

### Register New Customer

O caso de uso cria clientes pessoa fisica ou juridica via
`RegisterNewCustomerService`. A politica valida duplicidade, formato basico de
CPF/CNPJ e coerencia entre tipo de pessoa e tipo de documento. O evento
`CustomerRegistered` registra o fato de dominio sem publicar integracoes
externas.

### Find Customer By CPF

`FindCustomerByCpfService` normaliza CPF e retorna `Customer | None`, mantendo
ausencia de cadastro como resultado de busca, nao como excecao de negocio.

### Archive And Restore

`ArchiveCustomerService` e `RestoreCustomerService` alteram o ciclo de vida do
aggregate root usando status, `archived_at` e `archived_by`. Nao ha hard delete.

### CustomerAddress

`CustomerAddress` pertence explicitamente a `Customer`. O service
`AddCustomerAddressService` valida cliente, tipo e logradouro, e garante que um
novo endereco principal desmarque o principal anterior do cliente.

### CustomerContact

`CustomerContact` pertence explicitamente a `Customer`. O service
`AddCustomerContactService` normaliza email/telefone/WhatsApp, valida formato
basico, impede duplicidade por cliente/tipo/valor e mantem um contato principal
por tipo.

## Migrations

O grafo de migrations esta coerente:

- `0001_initial`: cria `Customer`.
- `0002_customeraddress`: cria `CustomerAddress`.
- `0003_customercontact`: cria `CustomerContact`.

Todas aplicam em banco limpo usando `config.settings.test`.

## Comandos Executados

```powershell
..\.venv\Scripts\python.exe manage.py check
..\.venv\Scripts\python.exe manage.py makemigrations --check --dry-run --settings=config.settings.test
..\.venv\Scripts\pytest.exe apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification apps/reference_data apps/customers tests -q --no-migrations
..\.venv\Scripts\ruff.exe check apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification apps/reference_data apps/customers config --no-cache
..\.venv\Scripts\ruff.exe format --check --no-cache apps/customers
..\.venv\Scripts\ruff.exe format --check --no-cache apps/customers apps/reference_data apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification config
..\.venv\Scripts\mypy.exe apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification apps/reference_data apps/customers config
..\.venv\Scripts\python.exe manage.py migrate --settings=config.settings.test --noinput
```

## Resultados De Validacao

| Comando | Resultado |
| --- | --- |
| `manage.py check` | Passou, sem issues |
| `makemigrations --check --dry-run --settings=config.settings.test` | Passou, sem mudancas pendentes |
| `pytest ... --no-migrations` | Passou, 101 testes |
| `ruff check ... --no-cache` | Passou |
| `ruff format --check --no-cache apps/customers` | Passou |
| `ruff format --check --no-cache ...` amplo | Nao bloqueante: apontou duas migrations antigas fora do escopo |
| `mypy ...` | Passou, 125 arquivos |
| `migrate --settings=config.settings.test --noinput` | Passou, migrations aplicadas em banco limpo |

## Decisao

Backend 4.0 aprovado.

Proxima etapa sugerida apos merge: evoluir o Customer Domain com componentes
adicionais do agregado somente quando houver caso de uso claro, mantendo a regra
de nao criar CRUD generico e de passar alteracoes do agregado por services do
dominio.
