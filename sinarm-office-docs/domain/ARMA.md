# Arma

## Descricao

Arma representa o bem controlado vinculado a um cliente. Ela pode ser utilizada
em varios processos ao longo do tempo, como aquisicao, renovacao, transferencia,
apostilamento ou porte.

## Regra Estrutural Essencial

Uma arma pertence ao cliente.

O processo apenas utiliza aquela arma.

```text
Cliente -> Arma -> Processo
```

Nao devemos modelar como:

```text
Processo -> Arma
```

Essa decisao evita duplicidade e preserva o historico quando a mesma arma passar
por varias renovacoes ou procedimentos.

## Tipo DDD

Entidade e agregado candidato.

## Identidade

- `arma_id`.
- Numero de serie.
- Numero de registro ou CRAF quando existente.

## Atributos Candidatos

- Tipo de arma.
- Fabricante.
- Modelo.
- Calibre.
- Numero de serie.
- Numero de registro.
- Numero do CRAF.
- Data de emissao do CRAF.
- Data de validade do CRAF.
- Situacao.
- Observacoes tecnicas.

## Value Objects Candidatos

- NumeroSerieArma.
- Calibre.
- Fabricante.
- ModeloArma.
- RegistroArma.
- ValidadeCRAF.

## Relacionamentos

- 1 Cliente possui N Armas.
- 1 Arma pode ser usada em N Processos.
- 1 Arma possui N Documentos.
- 1 Arma possui N Anexos.
- 1 Arma pode possuir N eventos historicos.

## Regras De Negocio

- Numero de serie deve ser rastreavel.
- Numero de serie nao deve ser duplicado indevidamente.
- Arma pode existir sem processo aberto.
- Arma transferida deve preservar historico de proprietarios.
- Validade do CRAF deve alimentar agenda e notificacoes.
- Arma arquivada nao deve desaparecer do historico.

## Validacoes

- Numero de serie obrigatorio quando conhecido.
- Calibre obrigatorio quando processo exigir.
- Fabricante e modelo devem preferir cadastro controlado.
- Data de validade nao pode ser anterior a data de emissao.
- CRAF vencido deve gerar alerta quando aplicavel.

## Documentos Relacionados

- CRAF.
- Nota fiscal ou comprovante de origem.
- Fotos ou imagens.
- Certificados aplicaveis.
- Guias e comprovantes.

## Eventos De Dominio Candidatos

- ArmaCadastrada.
- ArmaAtualizada.
- ArmaVinculadaAoCliente.
- ArmaUsadaEmProcesso.
- ValidadeCRAFProxima.
- ArmaTransferida.
- ArmaArquivada.

## Questoes Em Aberto

- Como tratar arma sem numero de registro no momento do cadastro?
- Haverá controle de acessorios?
- Quais campos sao obrigatorios por tipo de processo?
