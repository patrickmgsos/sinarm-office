# Architecture Review Actions

## A-001: Consolidar `decisions/`

**Origem:** F-001

Escolher uma das abordagens:

- mover `decisions/ADR-0002-modelos-juridicos-versionados.md` para `adr/` com
  numeracao formal; ou
- marcar `decisions/` como historico/legado e apontar para ADRs oficiais.

## A-002: Declarar UC001-UC010 Como Fonte Oficial

**Origem:** F-002

Atualizar `use-cases/README.md` para declarar UC001-UC010 como fonte oficial.
Arquivos nao numerados devem ser arquivados, renomeados como legado ou
referenciados como rascunhos iniciais.

## A-003: Explicitar Camadas De Fluxo

**Origem:** F-003

Adicionar uma convencao documental:

- `business/`: mundo juridico.
- `domain-storytelling/`: narrativa real, eventos e comandos.
- `workflow/`: etapas e transicoes do sistema.
- `flows/`: rascunhos iniciais ou material legado.

## A-004: Refinar Roadmap Da Fase 2

**Origem:** F-004

Atualizar o roadmap para indicar:

- Fase 2: modelo conceitual em consolidacao.
- Fase 2.7: storytelling em andamento.
- Fase 3: PostgreSQL bloqueada ate conclusao das acoes criticas.

## A-005: Atualizar ERD Para Knowledge Base, Compliance E Timeline

**Origem:** F-005

Antes de modelar PostgreSQL, adicionar ao ERD:

- knowledge_base_items.
- knowledge_base_sources.
- compliance_checks.
- compliance_findings.
- timeline_events.
- retention_policies.

Os nomes finais devem ser aprovados na Fase 3.

## A-006: Criar Service Do Legal Automation Engine

**Origem:** F-006

Adicionar `domain/services/LegalAutomationEngine.md` descrevendo entradas,
saidas, responsabilidades, eventos e invariantes do servico.

## A-007: Alinhar Domain Portfolio E Bounded Contexts

**Origem:** F-007

Revisar `architecture/domain-portfolio.md` e
`architecture/bounded-contexts.md`, escolhendo nomenclatura canonica para:

- Customer Domain.
- Firearms Domain.
- Case Management Domain.
- Document Management Domain.
- Legal Automation Domain.
- Knowledge Base Domain.
- Compliance Domain.
- Core.

## A-008: Restaurar Ou Recriar ADRs 0009 A 0011

**Origem:** F-008

Confirmar se continuam aprovadas as decisoes:

- Nada juridicamente relevante e apagado fisicamente.
- Toda alteracao importante gera auditoria.
- Regras de negocio passam por services/repositories.

Se sim, recriar ADRs formais antes da Fase 3.

## A-009: Gate Para Fase 3

**Origem:** Architecture Review 1.0

Nao iniciar modelagem PostgreSQL ate as acoes A-001, A-004, A-005, A-006 e A-008
serem resolvidas ou formalmente dispensadas.
