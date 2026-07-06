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

## Arquivos

- CLIENTE.md
- ARMA.md
- PROCESSO.md
- DOCUMENTO.md
- WORKFLOW.md
- USUARIO.md
- EMPRESA.md
- AUDITORIA.md
- NOTIFICACAO.md
