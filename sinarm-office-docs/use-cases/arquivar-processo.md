# Caso De Uso: Arquivar Processo

## Objetivo

Encerrar operacionalmente um processo mantendo historico e documentos.

## Fluxo Principal

1. Usuario solicita arquivamento.
2. Sistema valida pendencias impeditivas.
3. Usuario informa motivo.
4. Sistema move processo para etapa arquivada.
5. Sistema registra auditoria.

## Regras

- Processo arquivado deve permanecer consultavel.
- Arquivamento deve exigir motivo.
- Documentos e historico nao devem ser apagados.
