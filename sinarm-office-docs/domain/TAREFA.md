# Tarefa

## Proposito

Representa atividades operacionais criadas manualmente ou automaticamente pelo
workflow.

## Entidade

Tarefa possui identidade, responsavel, prazo, prioridade, origem e estado.

## Origens Candidatas

- Workflow.
- Exigencia.
- Agenda.
- Documento.
- Financeiro.

## Regras Iniciais

- Transicoes de workflow podem criar tarefas.
- Tarefa pode ter responsavel e prazo.
- Conclusao deve registrar usuario e data.
- Tarefas vencidas devem gerar notificacoes.

## Questoes Em Aberto

- Havera filas por equipe?
- Como tratar delegacao e transferencia de tarefa?
- Tarefas podem bloquear transicoes de workflow?
