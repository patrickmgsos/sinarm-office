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

## Estados Operacionais

Entidades juridicamente relevantes devem possuir estado operacional em vez de
exclusao fisica:

- ativo.
- inativo.
- arquivado.
- cancelado.

Quando necessario, usar `deleted_at` apenas como soft delete tecnico.

## Indices Candidatos

- `clientes(organizacao_id, cpf)`.
- `clientes(organizacao_id, cnpj)`.
- `armas(cliente_id)`.
- `armas(numero_serie)`.
- `processos(cliente_id, tipo)`.
- `processos(organizacao_id, tipo_processo_id)`.
- `processos(etapa_atual_id)`.
- `workflow_historico(processo_id, criado_em)`.
- `documentos(processo_id, tipo)`.
- `documento_versoes(documento_id, versao)`.
- `auditoria(alvo_tipo, alvo_id, criado_em)`.

## Restricoes Candidatas

- CPF unico por organizacao quando nao nulo.
- CNPJ unico por organizacao quando nao nulo.
- Numero de serie unico conforme regra aprovada.
- Apenas uma versao ativa de modelo por tipo e organizacao quando aplicavel.
- Auditoria append-only.

## Decisoes Pendentes

- UUID ou BigAutoField.
- Estrategia de criptografia em repouso.
- Particionamento futuro de auditoria.
- Storage de arquivos local, S3 ou equivalente.
