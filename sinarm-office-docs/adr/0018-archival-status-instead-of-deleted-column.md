# ADR 0018: Status E Arquivamento Em Vez De Coluna Deleted

## Status

Aceita

## Decisao

Nao padronizar uma coluna booleana `deleted`.

Entidades juridicamente relevantes devem usar estado operacional e campos de
arquivamento quando fizer sentido:

- `status`.
- `archived_at`.
- `archived_by`.

## Motivo

Em dominio juridico, "arquivado", "cancelado", "inativo" e "ativo" possuem
significados de negocio diferentes de exclusao tecnica.

## Consequencias

- Nem toda tabela tera arquivamento.
- Tabelas de catalogo podem usar `is_active`.
- Tabelas juridicas devem preservar historico.
- Exclusao fisica sera excepcional e documentada.
