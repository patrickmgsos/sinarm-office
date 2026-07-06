# UC008 - Protocolar Processo

## Objetivo

Registrar protocolo do processo junto a Policia Federal.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Processo em etapa que permita protocolo.
- Documentos obrigatorios revisados.

## Fluxo Principal

1. Usuario informa dados do protocolo.
2. Usuario anexa comprovante quando houver.
3. Sistema valida documentos obrigatorios.
4. Sistema registra data e numero de protocolo.
5. Sistema move processo para etapa posterior.
6. Sistema gera alerta de acompanhamento.
7. Sistema registra auditoria.

## Regras De Negocio

- Protocolo deve possuir data.
- Comprovante deve ser preservado quando anexado.
- Transicao deve respeitar workflow.

## Eventos

- ProcessoProtocolado.
