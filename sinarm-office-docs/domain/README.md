# Dominio

Este diretorio registra a modelagem DDD do SINARM Office antes da criacao dos
Models Django.

## Regra De Governanca

Nenhum Model Django de negocio deve ser criado antes da aprovacao dos documentos
de dominio, casos de uso, fluxos, diagramas e modelo de banco.

## Contextos Principais

- Clientes
- Armas
- Processos
- Documentos
- Workflows
- Modelos
- Auditoria
- IA
- Notificacoes
- Empresas e Usuarios
- Agenda e Tarefas
- Financeiro
- Configuracoes

## Diferenciais Do Produto

### Workflow Engine

Processos nao devem ficar apenas em um status generico. Eles devem percorrer
etapas configuraveis, com transicoes, historico, tarefas, notificacoes e
auditoria.

### Time Machine

Alteracoes relevantes devem gerar versoes historicas consultaveis. Documentos,
modelos e processos sensiveis devem permitir rastrear quem alterou, quando, por
que e qual foi a diferenca.

### Motor De Templates

Textos juridicos nao devem ficar fixos no codigo. Modelos devem ser versionados
e armazenados no banco, permitindo ativar novas versoes sem deploy.

### Legal Automation Engine

Camada de dominio responsavel por modelos, variaveis, regras, condicoes,
assistencia por IA, renderizacao DOCX/PDF, checklists, validacoes, tarefas,
versoes e rastreabilidade juridica. Ela nao e apenas IA e nao e apenas gerador
de documentos.

### Rastreabilidade Total

Toda etapa juridicamente relevante deve ser preservada: modelo, versao, IA,
revisao humana, assinatura, PDF, protocolo, resposta e arquivamento.

## Arquivos

- AGREGADOS.md
- VALUE_OBJECTS.md
- CLIENTE.md
- ARMA.md
- PROCESSO.md
- DOCUMENTO.md
- WORKFLOW.md
- MODELO.md
- IA.md
- LEGAL_AUTOMATION_ENGINE.md
- USUARIO.md
- EMPRESA.md
- AUDITORIA.md
- NOTIFICACAO.md
- ANEXO.md
- CERTIDAO.md
- AGENDA.md
- TAREFA.md
- FINANCEIRO.md
- CONFIGURACAO.md
- PERMISSAO.md
- KNOWLEDGE_BASE.md
- COMPLIANCE.md
- TIMELINE.md

## Subdiretorios

- events/
- services/
- policies/
- factories/
- specifications/
