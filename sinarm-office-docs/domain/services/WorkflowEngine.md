# Servico De Dominio: WorkflowEngine

## Responsabilidade

Validar e executar transicoes de workflow.

## Entradas

- Processo.
- Etapa atual.
- Etapa desejada.
- Usuario.
- Justificativa quando exigida.

## Saidas

- Historico de workflow.
- Eventos.
- Tarefas ou notificacoes geradas.

## Regras

- Nao avanca sem transicao valida.
- Deve registrar historico.
- Pode bloquear transicoes com pendencias.
