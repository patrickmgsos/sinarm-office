# Permissao

## Proposito

Definir o controle de acesso do sistema por papel, contexto e acao.

## Entidades Candidatas

- Grupo
- Permissao
- Papel
- PoliticaAcesso

## Regras Iniciais

- Permissoes devem considerar empresa e contexto.
- Acoes sensiveis devem exigir permissao explicita.
- Revisao, aprovacao e exclusao devem ser separadas.
- Auditoria deve registrar acoes negadas quando relevante.

## Acoes Candidatas

- Visualizar cliente.
- Editar cliente.
- Abrir processo.
- Mover etapa de workflow.
- Gerar documento.
- Aprovar documento.
- Editar modelo.
- Acessar financeiro.
- Exportar dados.

## Questoes Em Aberto

- Usaremos RBAC puro ou RBAC com politicas contextuais?
- Perfis serao globais ou por empresa?
- Havera aprovacao em duas etapas para documentos sensiveis?
