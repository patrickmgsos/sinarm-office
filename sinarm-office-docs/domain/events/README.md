# Eventos De Dominio

Eventos representam fatos relevantes que ja aconteceram no dominio.

No futuro, alguns eventos poderao disparar tarefas assincronas via Celery,
notificacoes, auditoria, atualizacao de agenda ou integracoes.

## Eventos Iniciais

- ClienteCriado.
- ClienteAtualizado.
- ArmaRegistrada.
- ProcessoCriado.
- ProcessoProtocolado.
- DocumentoGerado.
- DocumentoRevisado.
- WorkflowAlterado.
