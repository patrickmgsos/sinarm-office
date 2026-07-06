# ADR 0019: Auditoria Como Dominio Proprio

## Status

Aceita

## Decisao

Auditoria sera modelada como dominio proprio baseado em eventos, e nao como
replicacao de colunas de auditoria em todas as tabelas.

## Motivo

Eventos de auditoria permitem rastrear quem, quando, entidade, acao, origem e
valores antes/depois quando pertinente, sem acoplar todas as regras de negocio a
colunas repetidas.

## Consequencias

- Tabelas operacionais podem ter `created_at`, `updated_at`, `created_by` e
  `updated_by` quando isso agregar valor.
- A trilha juridica oficial fica em `audit_events`.
- Auditoria deve ser append-only.
- Alteracoes importantes devem emitir eventos auditaveis.
