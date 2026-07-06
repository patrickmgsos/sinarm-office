# IA

## Proposito

Auxiliar usuarios na elaboracao de minutas e revisoes textuais sem tomar
decisoes juridicas.

## Entidades Candidatas

- IaPrompt
- IaExecucao
- IaProvider
- IaRevisaoHumana

## Modelo Conceitual

```text
Prompt
  -> Execucao
    -> Resultado
      -> Documento
        -> Versao
```

## Regras Iniciais

- IA nunca toma decisao juridica.
- Toda saida de IA deve exigir revisao humana antes de uso operacional.
- Prompt, entrada, saida, provedor, modelo e usuario devem ser rastreados.
- Dados sensiveis devem respeitar LGPD e minimizacao.
- Provedor deve ser substituivel sem alterar casos de uso.

## Provedores Candidatos

- OpenAI
- Azure OpenAI
- Gemini
- Claude
- Ollama

## Relacionamentos

- IA pode apoiar geracao de documento.
- IA pode sugerir texto para resposta a exigencia.
- IA pode apoiar revisao, mas nao aprovar.
- Execucoes de IA devem alimentar auditoria.

## Questoes Em Aberto

- Quais dados podem ser enviados a provedores externos?
- Haverá modo offline/local com Ollama?
- Como tratar retencao de prompts e saidas?
