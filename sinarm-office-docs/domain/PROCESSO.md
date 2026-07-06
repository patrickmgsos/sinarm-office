# Processo

## Proposito

Representa o caso administrativo conduzido perante a Policia Federal ou outra
autoridade competente.

## Agregado Candidato

Processo e candidato a agregado central. Ele coordena cliente, armas envolvidas,
workflow, documentos, anexos, tarefas, prazos, exigencias e resultado.

## Identidade

- `processo_id`
- numero interno
- numero de protocolo externo quando existir

## Tipos Candidatos

- Aquisicao
- Renovacao
- Transferencia
- Porte
- Registro
- Recurso
- Resposta a exigencia

## Relacionamentos

- Processo pertence a um cliente.
- Processo pode envolver uma ou mais armas.
- Processo percorre um workflow.
- Processo gera documentos.
- Processo possui movimentacoes, prazos, tarefas e anexos.

## Regras Iniciais

- Processo nao deve depender apenas de um campo `status`.
- Toda mudanca de etapa deve gerar historico.
- Etapas criticas devem exigir usuario, data, motivo e, quando aplicavel,
  documentos associados.
- Processo arquivado deve permanecer consultavel.

## Invariantes Candidatas

- Um processo deve ter cliente.
- Um processo deve ter tipo.
- Um processo deve estar sempre em uma etapa valida do workflow.
- Uma transicao de etapa deve respeitar as transicoes permitidas.

## Questoes Em Aberto

- Um processo pode ter varios protocolos externos?
- Como tratar processos com exigencias multiplas?
- Como modelar indeferimento, recurso e reaproveitamento documental?
