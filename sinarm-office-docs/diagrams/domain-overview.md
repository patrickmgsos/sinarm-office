# Diagrama De Dominio

```mermaid
classDiagram
    Empresa "1" --> "*" Usuario
    Empresa "1" --> "*" Cliente
    Cliente "1" --> "*" Arma
    Cliente "1" --> "*" Processo
    Arma "*" --> "*" Processo
    Processo "1" --> "*" Documento
    Processo "1" --> "*" WorkflowHistorico
    Workflow "1" --> "*" WorkflowEtapa
    Workflow "1" --> "*" WorkflowTransicao
    Documento "1" --> "*" DocumentoVersao
    DocumentoModelo "1" --> "*" Documento
    Usuario "1" --> "*" Auditoria
    Processo "1" --> "*" Notificacao
```
