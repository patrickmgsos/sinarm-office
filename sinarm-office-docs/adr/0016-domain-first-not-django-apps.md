# ADR 0016: Pensar Em Dominios Antes De Apps Django

## Status

Aceita

## Decisao

A modelagem do SINARM Office deve ser orientada por dominios de negocio, nao por
apps Django.

Apps Django serao uma consequencia tecnica posterior.

## Motivo

Organizar primeiro por apps induz decisoes de framework antes de compreender o
conhecimento do sistema. O produto precisa preservar linguagem de dominio,
limites de contexto e regras de negocio independentes de Django.

## Consequencias

- Documentacao usa Customer Domain, Firearms Domain, Case Management Domain e
  outros dominios.
- Backend futuro deve respeitar esses limites.
- Imports e dependencias devem refletir contratos, nao conveniencia tecnica.
