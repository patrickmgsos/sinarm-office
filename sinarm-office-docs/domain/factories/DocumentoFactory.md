# Factory: DocumentoFactory

## Objetivo

Criar documento a partir de modelo versionado.

## Entradas

- Processo.
- Tipo de documento.
- ModeloVersao.
- Usuario solicitante.

## Regras

- Documento nasce como rascunho.
- Documento preserva versao do modelo.
- Documento aguarda revisao humana.
- Emite DocumentoGerado.
