# Value Objects

## Objetivo

Registrar objetos de valor candidatos, evitando strings soltas, variaveis
magicas e validacoes duplicadas.

## Candidatos

### DocumentoPessoal

Representa CPF, CNPJ ou outro documento principal validavel.

### Email

Representa endereco de email normalizado.

### Telefone

Representa telefone com DDD, tipo e normalizacao.

### Endereco

Representa logradouro, numero, complemento, bairro, cidade, UF e CEP.

### NumeroSerieArma

Representa numero de serie de arma com regras de normalizacao.

### Calibre

Representa calibre de arma com descricao e unidade.

### ProtocoloPF

Representa numero, data e origem de protocolo junto a Policia Federal.

### Periodo

Representa intervalo de datas para prazos, vigencias e filtros.

### Versao

Representa versao semantica ou sequencial de documento, modelo ou workflow.

### HashArquivo

Representa checksum para integridade de anexos e documentos.

## Regras

- Value objects devem ser imutaveis.
- Devem validar seu proprio formato.
- Devem evitar comparacoes por texto bruto quando houver semantica de dominio.
- Nao possuem identidade propria.
