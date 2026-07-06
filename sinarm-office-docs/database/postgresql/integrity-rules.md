# Integrity Rules

## Regras Gerais

- Toda chave estrangeira critica deve ser explicita.
- Tabelas juridicas nao devem usar exclusao fisica como fluxo comum.
- Eventos historicos devem ser append-only.
- Versoes de documentos e modelos nunca devem ser sobrescritas.
- Workflow em uso deve ser versionado, nao editado em linha.

## Regras Por Dominio

### Customer

- CPF unico por organizacao quando informado.
- CNPJ unico por organizacao quando informado.
- Cliente com processo nao pode ser apagado fisicamente.

### Firearms

- Arma pertence ao cliente.
- Processo usa arma por tabela associativa.
- Transferencia preserva historico.

### Case Management

- Processo possui cliente.
- Processo possui workflow.
- Processo possui etapa atual valida.
- Transicao gera historico.

### Document

- Documento preserva modelo e versao usados.
- Documento oficial exige revisao humana.
- Documento assinado aponta para versao.

### Legal Automation

- IA gera rascunho.
- Automacao registra entrada e saida.
- Revisao humana aprova ou rejeita.

### Compliance

- Verificacao gera achados.
- Achados possuem severidade e status.

### Knowledge

- Item de conhecimento preserva fonte.
- Vigencia deve ser validavel.
