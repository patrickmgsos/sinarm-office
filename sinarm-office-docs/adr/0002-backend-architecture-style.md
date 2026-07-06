# ADR 0002: Estilo Arquitetural Do Backend

## Status

Proposta

## Contexto

O backend do SINARM Office tera modulos como Accounts, Clientes, Armas,
Processos, Documentos, Modelos, IA, Agenda, Financeiro, Relatorios,
Notificacoes, Auditoria e Configuracoes.

Misturar regras de negocio em views, serializers, forms ou templates aumentaria
o custo de manutencao e dificultaria testes.

## Decisao

Adotar Django 5 com Clean Architecture pragmatica e DDD por contexto delimitado.

Cada app principal deve organizar suas responsabilidades em camadas:

```text
domain/
application/
infrastructure/
interfaces/
tests/
```

## Regras

- Models Django representam persistencia e invariantes simples.
- Services concentram casos de uso.
- Repositories encapsulam consultas complexas.
- Views e APIs apenas coordenam entrada e saida.
- Templates nao possuem regra de negocio.
- Consultas devem evitar N+1 com select_related, prefetch_related e indices.

## Consequencias

O codigo inicial fica mais estruturado e exige mais disciplina, mas o sistema se
torna mais testavel, previsivel e preparado para crescimento.
