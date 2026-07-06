# Domain Storytelling: Renovacao

## Narrativa

```text
Sistema identifica vencimento futuro
  -> Notificacao e gerada
  -> Usuario seleciona cliente
  -> Usuario seleciona arma existente
  -> Sistema verifica validade documental
  -> Cliente envia documentos atualizados
  -> Despachante confere documentacao
  -> Legal Automation Engine gera checklist de renovacao
  -> Legal Automation Engine gera minuta
  -> Advogado revisa
  -> Cliente assina
  -> Processo e protocolado
  -> PF analisa
  -> Exigencia pode ser emitida
  -> Escritorio responde
  -> Renovacao e deferida
  -> Validade da arma/documento e atualizada
  -> Processo e arquivado
```

## Comandos

- GerarAlertaVencimento.
- AbrirProcessoRenovacao.
- SelecionarArmaDoCliente.
- VerificarValidadeDocumental.
- GerarChecklistRenovacao.
- GerarMinutaRenovacao.
- RevisarDocumento.
- ProtocolarProcesso.
- AtualizarValidade.
- ArquivarProcesso.

## Eventos

- VencimentoDetectado.
- NotificacaoGerada.
- ProcessoRenovacaoCriado.
- ArmaSelecionada.
- ValidadeVerificada.
- ChecklistGerado.
- DocumentoGerado.
- DocumentoRevisado.
- ProcessoProtocolado.
- RenovacaoDeferida.
- ValidadeAtualizada.
- ProcessoArquivado.

## Regra Estrutural

Renovacao usa arma existente do cliente. A arma nao e recriada no processo.
