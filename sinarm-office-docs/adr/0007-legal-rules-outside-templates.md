# ADR 0007: Regras Juridicas Fora Dos Templates

## Status

Aceita

## Decisao

Nenhuma regra juridica ficara embutida diretamente no template.

Templates apenas renderizam conteudo. Regras juridicas pertencem ao dominio e
devem ser avaliadas antes da renderizacao.

## Motivo

Colocar regra em template mistura apresentacao com negocio, dificulta testes,
auditoria, manutencao e reaproveitamento.

## Consequencias

- Legal Automation Engine deve resolver regras antes de renderizar.
- Templates devem receber dados e blocos ja decididos pelo dominio.
- Mudancas juridicas ficam testaveis e auditaveis.
