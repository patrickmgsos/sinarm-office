# UC006 - Gerar Documento

## Objetivo

Gerar documento juridico a partir de modelo versionado.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Processo existente.
- Modelo ativo.
- Dados obrigatorios disponiveis.

## Fluxo Principal

1. Usuario escolhe documento a gerar.
2. Sistema seleciona modelo ativo.
3. Sistema resolve variaveis.
4. Sistema aplica regras de negocio do modelo.
5. IA pode sugerir redacao quando habilitada.
6. Sistema gera documento em versao inicial.
7. Sistema registra auditoria.

## Regras De Negocio

- Nenhum texto juridico deve estar fixo no codigo-fonte.
- Documento deve guardar versao do modelo usado.
- IA nao aprova conteudo juridico.

## Eventos

- DocumentoGerado.
- IaExecucaoRegistrada.
