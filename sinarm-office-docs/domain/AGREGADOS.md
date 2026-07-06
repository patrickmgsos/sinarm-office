# Agregados

## Objetivo

Definir os limites transacionais e conceituais do dominio antes da criacao dos
Models Django.

## Agregados Candidatos

### Empresa

Raiz candidata para isolamento organizacional, configuracoes, usuarios,
permissoes e modelos especificos.

### Cliente

Raiz candidata para dados cadastrais, contatos, enderecos e relacionamento com
armas e processos.

### Arma

Raiz candidata para dados tecnicos, documentos proprios, historico e vinculo com
processos.

### Processo

Agregado central do ERP. Coordena cliente, armas, workflow, documentos, anexos,
certidoes, tarefas, prazos, notificacoes e resultado.

### Workflow

Agregado responsavel por definicoes de etapas, transicoes e regras de movimento.
O historico de execucao se vincula ao processo.

### Documento

Agregado responsavel por conteudo, arquivos, versoes, assinaturas, revisoes e
relacao com modelos.

### Modelo

Agregado responsavel por templates juridicos versionados e ativacao de versoes.

### Auditoria

Agregado historico imutavel para eventos relevantes de seguranca e negocio.

## Regras De Desenho

- Agregados nao devem expor colecoes internas sem controle.
- Mudancas de estado devem passar por casos de uso.
- Um agregado nao deve depender de detalhes de persistencia de outro.
- Relacionamentos entre agregados devem preferir identificadores.
- Invariantes criticas devem ser protegidas no dominio e no banco.

## Questoes Em Aberto

- Processo e Documento devem ficar no mesmo limite transacional?
- WorkflowHistorico pertence ao agregado Processo ou ao agregado Workflow?
- Empresa sera obrigatoria desde a primeira versao ou preparada para multi-tenant?
