# ADR 0020: Considerar UUID Versao 7

## Status

Proposta

## Decisao

Considerar UUID versao 7 como estrategia preferencial para chaves primarias se a
versao do PostgreSQL, extensoes e bibliotecas adotadas suportarem UUIDv7 de
forma simples e confiavel.

Se a infraestrutura ainda nao oferecer suporte maduro, UUIDv4 permanece como
escolha solida.

## Motivo

UUIDv7 preserva as vantagens de UUIDs, como seguranca para APIs e baixa
exposicao de sequencias internas, mas melhora a ordenacao temporal e pode
reduzir parte do custo de indices em comparacao com UUIDv4.

## Consequencias

- A decisao final deve ocorrer antes da primeira migration.
- O modelo logico continua declarando `uuid`; a versao exata sera definida no
  modelo fisico.
- Architecture Review 2.0 deve validar suporte operacional a UUIDv7.
