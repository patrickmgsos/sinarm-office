# Factory: ProcessoFactory

## Objetivo

Criar processo em estado inicial valido.

## Entradas

- Cliente.
- Tipo de processo.
- Usuario responsavel.
- Armas quando aplicavel.

## Regras

- Seleciona workflow correto.
- Define etapa inicial.
- Valida armas pertencentes ao cliente.
- Emite ProcessoCriado.
