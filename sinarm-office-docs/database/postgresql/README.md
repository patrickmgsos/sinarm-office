# PostgreSQL Logical Model

## Objetivo

Projetar o banco PostgreSQL antes de qualquer `models.py`, migration ou codigo
Python de dominio.

## Principios

- UUID como chave primaria.
- Avaliar UUIDv7 antes da primeira migration, com fallback para UUIDv4.
- Integridade referencial explicita.
- Indices planejados por consultas reais.
- Status e arquivamento em vez de `deleted`.
- Auditoria como dominio proprio.
- Separacao por dominios.
- Nomes tecnicos em ingles; interface e documentacao de usuario em portugues.
- PostgreSQL primeiro, Django depois.

## Dominios

- Core Domain.
- Customer Domain.
- Firearms Domain.
- Case Management Domain.
- Document Domain.
- Legal Automation Domain.
- Knowledge Domain.
- Compliance Domain.
- Reference Data Domain.
- Integration Domain.

## Documentos

- table-catalog.md
- table-classification.md
- indexing-strategy.md
- integrity-rules.md
- foreign-key-policy.md
- naming-conventions.md
- architecture-review-2-checklist.md
