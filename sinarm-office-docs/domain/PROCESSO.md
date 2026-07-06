# Processo

## Descricao

Processo representa o caso administrativo conduzido para um cliente perante a
Policia Federal ou autoridade competente. E o coracao operacional do SINARM
Office.

## Tipo DDD

Agregado central.

Processo coordena cliente, armas utilizadas, workflow, documentos, anexos,
certidoes, tarefas, prazos, auditoria e resultado.

## Identidade

- `processo_id`.
- Numero interno.
- Numero de protocolo externo quando existir.

## Tipos De Processo

- Aquisicao.
- Renovacao.
- Transferencia.
- Porte.
- Recurso.
- Exigencia.

## Responsabilidades

- Registrar o procedimento administrativo.
- Controlar workflow e etapa atual.
- Associar armas utilizadas.
- Controlar documentos e anexos.
- Preservar historico.
- Gerar tarefas e notificacoes.
- Registrar protocolos e resultados.
- Garantir rastreabilidade operacional.

## Atributos Candidatos

- Tipo.
- Cliente.
- Responsavel interno.
- Workflow.
- Etapa atual.
- Data de abertura.
- Data de protocolo.
- Numero de protocolo.
- Resultado.
- Data de encerramento.
- Motivo de arquivamento.
- Observacoes internas.

## Relacionamentos

- 1 Processo pertence a 1 Cliente.
- 1 Processo utiliza N Armas do cliente.
- 1 Processo possui 1 Workflow.
- 1 Processo possui N Documentos.
- 1 Processo possui N Anexos.
- 1 Processo possui N Tarefas.
- 1 Processo possui N Notificacoes.
- 1 Processo possui N eventos de Auditoria.
- 1 Processo possui N registros de WorkflowHistorico.

## Regras De Negocio

- Processo nao deve depender apenas de um campo `status`.
- Processo deve estar sempre em uma etapa valida do workflow.
- Toda transicao deve gerar historico.
- Transicao deve respeitar regras do workflow.
- Processo arquivado permanece consultavel.
- Processo com pendencias criticas nao deve avancar sem justificativa ou regra
  explicita.
- Processo de renovacao deve usar arma ja vinculada ao cliente.
- Processo pode envolver uma ou mais armas quando a regra juridica permitir.

## Validacoes

- Cliente obrigatorio.
- Tipo de processo obrigatorio.
- Responsavel obrigatorio.
- Workflow obrigatorio.
- Etapa inicial obrigatoria.
- Armas obrigatorias quando o tipo de processo exigir.
- Protocolo externo deve ter data quando informado.

## Eventos De Dominio Candidatos

- ProcessoAberto.
- ProcessoWorkflowAlterado.
- ProcessoProtocolado.
- ExigenciaRegistrada.
- ExigenciaRespondida.
- DocumentoGeradoParaProcesso.
- ProcessoDeferido.
- ProcessoIndeferido.
- ProcessoArquivado.

## Invariantes

- Processo sempre possui cliente.
- Processo sempre possui tipo.
- Processo sempre possui etapa atual.
- Etapa atual deve pertencer ao workflow do processo.
- Transicoes devem ser registradas no historico.

## Questoes Em Aberto

- Um processo pode ter mais de um protocolo externo?
- Como modelar recurso vinculado a indeferimento?
- Exigencia e um tipo de processo, uma etapa ou ambos?
