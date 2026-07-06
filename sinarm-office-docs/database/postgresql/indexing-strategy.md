# Indexing Strategy

## Principios

- Indexar chaves estrangeiras usadas em joins frequentes.
- Indexar campos de busca operacional.
- Evitar indices prematuros em colunas de baixa seletividade.
- Nunca criar indice "just in case"; todo indice precisa de consulta esperada,
  justificativa e criterio de revisao.
- Usar indices compostos para consultas por organizacao e status.
- Revisar indices apos queries reais.

## Indices Prioritarios

- `customers(organization_id, cpf)`.
- `customers(organization_id, cnpj)`.
- `firearms(customer_id)`.
- `firearms(serial_number)`.
- `cases(organization_id, case_type, status)`.
- `cases(customer_id)`.
- `workflow_history(case_id, changed_at)`.
- `documents(case_id, document_type, status)`.
- `document_versions(document_id, version)`.
- `audit_events(entity_type, entity_id)`.
- `audit_events(actor_id, occurred_at)`.
- `notifications(recipient_id, status)`.
- `timelines(case_id, occurred_at)`.
- `compliance_checks(case_id, status)`.
- `knowledge_items(item_type, status, effective_from)`.
- `integration_logs(endpoint_id, occurred_at)`.
- `integration_jobs(status, scheduled_at)`.

## Indices Parciais Candidatos

- CPF unico por organizacao quando `cpf is not null`.
- CNPJ unico por organizacao quando `cnpj is not null`.
- Uma versao ativa de modelo quando `status = 'active'`.

## Revisao

Antes da implementacao, cada indice deve ser vinculado a uma consulta esperada.

## Justificativa Obrigatoria

| Indice | Consulta esperada | Motivo | Momento de revisao |
| --- | --- | --- | --- |
| `customers(organization_id, cpf)` | Buscar cliente por CPF dentro da organizacao | Identificacao frequente e unicidade parcial | Revisar apos queries reais de cadastro |
| `cases(organization_id, case_type, status)` | Listar processos por tipo e situacao | Dashboard e operacao diaria | Revisar apos primeira tela de processos |
| `workflow_history(case_id, changed_at)` | Montar historico do processo | Linha do tempo operacional | Revisar apos volume real de transicoes |
| `documents(case_id, document_type, status)` | Listar documentos do processo | Consulta recorrente no dossie | Revisar apos modulo documental |
| `audit_events(entity_type, entity_id)` | Auditar entidade especifica | Rastreabilidade juridica | Revisar apos trilha de auditoria |

Novos indices so entram no modelo fisico quando esta tabela for preenchida.
