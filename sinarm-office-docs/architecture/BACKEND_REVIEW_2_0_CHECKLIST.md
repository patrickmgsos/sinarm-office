# Backend Review 2.0 Checklist

## Objetivo

Revisar o codigo do backend antes da criacao do primeiro dominio juridico.

## Escopo

- Estrutura das apps tecnicas.
- Dependencias e imports.
- Mixins.
- Logging.
- Configuracoes.
- Testes.
- Cobertura.
- Performance basica.
- Observabilidade.
- Independencia dos pacotes de dominio.

## Checklist

- Nenhum dominio juridico foi implementado antes do gate.
- `common` permanece sem dependencia de apps de negocio.
- `core` permanece pequeno e sem concentrar responsabilidades indevidas.
- `health` concentra endpoints operacionais.
- Identity, Organization e Audit estao tecnicamente separados.
- Configuration nao possui constantes juridicas hardcoded.
- Notification nao conhece regras de processos juridicos.
- Models tecnicos usam UUID conforme ADR-0017.
- Arquivamento usa mixin opt-in quando aplicavel.
- Auditoria tecnica nao esta espalhada por models de negocio.
- Imports diretos entre dominios sao justificados ou rejeitados.
- Testes unitarios existem por pacote.
- Ruff, Black, Mypy, Pytest e `manage.py check` passam.
- Logging suporta evolucao para request ID, usuario e organizacao.

## Decisao Esperada

Se aprovado, o projeto pode iniciar o primeiro dominio juridico: Customer Domain.

Se reprovado, as correcoes devem ocorrer antes de qualquer `Customer`.
