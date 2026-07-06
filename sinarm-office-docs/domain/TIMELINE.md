# Timeline

## Proposito

Representar a linha do tempo de clientes, processos e documentos.

## Exemplo

```text
12/02 - Cliente cadastrado
13/02 - CRAF enviado
13/02 - Documentacao conferida
14/02 - Minuta IA gerada
15/02 - Revisao concluida
16/02 - Protocolado PF
28/02 - Deferido
```

## Eventos Candidatos

- ClienteCadastrado.
- DocumentoRecebido.
- DocumentacaoConferida.
- MinutaGerada.
- RevisaoConcluida.
- ProcessoProtocolado.
- ExigenciaRecebida.
- ExigenciaRespondida.
- ProcessoDeferido.
- ProcessoArquivado.

## Regras Iniciais

- Timeline deve ser append-only.
- Eventos devem ter data, origem e ator quando aplicavel.
- Timeline nao substitui auditoria, mas facilita acompanhamento.
