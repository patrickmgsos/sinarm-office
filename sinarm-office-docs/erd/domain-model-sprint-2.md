# Domain Model - Sprint 2

## Organizacao

```text
Organizacao
  -> Usuarios
  -> Clientes
  -> Processos
```

Organizacao prepara o sistema para multiempresa ou multi-tenant no futuro,
mesmo que a primeira versao use apenas uma organizacao.

## Clientes

```text
Cliente
  -> Enderecos
  -> Telefones
  -> Emails
  -> Contatos
```

## Armas

```text
Fabricante
  -> Modelo
  -> Calibre
  -> Especie
  -> Funcionamento
  -> Arma
```

Calibre, Fabricante e Modelo devem ser entidades candidatas para evitar
duplicacao, melhorar filtros e permitir relatorios.

## Processos

```text
Processo
  -> Tipo
  -> Workflow
  -> Etapa Atual
  -> Historico
  -> Anexos
  -> Documentos
  -> Auditoria
```

## Documentos

```text
Documento
  -> Modelo
  -> Versao
  -> Variaveis
  -> IA
  -> Renderizacao
  -> PDF
  -> Assinatura
  -> Historico
```

## ACL

Perfis candidatos:

- Administrador.
- Socio.
- Advogado.
- Despachante.
- Assistente.
- Financeiro.
- Estagiario.
- Somente leitura.

Cada perfil tera permissoes especificas por modulo, acao e contexto.
