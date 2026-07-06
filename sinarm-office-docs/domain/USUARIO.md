# Usuario

## Proposito

Representa a pessoa autenticada que opera o sistema, revisa documentos, executa
transicoes, aprova conteudos e realiza acoes auditaveis.

## Entidade

Usuario e entidade de seguranca e autoria.

## Relacionamentos

- Usuario pertence a uma empresa.
- Usuario pode pertencer a grupos.
- Usuario possui permissoes.
- Usuario cria, altera, revisa e aprova registros.

## Regras Iniciais

- Acoes sensiveis devem ser auditadas.
- Permissoes devem considerar papel e contexto.
- IA nao substitui revisao humana de usuario autorizado.
- Usuario inativo nao deve executar novas acoes, mas seu historico permanece.

## Questoes Em Aberto

- Havera multiempresa desde a primeira versao?
- Quais perfis iniciais existem?
- Havera assinatura digital ou apenas registro de aprovacao?
