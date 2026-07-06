# ADR-0002 - Modelos Juridicos Versionados Fora Do Codigo

## Status

Aceita

## Decisao

Nenhum documento juridico ficara armazenado como texto fixo no codigo-fonte.

Todos os modelos juridicos serao persistidos no banco de dados, versionados e
administraveis pelo sistema.

## Por Que

Textos juridicos mudam com frequencia por estrategia, entendimento interno,
alteracao de procedimento ou exigencia de orgao publico. Se o texto ficar no
codigo, qualquer ajuste exige alteracao tecnica, deploy e risco operacional.

## Consequencias Positivas

- Alterar modelo sem modificar Python.
- Versionar efetivas necessidades, procuracoes e requerimentos.
- Auditar quem alterou o texto, quando e por que.
- Preservar a versao usada em cada documento gerado.
- Permitir aprovacao humana antes de ativar modelos.

## Consequencias Negativas

- Exige motor de templates robusto.
- Exige controle de permissao para edicao.
- Exige validacao de variaveis e regras.
- Aumenta responsabilidade de auditoria.

## Alternativa Rejeitada

Guardar textos juridicos em arquivos Python, templates estaticos ou constantes
do sistema.

Essa alternativa foi rejeitada porque torna o sistema rigido e dependente de
deploy para ajustes juridicos.
