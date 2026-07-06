# Naming Conventions

## Regra Principal

Nomes tecnicos usam ingles.

## Tabelas

- Plural.
- Snake case.
- Nome orientado a dominio.

Exemplos:

- `customers`.
- `firearms`.
- `cases`.
- `workflows`.
- `workflow_steps`.
- `document_versions`.

## Colunas

- Singular quando referencia um atributo.
- Sufixo `_id` para FK.
- Timestamps com `_at`.
- Datas puras com `_date` quando nao houver hora.

## Indices

Formato sugerido:

```text
ix_<table>_<columns>
ux_<table>_<columns>
```

## Constraints

Formato sugerido:

```text
ck_<table>_<rule>
fk_<table>_<referenced_table>
```

## Interface

Interface, manuais e textos do usuario permanecem em portugues.
