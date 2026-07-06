# ADR 0010: Alteracoes Importantes Geram Auditoria

## Status

Aceita

## Decisao

Toda alteracao importante devera gerar evento de auditoria.

Exemplos:

- Cliente criado.
- Cliente atualizado.
- Arma cadastrada.
- Documento gerado.
- Documento revisado.
- Workflow alterado.
- Processo protocolado.
- Processo arquivado.

## Motivo

O SINARM Office precisa preservar trilha de responsabilidade, autoria,
temporalidade e contexto das acoes relevantes.

## Consequencias

- Casos de uso devem emitir eventos auditaveis.
- Eventos de dominio podem alimentar auditoria, notificacoes e tarefas.
- Auditoria deve ser append-only.
- Alteracoes sensiveis devem registrar usuario, data, origem e alvo.
