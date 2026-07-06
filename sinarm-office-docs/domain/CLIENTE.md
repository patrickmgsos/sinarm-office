# Cliente

## Descricao

Cliente representa a pessoa fisica ou juridica atendida pelo escritorio em
processos administrativos perante a Policia Federal e demais orgaos
relacionados ao SINARM.

Cliente nao e apenas um cadastro. Ele e a raiz de relacionamento para armas,
processos, documentos, anexos, historico, prazos e auditoria.

## Responsabilidades

- Manter dados cadastrais.
- Centralizar contatos e enderecos.
- Possuir armas.
- Possuir processos.
- Possuir documentos e anexos.
- Preservar historico juridico e operacional.
- Permitir rastreabilidade de alteracoes sensiveis.

## Tipo DDD

Entidade e agregado candidato.

Cliente possui identidade propria e ciclo de vida independente dos seus dados
cadastrais. Mudancas em nome, endereco, email ou telefone nao alteram sua
identidade.

## Identidade

- `cliente_id`.
- CPF para pessoa fisica.
- CNPJ para pessoa juridica.

## Atributos Candidatos

- Tipo de pessoa: fisica ou juridica.
- Nome completo ou razao social.
- Nome social ou nome fantasia.
- CPF.
- CNPJ.
- RG ou documento equivalente.
- Data de nascimento ou constituicao.
- Profissao.
- Estado civil.
- Nacionalidade.
- Observacoes internas.
- Status operacional: ativo, inativo, arquivado.
- Data de cadastro.
- Data da ultima atualizacao.

## Value Objects Candidatos

- CPF.
- CNPJ.
- Email.
- Telefone.
- Endereco.
- CEP.
- Nome.
- DocumentoPessoal.

## Documentos Obrigatorios Candidatos

A obrigatoriedade final depende do tipo de processo, mas o cliente pode manter
um dossie base com:

- Documento de identificacao.
- CPF ou CNPJ.
- Comprovante de residencia.
- Certidoes.
- Comprovantes de capacidade tecnica quando aplicavel.
- Comprovantes de aptidao psicologica quando aplicavel.
- Procuracao quando houver representante.

## Relacionamentos

- 1 Cliente possui N Armas.
- 1 Cliente possui N Processos.
- 1 Cliente possui N Documentos.
- 1 Cliente possui N Anexos.
- 1 Cliente possui N Enderecos.
- 1 Cliente possui N Telefones.
- 1 Cliente possui N Emails.

## Regra Estrutural Importante

Arma pertence ao Cliente, nao ao Processo.

O Processo apenas utiliza uma ou mais armas do cliente. Essa decisao preserva o
historico de renovacoes, transferencias e novos procedimentos envolvendo a mesma
arma ao longo dos anos.

## Regras De Negocio

- CPF deve ser unico por empresa quando pessoa fisica.
- CNPJ deve ser unico por empresa quando pessoa juridica.
- Telefone principal e obrigatorio.
- Email pode ser opcional.
- Cliente com processo vinculado nao deve ser excluido fisicamente.
- Cliente arquivado deve permanecer consultavel.
- Alteracoes em dados sensiveis devem gerar auditoria.
- Duplicidade suspeita deve ser sinalizada antes da gravacao.

## Validacoes

- CPF valido quando informado.
- CNPJ valido quando informado.
- Pelo menos um documento principal deve existir.
- Telefone principal deve possuir DDD.
- Email deve ter formato valido quando informado.
- CEP deve ter formato valido quando informado.
- Tipo de pessoa deve ser coerente com CPF ou CNPJ.

## Eventos De Dominio Candidatos

- ClienteCadastrado.
- ClienteAtualizado.
- ClienteArquivado.
- ClienteReativado.
- DocumentoClienteAnexado.
- ContatoClienteAtualizado.
- DuplicidadeClienteDetectada.

## Invariantes

- Um cliente deve pertencer a uma empresa quando houver multiempresa.
- Um cliente deve possuir tipo de pessoa.
- Um cliente ativo deve possuir documento principal valido.
- Um cliente com processos nao pode ser removido fisicamente.

## Questoes Em Aberto

- Pessoa juridica entra na primeira versao funcional?
- Cliente pode pertencer a mais de uma empresa?
- Como modelar procuradores, representantes e despachantes externos?
