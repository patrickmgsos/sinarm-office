# Sprint 2 - Domain Model

## Objetivo

Modelar banco de dados e limites de dominio antes dos Models Django.

## Escopo

- Modelo conceitual de negocio.
- Modelo logico com tabelas, chaves, cardinalidades e restricoes.
- Modelo fisico preparado para PostgreSQL e Django.
- Mapeamento DDD de agregados, eventos, services e repositories.

## Fora De Escopo

- Criar `models.py`.
- Criar migrations.
- Implementar views, APIs ou templates.

## Principios

- Nada sera apagado do banco sem decisao explicita.
- Alteracoes importantes geram auditoria.
- Regras de negocio passam por services e repositories.
- Organizacao prepara multiempresa.
- ACL deve representar perfis reais de escritorio juridico.
