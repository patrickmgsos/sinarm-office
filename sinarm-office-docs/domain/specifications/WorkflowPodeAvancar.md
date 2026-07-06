# Specification: WorkflowPodeAvancar

## Pergunta

Processo pode avancar para a proxima etapa?

## Regra Inicial

Pode avancar apenas se existir transicao valida e as pendencias obrigatorias da
etapa atual estiverem satisfeitas.

## Condicoes Candidatas

- Transicao existe.
- Usuario tem permissao.
- Pendencias foram resolvidas.
- Justificativa foi informada quando exigida.
