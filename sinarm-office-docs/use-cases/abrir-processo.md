# Caso De Uso: Abrir Processo

## Objetivo

Criar um processo administrativo SINARM para um cliente.

## Atores

- Usuario interno autorizado.

## Fluxo Principal

1. Usuario seleciona cliente.
2. Usuario informa tipo de processo.
3. Usuario seleciona armas quando aplicavel.
4. Sistema cria processo na etapa inicial do workflow.
5. Sistema gera tarefas e pendencias iniciais.
6. Sistema registra auditoria.

## Regras

- Processo deve iniciar em etapa valida.
- Workflow depende do tipo de processo.
- Nenhum processo deve nascer apenas com status textual livre.
