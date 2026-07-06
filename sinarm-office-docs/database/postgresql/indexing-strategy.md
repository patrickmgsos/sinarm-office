# Indexing Strategy

## Principios

- Indexar chaves estrangeiras usadas em joins frequentes.
- Indexar campos de busca operacional.
- Evitar indices prematuros em colunas de baixa seletividade.
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
- `timeline_events(case_id, occurred_at)`.
- `compliance_checks(case_id, status)`.
- `knowledge_items(item_type, status, effective_from)`.

## Indices Parciais Candidatos

- CPF unico por organizacao quando `cpf is not null`.
- CNPJ unico por organizacao quando `cnpj is not null`.
- Uma versao ativa de modelo quando `status = 'active'`.

## Revisao

Antes da implementacao, cada indice deve ser vinculado a uma consulta esperada.
