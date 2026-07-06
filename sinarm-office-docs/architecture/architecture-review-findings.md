# Architecture Review Findings

## F-001: Duplicidade Entre `decisions/` E `adr/`

**Severidade:** Media
**Status:** Resolvido em `docs/architecture-review-fixes`.

`decisions/ADR-0002-modelos-juridicos-versionados.md` duplica decisoes que ja
estao formalizadas em:

- `adr/0005-legal-template-engine.md`
- `adr/0006-document-versioning-required.md`

Tambem ha risco de confusao porque existe `adr/0002-backend-architecture-style.md`.

## F-002: Casos De Uso Numerados E Nao Numerados Coexistem

**Severidade:** Media
**Status:** Resolvido em `docs/architecture-review-fixes`.

`use-cases/` possui arquivos antigos nao numerados e arquivos oficiais UC001 a
UC010. Isso pode gerar duvida sobre qual documento e fonte de verdade.

## F-003: Fluxos Em `flows/`, `workflow/`, `business/` E `domain-storytelling/`

**Severidade:** Baixa

Existem varias camadas descrevendo fluxos. A separacao e valida, mas precisa ser
explicitada para evitar percepcao de duplicidade.

## F-004: Roadmap Com Fase 2 Em 95% E Fase 2.7 Em Andamento

**Severidade:** Baixa

O roadmap informa que Fase 2 esta 95%, mas tambem inclui Domain Storytelling
como item da Fase 2 e declara Fase 2.7 em andamento. A mensagem e correta, mas
pode ser refinada para deixar claro que Fase 2 esta quase completa exceto pelo
storytelling.

## F-005: Novos Dominios Ainda Nao Totalmente Refletidos No ERD

**Severidade:** Alta antes da Fase 3
**Status:** Resolvido em `docs/architecture-review-fixes`.

Knowledge Base, Compliance e Timeline foram adicionados como dominios, mas ainda
precisam ser refletidos no ERD logico/fisico e no mapeamento DDD antes da
modelagem PostgreSQL.

## F-006: Legal Automation Engine Sem Service De Dominio Proprio

**Severidade:** Media
**Status:** Resolvido em `docs/architecture-review-fixes`.

Existe `domain/LEGAL_AUTOMATION_ENGINE.md`, mas em `domain/services/` ainda nao
ha `LegalAutomationEngine.md`. O servico conceitual precisa existir para manter
simetria com a arquitetura.

## F-007: Domain Portfolio E Bounded Contexts Precisam Ser Alinhados

**Severidade:** Media

`architecture/domain-portfolio.md` e `architecture/bounded-contexts.md` sao
compatíveis, mas devem ser revisados juntos para garantir nomenclatura unica
entre dominios e bounded contexts.

## F-008: ADRs 0009 A 0011 Ausentes Na Main Atual

**Severidade:** Alta se a decisao ainda for valida
**Status:** Resolvido em `docs/architecture-review-fixes`.

Na main revisada existem ADRs 0012 a 0016, mas nao aparecem ADRs 0009, 0010 e
0011. Se as decisoes sobre soft delete, auditoria obrigatoria e fluxo
services/repositories continuam aprovadas, elas devem ser restauradas ou
recriadas antes da Fase 3.
