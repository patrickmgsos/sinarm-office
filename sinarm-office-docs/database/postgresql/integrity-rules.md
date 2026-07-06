# Integrity Rules

## Regras Gerais

- Toda chave estrangeira critica deve ser explicita.
- Toda chave estrangeira deve declarar politica de `ON DELETE` e `ON UPDATE`.
- `ON UPDATE` deve ser `RESTRICT` ou `NO ACTION`, pois UUIDs nao devem mudar.
- Tabelas juridicas nao devem usar exclusao fisica como fluxo comum.
- Eventos historicos devem ser append-only.
- Versoes de documentos e modelos nunca devem ser sobrescritas.
- Workflow em uso deve ser versionado, nao editado em linha.
- Catalogos de referencia devem ser inativados, nao removidos, quando ja usados.

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

### Reference Data

- Fabricantes, calibres, modelos de arma, paises, estados, cidades, tipos de
  documento, tipos de processo, tipos de workflow e tipos de status sao dados de
  referencia.
- Dados de referencia usados por entidades juridicas devem ser inativados em vez
  de removidos.
- Dados de referencia globais nao devem depender de uma organizacao especifica,
  salvo quando houver customizacao aprovada.

### Integration

- Credenciais externas nunca devem ser armazenadas em texto puro.
- Chamadas externas devem gerar logs de integracao auditaveis.
- Falhas de integracao devem preservar payload minimo necessario para diagnostico,
  respeitando LGPD e politicas de retencao.

## Politica De FK

A politica detalhada de `ON DELETE` e `ON UPDATE` esta em
`foreign-key-policy.md` e deve ser validada antes de qualquer migration.
