# Backend Roadmap

## Principio

O backend sera implementado em camadas de produto, preservando a separacao entre
fundacao tecnica, dominios tecnicos e dominios juridicos.

## Backend 0: Foundation

Status: em PR.

- Django executavel.
- Settings por ambiente.
- PostgreSQL, Redis, Celery e DRF preparados.
- `BaseModel` inicial.
- Health check simples.
- Qualidade de codigo validada.

## Backend 1: Core Platform

Status: em PR.

- Apps tecnicos.
- `common`.
- `core`.
- `health`.
- Mixins.
- Excecoes.
- Logging estruturado inicial.
- ADR-0022.
- Architecture Review Backend 1.0.

## Backend 2: Platform Services

Status: proximo.

Implementar models tecnicos sem conhecimento do SINARM:

- Identity.
- Organization.
- Audit.
- Configuration.
- Notification.

Gate:

- Sem Customer, Firearm, Case ou Document.
- Sem regras juridicas.
- Architecture Review Backend 2.0 antes do primeiro dominio juridico.

## Backend 3: Reference Data

Status: pendente.

Implementar dados de referencia reutilizaveis:

- Manufacturers.
- Firearm Models.
- Calibers.
- Countries.
- States.
- Cities.
- Document Types.
- Case Types.
- Workflow Types.
- Status Types.

## Backend 4: Customer Domain

Status: pendente.

Primeiro dominio de negocio:

- Customer.
- Customer Address.
- Customer Contact.
- Customer Email.
- Customer Phone.

Fora de escopo nesta fase:

- Processos.
- Armas.
- Documentos.
- Workflow juridico.

## Backend 5: Firearms Domain

Status: pendente.

- Firearm.
- Registration.
- Owner History.

## Fases Posteriores

- Case Management.
- Documents.
- Workflow.
- Legal Automation.
- IA assistiva.

## Regra De Sequenciamento

O dominio juridico so deve iniciar apos Platform Services, Reference Data e
Backend Review 2.0 estarem aprovados.
