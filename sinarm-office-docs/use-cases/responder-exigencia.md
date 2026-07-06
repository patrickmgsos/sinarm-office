# Caso De Uso: Responder Exigencia

## Objetivo

Registrar e responder uma exigencia emitida pela Policia Federal.

## Fluxo Principal

1. Usuario registra exigencia.
2. Sistema move processo para etapa de exigencia.
3. Sistema cria prazo e tarefas.
4. Usuario prepara resposta.
5. Usuario revisa documentos.
6. Sistema registra protocolo de resposta.
7. Sistema move processo para etapa posterior permitida.

## Regras

- Exigencia deve ter data e descricao.
- Prazo deve gerar notificacoes.
- Resposta deve gerar auditoria e historico de workflow.
