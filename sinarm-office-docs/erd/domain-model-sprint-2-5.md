# Domain Model - Sprint 2.5

## Objetivo

Consolidar o modelo conceitual antes de qualquer `models.py`.

## Organizacao

```text
Organizacao
  -> Usuarios
  -> Clientes
  -> Processos
```

Organizacao prepara o sistema para multiempresa no futuro, ainda que a primeira
versao use apenas uma organizacao.

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

Calibre, Fabricante e Modelo sao entidades candidatas para evitar duplicacao,
melhorar filtros e preparar relatorios.

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

## ACL/RBAC

Perfis candidatos:

- Administrador.
- Socio.
- Advogado.
- Despachante.
- Assistente.
- Financeiro.
- Estagiario.
- Somente leitura.
