# UC010 - Arquivar Processo

## Objetivo

Encerrar operacionalmente processo mantendo historico consultavel.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Processo existente.
- Usuario possui permissao para arquivar.

## Fluxo Principal

1. Usuario solicita arquivamento.
2. Sistema verifica pendencias impeditivas.
3. Usuario informa motivo.
4. Sistema move processo para etapa arquivada.
5. Sistema preserva historico e documentos.
6. Sistema registra auditoria.

## Regras De Negocio

- Arquivamento exige motivo.
- Processo arquivado permanece consultavel.
- Documentos e historico nao sao apagados.

## Eventos

- ProcessoArquivado.
