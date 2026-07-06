# ADR 0021: Nomenclatura Tecnica Em Ingles

## Status

Aceita

## Decisao

Usar ingles tecnico para nomes de tabelas, colunas, constraints, indices,
servicos internos e contratos tecnicos.

Exemplos:

- `customers`.
- `firearms`.
- `cases`.
- `workflows`.
- `workflow_steps`.
- `document_versions`.
- `knowledge_items`.
- `compliance_checks`.

A interface do usuario permanece em portugues.

## Motivo

Ingles tecnico facilita integracoes, padroniza nomenclatura com bibliotecas,
reduz ambiguidade tecnica e melhora consistencia para eventuais colaboradores e
futuras APIs.

## Consequencias

- Documentacao de negocio pode usar portugues.
- Artefatos tecnicos devem usar ingles.
- Glossarios devem mapear termo juridico em portugues para termo tecnico em
  ingles quando necessario.
