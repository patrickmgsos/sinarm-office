# ADR 0009: Nao Apagar Registros Do Banco

## Status

Aceita

## Decisao

Nada juridicamente ou operacionalmente relevante sera apagado fisicamente do
banco de dados.

Entidades deverao possuir estado operacional, como:

- Ativo.
- Inativo.
- Arquivado.
- Cancelado.

Quando necessario, sera usado mecanismo de soft delete.

## Motivo

Em um sistema juridico, preservar historico costuma ser mais seguro do que
excluir registros definitivamente. Clientes, processos, documentos, anexos,
eventos e auditorias podem ser necessarios para defesa, revisao, rastreabilidade
ou cumprimento legal.

## Consequencias

- Consultas devem filtrar registros ativos quando apropriado.
- Dados arquivados permanecem consultaveis por usuarios autorizados.
- Exclusao fisica fica restrita a casos tecnicos ou obrigacoes legais
  especificas.
- Modelagem deve prever estados e datas de arquivamento/cancelamento.
