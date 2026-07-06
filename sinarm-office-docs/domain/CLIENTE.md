# Cliente

## Proposito

Representa a pessoa fisica ou juridica atendida pelo escritorio em processos
administrativos relacionados ao SINARM.

## Entidade

Cliente e uma entidade porque possui identidade propria e ciclo de vida
independente dos dados cadastrais.

## Identidade

- `cliente_id`
- documento principal, como CPF ou CNPJ, com validacao e unicidade contextual

## Possiveis Value Objects

- CPF
- CNPJ
- Nome
- Email
- Telefone
- Endereco
- Data de nascimento

## Relacionamentos

- Cliente possui enderecos.
- Cliente possui telefones e emails.
- Cliente pode possuir armas.
- Cliente pode ter varios processos.
- Cliente pode possuir anexos e documentos.

## Regras Iniciais

- Um cliente nao deve ser duplicado pelo mesmo documento principal.
- Dados sensiveis devem ser auditaveis.
- Alteracoes cadastrais relevantes devem registrar autor, data e motivo.
- Cliente arquivado nao deve impedir consulta historica.

## Questoes Em Aberto

- Havera clientes pessoa juridica na primeira versao?
- O cliente pode pertencer a mais de uma empresa/escritorio?
- Como tratar dependentes, representantes ou procuradores?
