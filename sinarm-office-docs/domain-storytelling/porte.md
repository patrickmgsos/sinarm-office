# Domain Storytelling: Porte

## Narrativa

```text
Cliente solicita porte
  -> Usuario coleta justificativa
  -> Sistema cria processo
  -> Cliente envia documentos
  -> Sistema verifica pendencias
  -> Despachante confere
  -> Legal Automation Engine apoia redacao da justificativa
  -> Advogado revisa estrategia e texto
  -> Cliente assina
  -> Processo e protocolado
  -> PF analisa
  -> PF defere, indefere ou exige complemento
  -> Escritorio responde ou recorre
  -> Processo e arquivado
```

## Comandos

- AbrirProcessoPorte.
- RegistrarJustificativa.
- VerificarPendencias.
- ConferirDocumentacao.
- GerarMinutaPorte.
- RevisarDocumento.
- ProtocolarProcesso.
- RegistrarResultado.
- AbrirRecursoQuandoAplicavel.
- ArquivarProcesso.

## Eventos

- ProcessoPorteCriado.
- JustificativaRegistrada.
- PendenciaDetectada.
- DocumentacaoConferida.
- DocumentoGerado.
- DocumentoRevisado.
- ProcessoProtocolado.
- ProcessoDeferido.
- ProcessoIndeferido.
- RecursoAberto.
- ProcessoArquivado.

## Regra Central

IA pode auxiliar a redacao, mas decisao juridica e estrategia permanecem com
usuario humano autorizado.
