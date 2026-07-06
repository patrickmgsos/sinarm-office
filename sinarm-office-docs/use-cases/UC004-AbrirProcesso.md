# UC004 - Abrir Processo

## Objetivo

Criar processo administrativo SINARM para cliente.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Cliente cadastrado.
- Workflow aprovado para o tipo de processo.

## Fluxo Principal

1. Usuario seleciona cliente.
2. Usuario escolhe tipo de processo.
3. Usuario seleciona armas quando aplicavel.
4. Sistema define workflow inicial.
5. Sistema cria processo na etapa inicial.
6. Sistema gera tarefas iniciais.
7. Sistema registra auditoria.

## Regras De Negocio

- Processo deve possuir cliente.
- Processo deve possuir tipo.
- Processo deve iniciar em etapa valida.
- Armas selecionadas devem pertencer ao cliente.

## Eventos

- ProcessoAberto.
- ProcessoWorkflowAlterado.
