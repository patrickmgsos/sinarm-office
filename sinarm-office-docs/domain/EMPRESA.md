# Empresa

## Proposito

Representa o escritorio ou organizacao que utiliza o SINARM Office.

## Entidade

Empresa e entidade porque delimita usuarios, clientes, configuracoes, modelos,
parametros e possivelmente dados financeiros.

## Relacionamentos

- Empresa possui usuarios.
- Empresa pode possuir clientes.
- Empresa pode possuir modelos documentais.
- Empresa possui parametros e configuracoes.

## Regras Iniciais

- Dados de empresas diferentes nao devem se misturar.
- Configuracoes devem ser versionaveis quando afetarem documentos ou workflow.
- Modelos podem ser globais ou especificos da empresa.

## Questoes Em Aberto

- Produto sera single-tenant no inicio e multi-tenant no futuro?
- Clientes podem migrar entre empresas?
- Quais configuracoes sao globais e quais sao por empresa?
