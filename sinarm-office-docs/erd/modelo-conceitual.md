# ERD - Modelo Conceitual

## Objetivo

Representar entidades e relacionamentos do dominio sem compromisso ainda com
tipos fisicos, indices ou detalhes de Django.

## Entidades Principais

- Empresa.
- Usuario.
- Cliente.
- Arma.
- Processo.
- Workflow.
- WorkflowEtapa.
- WorkflowTransicao.
- WorkflowHistorico.
- Documento.
- DocumentoModelo.
- DocumentoVersao.
- Anexo.
- Certidao.
- IaPrompt.
- IaExecucao.
- Auditoria.
- Notificacao.
- Tarefa.
- Agenda.
- Financeiro.

## Relacionamentos Conceituais

```mermaid
erDiagram
    EMPRESA ||--o{ USUARIO : possui
    EMPRESA ||--o{ CLIENTE : atende
    CLIENTE ||--o{ ARMA : possui
    CLIENTE ||--o{ PROCESSO : solicita
    ARMA }o--o{ PROCESSO : utilizada_em
    PROCESSO ||--o{ DOCUMENTO : gera
    PROCESSO ||--o{ ANEXO : possui
    PROCESSO ||--o{ WORKFLOW_HISTORICO : percorre
    WORKFLOW ||--o{ WORKFLOW_ETAPA : define
    WORKFLOW ||--o{ WORKFLOW_TRANSICAO : permite
    DOCUMENTO_MODELO ||--o{ DOCUMENTO : origina
    DOCUMENTO ||--o{ DOCUMENTO_VERSAO : versiona
    IA_PROMPT ||--o{ IA_EXECUCAO : executa
    IA_EXECUCAO }o--|| DOCUMENTO : sugere
    USUARIO ||--o{ AUDITORIA : realiza
```
