# Servico De Dominio: GeradorDocumentos

## Responsabilidade

Coordenar a geracao de documentos a partir do Legal Engine.

## Entradas

- Processo.
- Tipo de documento.
- Modelo versionado.
- Usuario solicitante.

## Saidas

- Documento em rascunho.
- Versao inicial.
- Eventos de dominio.

## Regras

- Deve preservar a versao do modelo usado.
- Deve exigir revisao humana antes do documento oficial.
- Nao deve conter regra juridica dentro do template.
