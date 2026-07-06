# ADR 0017: UUID Como Chave Primaria No PostgreSQL

## Status

Aceita

## Decisao

Usar UUID como chave primaria das tabelas de dominio no PostgreSQL.

## Motivo

UUIDs reduzem exposicao de IDs sequenciais, facilitam integracoes futuras,
sincronizacao entre ambientes e eventual evolucao para arquitetura distribuida.
PostgreSQL possui suporte maduro para UUID.

## Consequencias

- Todas as tabelas de dominio devem usar `id uuid primary key`.
- IDs publicos de APIs nao revelam volume ou ordem de criacao.
- Indices ficam maiores que `bigint`, exigindo disciplina de indexacao.
- A geracao padrao sera definida na Fase 3 fisica, provavelmente com
  `gen_random_uuid()`.
