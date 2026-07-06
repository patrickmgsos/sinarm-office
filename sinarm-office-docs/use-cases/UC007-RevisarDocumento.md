# UC007 - Revisar Documento

## Objetivo

Revisar documento juridico antes de assinatura, protocolo ou uso operacional.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Documento existente.
- Usuario possui permissao de revisao.

## Fluxo Principal

1. Usuario abre documento.
2. Usuario revisa conteudo.
3. Usuario edita quando necessario.
4. Sistema cria nova versao.
5. Usuario aprova ou devolve para ajustes.
6. Sistema registra auditoria.

## Regras De Negocio

- Saida de IA exige revisao humana.
- Alteracao relevante deve criar versao.
- Documento aprovado deve preservar autor da revisao.

## Eventos

- DocumentoRevisado.
- DocumentoAprovado.
- DocumentoVersionado.
