# Legal Engine

## Proposito

Legal Engine e o motor juridico do SINARM Office. Ele concentra a automacao
documental juridica sem transformar IA em decisora e sem colocar regras dentro
de templates.

## Responsabilidades

- Resolver modelos juridicos versionados.
- Resolver variaveis como `cliente.nome`, `arma.calibre` e `processo.tipo`.
- Aplicar regras de negocio antes da renderizacao.
- Avaliar condicoes para inclusao ou exclusao de trechos.
- Solicitar assistencia de IA quando habilitada.
- Gerar rascunhos.
- Exigir revisao humana.
- Criar versoes oficiais.
- Renderizar DOCX e PDF.
- Preservar historico completo.

## Fluxo Conceitual

```text
Modelo
  -> Versao
    -> Variaveis
      -> Regras
        -> Condicoes
          -> IA assistiva
            -> Rascunho
              -> Revisao humana
                -> Versao oficial
                  -> DOCX
                    -> PDF
                      -> Assinatura
                        -> Protocolo PF
```

## Regras De Dominio

- Template apenas renderiza.
- Regra juridica fica no dominio.
- IA apenas sugere.
- Usuario humano revisa e aprova.
- Documento oficial nunca substitui versao anterior.
- Cada versao deve ser auditavel.

## Diferenca Para IA

IA e um mecanismo auxiliar do Legal Engine, nao o motor juridico inteiro.

## Diferenca Para Documentos

Documento e o artefato produzido e versionado. Legal Engine e a camada que
coordena regras, modelos, variaveis, IA e renderizacao.
