# Configuracao

## Proposito

Representar parametros do sistema, preferencias de empresa, chaves de API e
ajustes operacionais.

## Entidades Candidatas

- Parametro
- ConfiguracaoEmpresa
- ApiKey

## Regras Iniciais

- Configuracoes sensiveis devem ser protegidas.
- Segredos nao devem ser expostos em logs ou auditoria detalhada.
- Alteracoes em configuracoes criticas devem gerar auditoria.
- Configuracoes que afetam documentos ou workflow devem ser versionaveis.

## Questoes Em Aberto

- Quais configuracoes ficam no banco e quais ficam em ambiente?
- Havera configuracoes globais administradas pelo produto?
- Como rotacionar chaves de API?
