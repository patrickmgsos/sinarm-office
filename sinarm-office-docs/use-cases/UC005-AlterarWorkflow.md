# UC005 - Alterar Workflow

## Objetivo

Mover processo entre etapas por transicao valida.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Processo existente.
- Workflow ativo.
- Transicao permitida.

## Fluxo Principal

1. Usuario solicita mudanca de etapa.
2. Sistema verifica transicao permitida.
3. Sistema valida pendencias obrigatorias.
4. Sistema move processo para nova etapa.
5. Sistema registra historico de workflow.
6. Sistema gera tarefas e notificacoes quando configurado.
7. Sistema registra auditoria.

## Regras De Negocio

- Nenhuma mudanca de etapa ocorre sem transicao valida.
- Toda transicao registra usuario, data e etapa anterior.
- Transicoes criticas podem exigir justificativa.

## Eventos

- ProcessoMovidoDeEtapa.
- TransicaoBloqueada.
