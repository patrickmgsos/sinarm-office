# ERD - Modelo Conceitual

## Objetivo

Representar entidades e relacionamentos do dominio sem compromisso ainda com
tipos fisicos, indices ou detalhes de Django.

## Entidades Principais

- Organizacao.
- Usuario.
- Perfil.
- Permissao.
- Cliente.
- Endereco.
- Telefone.
- Email.
- Contato.
- Arma.
- Fabricante.
- ModeloArma.
- Calibre.
- EspecieArma.
- FuncionamentoArma.
- Processo.
- TipoProcesso.
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
    ORGANIZACAO ||--o{ USUARIO : possui
    ORGANIZACAO ||--o{ CLIENTE : atende
    ORGANIZACAO ||--o{ PROCESSO : gerencia
    USUARIO }o--o{ PERFIL : possui
    PERFIL }o--o{ PERMISSAO : concede
    CLIENTE ||--o{ ARMA : possui
    CLIENTE ||--o{ ENDERECO : possui
    CLIENTE ||--o{ TELEFONE : possui
    CLIENTE ||--o{ EMAIL : possui
    CLIENTE ||--o{ CONTATO : possui
    CLIENTE ||--o{ PROCESSO : solicita
    FABRICANTE ||--o{ MODELO_ARMA : fabrica
    MODELO_ARMA ||--o{ ARMA : classifica
    CALIBRE ||--o{ ARMA : define
    ESPECIE_ARMA ||--o{ ARMA : define
    FUNCIONAMENTO_ARMA ||--o{ ARMA : define
    ARMA }o--o{ PROCESSO : utilizada_em
    TIPO_PROCESSO ||--o{ PROCESSO : classifica
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
