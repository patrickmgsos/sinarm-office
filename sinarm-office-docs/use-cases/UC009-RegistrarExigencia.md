# UC009 - Registrar Exigencia

## Objetivo

Registrar exigencia emitida pela Policia Federal e iniciar fluxo de resposta.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Processo protocolado ou em analise.

## Fluxo Principal

1. Usuario registra exigencia.
2. Usuario informa data, descricao e prazo.
3. Sistema move processo para etapa de exigencia.
4. Sistema cria tarefas de resposta.
5. Sistema gera notificacoes.
6. Sistema registra auditoria.

## Regras De Negocio

- Exigencia deve possuir descricao.
- Prazo deve gerar alertas.
- Pode haver mais de uma exigencia no mesmo processo.

## Eventos

- ExigenciaRegistrada.
