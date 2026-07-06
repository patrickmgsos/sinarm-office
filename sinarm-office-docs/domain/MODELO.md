# Modelo

## Proposito

Representa templates juridicos usados para gerar documentos como efetiva
necessidade, procuracoes, autorizacoes, requerimentos, recursos e respostas a
exigencias.

## Agregado Candidato

Modelo e agregado proprio, com versoes e status de ativacao.

## Identidade

- `modelo_id`
- nome
- tipo

## Entidades Candidatas

- Modelo
- ModeloVersao

## Possiveis Value Objects

- TipoModelo
- Versao
- ConteudoTemplate
- StatusModelo

## Regras Iniciais

- Textos juridicos nao devem ficar fixos no codigo.
- Apenas uma versao ativa por tipo e contexto deve existir quando a regra exigir.
- Documento gerado deve registrar a versao exata do modelo usado.
- Alteracao de modelo deve gerar nova versao, nao sobrescrever a anterior.
- Modelos podem ser globais ou especificos de empresa.

## Time Machine

Toda versao deve preservar:

- Autor.
- Data.
- Motivo.
- Conteudo.
- Status.
- Data de ativacao e inativacao.

## Questoes Em Aberto

- O template usara sintaxe Jinja, DOCX template ou motor proprio?
- Usuarios poderao editar modelos pela interface?
- Havera aprovacao antes de ativar nova versao?
