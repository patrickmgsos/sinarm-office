# ERD - Modelo Fisico

## Objetivo

Registrar diretrizes fisicas futuras para PostgreSQL. Este documento ainda nao e
uma migration.

## Padroes Candidatos

- Chaves primarias: `bigint` ou `uuid`, decisao pendente.
- Timestamps: `created_at`, `updated_at`.
- Auditoria tecnica: `created_by_id`, `updated_by_id` quando aplicavel.
- Exclusao logica: `deleted_at` para entidades sensiveis.
- Campos JSONB apenas quando houver real variabilidade.
- Indices por chaves estrangeiras e filtros frequentes.

## Indices Candidatos

- `clientes(empresa_id, cpf)`.
- `clientes(empresa_id, cnpj)`.
- `armas(cliente_id)`.
- `armas(numero_serie)`.
- `processos(cliente_id, tipo)`.
- `processos(etapa_atual_id)`.
- `workflow_historico(processo_id, criado_em)`.
- `documentos(processo_id, tipo)`.
- `documento_versoes(documento_id, versao)`.
- `auditoria(alvo_tipo, alvo_id, criado_em)`.

## Restricoes Candidatas

- CPF unico por empresa quando nao nulo.
- CNPJ unico por empresa quando nao nulo.
- Numero de serie unico conforme regra aprovada.
- Apenas uma versao ativa de modelo por tipo e empresa quando aplicavel.

## Decisoes Pendentes

- UUID ou BigAutoField.
- Estrategia de criptografia em repouso.
- Particionamento futuro de auditoria.
- Storage de arquivos local, S3 ou equivalente.
