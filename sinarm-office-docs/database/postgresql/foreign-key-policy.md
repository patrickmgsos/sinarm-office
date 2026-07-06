# Foreign Key Policy

## Objetivo

Definir politica conceitual de `ON DELETE` e `ON UPDATE` antes de migrations.

## Principios

- Entidades juridicamente relevantes usam `ON DELETE RESTRICT`.
- Historicos e auditorias devem preservar contexto.
- Associacoes puramente tecnicas podem usar `ON DELETE CASCADE`.
- `ON UPDATE` deve ser `RESTRICT` ou `NO ACTION`, pois UUIDs nao devem mudar.

## Politicas Candidatas

| Relacionamento | ON DELETE | ON UPDATE | Justificativa |
| --- | --- | --- | --- |
| organizations -> customers | RESTRICT | RESTRICT | Organizacao com clientes nao deve ser removida |
| organizations -> users | RESTRICT | RESTRICT | Usuarios preservam autoria |
| customers -> firearms | RESTRICT | RESTRICT | Armas dependem de cliente e preservam historico |
| customers -> cases | RESTRICT | RESTRICT | Processo juridico preserva cliente |
| firearms -> case_firearms | CASCADE | RESTRICT | Associacao pode sumir se a linha associativa for removida tecnicamente |
| cases -> case_firearms | CASCADE | RESTRICT | Associacao pertence ao processo |
| cases -> documents | RESTRICT | RESTRICT | Documento juridico preserva processo |
| cases -> workflow_history | RESTRICT | RESTRICT | Historico nao deve desaparecer |
| workflows -> workflow_steps | RESTRICT | RESTRICT | Workflow publicado deve ser versionado, nao removido |
| workflow_steps -> workflow_history | RESTRICT | RESTRICT | Historico precisa da etapa original |
| documents -> document_versions | RESTRICT | RESTRICT | Versoes preservam Time Machine |
| document_versions -> signatures | RESTRICT | RESTRICT | Assinatura aponta para versao especifica |
| document_templates -> document_template_versions | RESTRICT | RESTRICT | Modelos versionados nao devem perder versoes |
| audit_event_types -> audit_events | RESTRICT | RESTRICT | Tipo de evento usado nao deve ser removido |
| audit_sessions -> audit_events | SET NULL | RESTRICT | Evento permanece mesmo sem sessao disponivel |
| knowledge_sources -> knowledge_items | RESTRICT | RESTRICT | Item deve preservar fonte |
| compliance_checks -> findings | RESTRICT | RESTRICT | Achados preservam verificacao |

## Revisao Obrigatoria

Toda FK final deve declarar explicitamente `ON DELETE` e `ON UPDATE` no modelo
fisico antes de virar migration.
