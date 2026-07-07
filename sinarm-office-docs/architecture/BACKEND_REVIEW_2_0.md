# Backend Review 2.0

## Status

Aprovada com observacoes nao bloqueantes.

## Data

2026-07-07

## Branch Revisada

`feat/backend-2-platform-services`

## Commits Revisados

- `072096d feat: implement technical audit domain`
- `12d4679 feat: implement organization domain`
- `30dcffe Implement identity domain`
- `afea539 Implement configuration domain`
- `05d6e3e Implement notification domain`

## Objetivo

Revisar os dominios tecnicos da Sprint Backend 2 antes da abertura de PR,
confirmando que a plataforma avancou em auditabilidade, organizacao,
identidade, configuracao e notificacoes sem antecipar dominio juridico.

## Escopo

- `sinarm-office-backend/apps/common`
- `sinarm-office-backend/apps/audit`
- `sinarm-office-backend/apps/organization`
- `sinarm-office-backend/apps/identity`
- `sinarm-office-backend/apps/configuration`
- `sinarm-office-backend/apps/notification`
- `sinarm-office-backend/config/settings`
- migrations dos apps tecnicos
- testes dos apps tecnicos

## Resultado Executivo

A Sprint Backend 2 esta adequada para seguir para PR apos esta revisao.

Nao foram encontrados models, services ou selectors de dominio juridico nos
apps revisados. Os apps adicionados permanecem tecnicos e tratam apenas de
fundacoes de plataforma: auditoria, multiempresa futura, autenticacao e RBAC,
configuracoes runtime e fila historica de notificacoes.

## Achados

### Bloqueadores

Nenhum.

### Nao Bloqueantes

1. O banco local `db.sqlite3` criado antes da introducao de
   `AUTH_USER_MODEL = "identity.CustomUser"` pode apresentar historico de
   migrations inconsistente. Isso e esperado em ambiente de desenvolvimento e
   deve ser resolvido recriando o banco local antes de migrar com settings dev.

2. O executavel compilado do Black no ambiente Windows travou repetidamente em
   `--check`. Antes de travar, quando havia diferenca, ele apontou o arquivo
   afetado; apos ajustes, nao apontou novos arquivos. Como `ruff format
   --check`, `ruff check` e `mypy` passaram, isso foi classificado como
   observacao ambiental e nao bloqueia a sprint.

## Checklist De Revisao

| Item | Resultado | Evidencia |
| --- | --- | --- |
| Nenhum dominio juridico implementado | Aprovado | Busca por `Customer`, `Firearm`, `Case`, `Document`, `Cliente`, `Arma`, `Processo`, `Documento` nao encontrou implementacoes nos apps tecnicos; referencias aparecem apenas em `INSTALLED_APPS` dos scaffolds existentes |
| Dependencias entre apps tecnicos | Aprovado | `common` e base; `identity` depende de `common`; `organization` depende de `common` e user swappable; `audit` usa user swappable e `organization_id`; `configuration` depende de `organization`; `notification` depende de `organization` e user swappable |
| Models | Aprovado | Todos usam UUID via `BaseModel`; `ArchivableModel` aplicado a entidades arquivaveis; indices e constraints foram criados para consultas/status/escopo |
| Services | Aprovado | Services encapsulam criacao, arquivamento e transicoes tecnicas; notification nao envia mensagens reais |
| Selectors | Aprovado | Query helpers focados por status, escopo, usuario, entidade e organizacao |
| Admin | Aprovado | Admin registrado para os modelos tecnicos com filtros, buscas e campos readonly |
| Tests | Aprovado | Testes cobrem models, services e selectors dos dominios tecnicos |
| Migrations | Aprovado | Migrations iniciais aplicam em banco limpo com settings de teste |
| `AUTH_USER_MODEL` | Aprovado | `config/settings/base.py` define `AUTH_USER_MODEL = "identity.CustomUser"` |
| Multiempresa futura | Aprovado | `Organization`, `Office` e `Department`; escopos por organizacao em configuration/notification; identity e audit preservam `organization_id` tecnico |
| Audit dedicado | Aprovado | `AuditEventType`, `AuditSession` e `AuditEvent` em app proprio, sem dependencia de dominio juridico |
| Configuration sem segredos | Aprovado | `SettingValueMixin.clean()` rejeita chaves contendo `api_key`, `credential`, `password`, `private_key`, `secret` e `token` |
| Notification sem envio real | Aprovado | Services apenas criam mensagens, marcam status e registram delivery attempts; nenhuma chamada SMTP/API/Celery foi implementada |

## Dependencias Tecnicas

```text
common
  -> Django settings auth references only

identity
  -> common
  -> django.contrib.auth

organization
  -> common
  -> settings.AUTH_USER_MODEL through BaseModel/ArchivableModel

audit
  -> common
  -> settings.AUTH_USER_MODEL
  -> organization_id as UUID, without FK to Organization

configuration
  -> common
  -> organization
  -> settings.AUTH_USER_MODEL through BaseModel/ArchivableModel

notification
  -> common
  -> organization
  -> settings.AUTH_USER_MODEL
```

Essa direcao esta aceitavel para a Sprint Backend 2. `audit` foi mantido mais
desacoplado por usar `organization_id` em vez de FK direta, preservando sua
funcao transversal.

## Revisao Por Dominio

### Common

`BaseModel` centraliza UUID, timestamps e user stamps. `ArchivableModel` fornece
arquivamento opt-in. Nao ha dependencia de apps juridicos.

### Organization

`Organization`, `Office` e `Department` modelam a estrutura tecnica minima para
multiempresa futura. Constraints por codigo dentro da organizacao evitam colisao
entre filiais/departamentos. O app nao implementa billing, assinatura, plano ou
regra juridica.

### Audit

Audit permanece como dominio tecnico dedicado. `AuditEventType`, `AuditSession`
e `AuditEvent` registram ator, acao, entidade generica, metadados e contexto de
organizacao. Nao conhece Customer, Firearm, Case ou Document.

### Identity

`CustomUser` esta configurado como `AUTH_USER_MODEL` antes dos dominios
juridicos. `Role`, `Permission`, `UserRole` e `UserSession` cobrem RBAC tecnico
e sessoes sem depender de apps juridicos. Escopo multiempresa foi preservado por
`organization_id`.

### Configuration

`SystemSetting` e `OrganizationSetting` suportam valores string, boolean,
integer, decimal e JSON. Chaves sao unicas por escopo. A protecao contra
segredos esta implementada por validacao de chave e coberta por teste.

### Notification

`NotificationChannel`, `NotificationTemplate`, `NotificationMessage` e
`NotificationDelivery` modelam canais, templates, fila/status e historico de
tentativas. Os canais previstos (`email`, `whatsapp`, `sms`, `system`) e os
status (`pending`, `queued`, `sent`, `failed`, `cancelled`) estao representados.
Nao ha envio real.

## Migrations

O grafo aplica corretamente em banco limpo usando `config.settings.test`.

Pontos relevantes:

- `identity.0001_initial` depende apenas de `auth`.
- `organization.0001_initial` usa `migrations.swappable_dependency`.
- `audit.0001_initial` usa user swappable e nao depende de organization.
- `configuration.0001_initial` depende de organization e user swappable.
- `notification.0001_initial` depende de organization e user swappable.

## Comandos Executados

```powershell
..\.venv\Scripts\python.exe manage.py check
..\.venv\Scripts\python.exe manage.py makemigrations --check --dry-run --settings=config.settings.test
..\.venv\Scripts\pytest.exe apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification tests -q --no-migrations
..\.venv\Scripts\ruff.exe check apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification config --no-cache
..\.venv\Scripts\ruff.exe format --check --no-cache apps/identity apps/configuration apps/notification
..\.venv\Scripts\mypy.exe apps/common apps/core apps/health apps/audit apps/organization apps/identity apps/configuration apps/notification config
..\.venv\Scripts\python.exe manage.py migrate --settings=config.settings.test --noinput
```

Nota: os comandos foram executados a partir de `sinarm-office-backend`. O
interpretador usado foi o virtualenv em `D:\despachante\.venv`.

## Resultados De Validacao

| Comando | Resultado |
| --- | --- |
| `manage.py check` | Passou, sem issues |
| `makemigrations --check --dry-run --settings=config.settings.test` | Passou, sem mudancas pendentes |
| `pytest ... --no-migrations` | Passou, 53 testes |
| `ruff check ... --no-cache` | Passou |
| `ruff format --check --no-cache` | Passou nos apps tecnicos adicionados |
| `mypy ...` | Passou, 85 arquivos |
| `migrate --settings=config.settings.test --noinput` | Passou, migrations aplicadas em banco limpo |

## Observacao Sobre Banco Local

Como `AUTH_USER_MODEL` foi definido nesta sprint, qualquer `db.sqlite3` local
criado antes de `identity.0001_initial` pode ficar inconsistente. Para ambiente
de desenvolvimento, recriar o banco local antes de migrar e a abordagem
recomendada.

## Decisao

Backend 2.0 aprovado para PR apos esta revisao.

Antes do PR, manter a branch sem alteracoes pendentes e incluir este documento
como evidencia da revisao tecnica.
