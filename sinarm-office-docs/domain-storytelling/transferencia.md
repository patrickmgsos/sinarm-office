# Domain Storytelling: Transferencia

## Narrativa

```text
Cliente solicita transferencia
  -> Usuario identifica arma
  -> Usuario identifica parte destino
  -> Sistema confere documentos das partes
  -> Sistema preserva titularidade atual
  -> Legal Automation Engine gera checklist
  -> Legal Automation Engine gera documentos
  -> Advogado revisa
  -> Partes assinam
  -> Processo e protocolado
  -> PF analisa
  -> Transferencia e deferida
  -> Historico de titularidade e atualizado
  -> Processo e arquivado
```

## Comandos

- AbrirProcessoTransferencia.
- IdentificarArma.
- IdentificarParteDestino.
- ConferirDocumentosTransferencia.
- GerarChecklistTransferencia.
- GerarDocumentosTransferencia.
- RegistrarAssinaturas.
- ProtocolarProcesso.
- AtualizarTitularidade.
- ArquivarProcesso.

## Eventos

- ProcessoTransferenciaCriado.
- ArmaIdentificada.
- ParteDestinoIdentificada.
- DocumentacaoConferida.
- DocumentoGerado.
- DocumentoRevisado.
- DocumentoAssinado.
- ProcessoProtocolado.
- TransferenciaDeferida.
- TitularidadeAtualizada.
- ProcessoArquivado.

## Pontos De Atencao

- Arma nao deve ser duplicada.
- Historico de titularidade deve ser preservado.
- Transferencia deve ser totalmente auditavel.
