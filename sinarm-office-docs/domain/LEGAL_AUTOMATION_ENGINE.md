# Legal Automation Engine

## Proposito

Legal Automation Engine e o motor de automacao juridica do SINARM Office. Ele
concentra modelos, variaveis, regras, condicoes, IA assistiva, renderizacao,
checklists, validacoes, tarefas e rastreabilidade.

Ele nao e apenas IA, nao e apenas documentos e nao e apenas um gerador de PDF.

## Historico Da Nomenclatura

O conceito nasceu na Sprint 1 com o nome Legal Engine, focado principalmente no
motor juridico para documentos, modelos versionados, variaveis, regras,
assistencia por IA e revisao humana.

Na Sprint 2, o conceito foi ampliado para Legal Automation Engine para refletir
um escopo maior: automacao juridica completa. Ele nao sera apenas um gerador de
documentos. Tambem sera responsavel por checklists, validacoes, tarefas,
exigencias, protocolos e relatorios.

## Responsabilidades

- Resolver modelos juridicos versionados.
- Resolver variaveis como `cliente.nome`, `arma.calibre` e `processo.tipo`.
- Aplicar regras de negocio antes da renderizacao.
- Avaliar condicoes para inclusao ou exclusao de trechos.
- Solicitar assistencia de IA quando habilitada.
- Gerar checklists.
- Validar documentacao.
- Sugerir pendencias.
- Criar tarefas.
- Apoiar respostas a exigencias.
- Montar protocolos.
- Produzir relatorios operacionais.
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

IA e um mecanismo auxiliar do Legal Automation Engine, nao o motor inteiro.

## Diferenca Para Documentos

Documento e um dos artefatos produzidos e versionados. Legal Automation Engine e
a camada que coordena regras, modelos, variaveis, IA, validacoes, tarefas e
renderizacao.
