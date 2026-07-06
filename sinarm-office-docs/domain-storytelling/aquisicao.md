# Domain Storytelling: Aquisicao

## Narrativa

```text
Cliente procura o escritorio
  -> Atendente cadastra cliente
  -> Cliente envia documentos
  -> Sistema registra anexos
  -> Sistema verifica pendencias
  -> Despachante confere documentacao
  -> Legal Automation Engine gera checklist
  -> Legal Automation Engine gera minuta
  -> Advogado revisa minuta
  -> Cliente assina
  -> Processo e protocolado na PF
  -> PF analisa
  -> PF pode emitir exigencia
  -> Escritorio responde exigencia
  -> PF decide
  -> Processo e deferido ou indeferido
  -> Processo e arquivado
```

## Comandos

- CadastrarCliente.
- AnexarDocumento.
- VerificarPendencias.
- ConferirDocumentacao.
- GerarChecklistAquisicao.
- GerarMinutaAquisicao.
- RevisarDocumento.
- RegistrarAssinatura.
- ProtocolarProcesso.
- RegistrarExigencia.
- ResponderExigencia.
- RegistrarResultado.
- ArquivarProcesso.

## Eventos

- ClienteCadastrado.
- DocumentoAnexado.
- PendenciaDetectada.
- DocumentacaoConferida.
- ChecklistGerado.
- DocumentoGerado.
- DocumentoRevisado.
- DocumentoAssinado.
- ProcessoProtocolado.
- ExigenciaRegistrada.
- ExigenciaRespondida.
- ProcessoDeferido.
- ProcessoIndeferido.
- ProcessoArquivado.

## Entidades Envolvidas

- Cliente.
- Processo.
- Documento.
- Anexo.
- Checklist.
- Workflow.
- Exigencia.
- Protocolo.
- Auditoria.

## Pontos De Auditoria

- Cadastro do cliente.
- Upload de documentos.
- Conferencia documental.
- Geracao de minuta.
- Revisao humana.
- Assinatura.
- Protocolo.
- Resposta a exigencia.
- Resultado.
