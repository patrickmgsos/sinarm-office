# Processo Rules

## Regras Funcionais

- Processo deve possuir um Cliente.
- Processo deve possuir tipo.
- Processo pode possuir varias Armas.
- Armas do processo devem pertencer ao Cliente do processo.
- Processo possui exatamente um Workflow ativo.
- Processo deve possuir etapa atual valida.
- Processo nao pode avancar sem transicao valida.
- Processo nao pode ser arquivado com exigencia pendente.
- Processo arquivado e somente leitura.
- Processo protocolado deve possuir data de protocolo.
- Toda mudanca relevante deve gerar evento de auditoria.
