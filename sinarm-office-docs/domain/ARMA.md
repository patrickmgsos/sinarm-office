# Arma

## Proposito

Representa uma arma vinculada ao cliente e utilizada em processos de aquisicao,
renovacao, transferencia, apostilamento ou outros procedimentos SINARM.

## Entidade

Arma e uma entidade porque possui identidade propria, historico e atributos
tecnicos que podem ser usados em diferentes processos.

## Identidade

- `arma_id`
- numero de serie
- registro ou CRAF quando existente

## Possiveis Value Objects

- Numero de serie
- Calibre
- Fabricante
- Modelo
- Tipo de arma
- Data de validade do CRAF

## Relacionamentos

- Arma pertence a um cliente atual.
- Arma pode participar de varios processos ao longo do tempo.
- Arma pode possuir anexos, CRAF, fotos e historico documental.

## Regras Iniciais

- Numero de serie deve ser controlado para evitar duplicidade indevida.
- Validade documental deve alimentar alertas e agenda.
- Historico de proprietario deve ser preservado quando houver transferencia.

## Questoes Em Aberto

- Como modelar arma sem CRAF no momento do cadastro?
- Havera controle de acessorios, apostilamentos ou guias?
- Quais campos sao obrigatorios por tipo de processo?
