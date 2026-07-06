# Workflow - Renovacao

```mermaid
stateDiagram-v2
    [*] --> ClienteSelecionado
    ClienteSelecionado --> ArmasSelecionadas
    ArmasSelecionadas --> DocumentacaoPendente
    DocumentacaoPendente --> Conferencia
    Conferencia --> DocumentosGerados
    DocumentosGerados --> RevisaoHumana
    RevisaoHumana --> Assinatura
    Assinatura --> ProtocoloPF
    ProtocoloPF --> EmAnalise
    EmAnalise --> Exigencia
    Exigencia --> RespostaExigencia
    RespostaExigencia --> EmAnalise
    EmAnalise --> Deferido
    Deferido --> Arquivado
    Arquivado --> [*]
```
