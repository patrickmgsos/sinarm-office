# ADR 0008: IA Gera Rascunhos E Exige Revisao Humana

## Status

Aceita

## Decisao

A IA jamais gravara documentos oficiais diretamente.

O fluxo obrigatorio sera:

```text
IA
  -> Rascunho
    -> Usuario revisa
      -> Salvar versao
        -> Documento oficial
```

## Motivo

A IA e assistiva e nao toma decisoes juridicas. O controle humano preserva
responsabilidade profissional, qualidade juridica e rastreabilidade.

## Consequencias

- Toda execucao de IA deve ser registrada.
- Documento com participacao de IA deve indicar revisao humana.
- Documento oficial so nasce apos aprovacao humana.
