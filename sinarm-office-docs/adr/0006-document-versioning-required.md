# ADR 0006: Versionamento Obrigatorio De Documentos Juridicos

## Status

Aceita

## Decisao

Todo documento juridico devera possuir versionamento.

Documentos juridicos oficiais jamais deverao ser substituidos em sobrescrita.
Qualquer alteracao relevante cria uma nova versao.

## Motivo

Documentos juridicos precisam de rastreabilidade, auditoria e possibilidade de
comparacao historica. Sobrescrever conteudo apagaria contexto, autoria e
responsabilidade.

## Consequencias

- Cada versao deve registrar autor, data e motivo.
- Documento oficial deve preservar a versao anterior.
- Comparacao de versoes passa a ser requisito futuro.
- Armazenamento e auditoria ficam mais complexos, mas juridicamente mais fortes.
