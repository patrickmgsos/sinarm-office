# Workflow

## Proposito

Controlar a jornada operacional dos processos SINARM por etapas e transicoes
explicitas.

## Agregado Candidato

Workflow pode ser um agregado proprio, referenciado por Processo. Ele define
etapas, transicoes permitidas, tarefas automaticas, prazos, notificacoes e
gatilhos de auditoria.

## Entidades Candidatas

- Workflow
- WorkflowEtapa
- WorkflowTransicao
- WorkflowHistorico

## Etapas Candidatas

- Cliente cadastrado
- Documentacao pendente
- Documentacao enviada
- Conferencia
- Documentos gerados
- Revisao humana
- Assinatura
- Protocolo na Policia Federal
- Em analise
- Exigencia
- Resposta a exigencia
- Deferido
- Indeferido
- Arquivado

## Regras Iniciais

- Nenhum processo deve mudar de etapa sem transicao valida.
- Toda transicao deve registrar usuario, data e etapa anterior.
- Transicoes podem gerar tarefas, notificacoes e auditoria.
- Fluxos devem ser configuraveis por tipo de processo.
- Exigencias devem permitir retorno para etapas especificas.

## Questoes Em Aberto

- Workflows serao globais ou por empresa?
- Usuarios poderao editar fluxos pela interface?
- Como versionar um workflow em uso?
