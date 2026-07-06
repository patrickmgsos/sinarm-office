# PostgreSQL Logical Model

## Objetivo

Projetar o banco PostgreSQL antes de qualquer `models.py`, migration ou codigo
Python de dominio.

## Principios

- UUID como chave primaria.
- Integridade referencial explicita.
- Indices planejados por consultas reais.
- Status e arquivamento em vez de `deleted`.
- Auditoria como dominio proprio.
- Separacao por dominios.
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

## Documentos

- table-catalog.md
- indexing-strategy.md
- integrity-rules.md
- architecture-review-2-checklist.md
