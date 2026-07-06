# Banco De Dados

## Direcao Inicial

O banco principal sera PostgreSQL. Redis sera usado para cache, filas e suporte
a tarefas assincronas com Celery.

## Principios

- Chaves primarias estaveis.
- Indices planejados por consultas reais.
- Constraints no banco para invariantes criticas.
- Auditoria para entidades sensiveis.
- Campos de rastreabilidade em entidades relevantes.
- Migrations revisadas antes de producao.

## Topicos A Documentar

- Modelo conceitual.
- Modelo logico.
- Diagrama entidade-relacionamento.
- Estrategia de indices.
- Estrategia de backup e restore.
- Politica de retencao conforme LGPD.
- Classificacao de dados sensiveis.

## PostgreSQL

O diretorio `postgresql/` contem a Sprint PostgreSQL Logical Model, ainda sem
Django Models e sem migrations.
