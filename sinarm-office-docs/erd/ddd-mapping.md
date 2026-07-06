# Mapeamento DDD

## Agregados

| Agregado | Raiz | Observacao |
| --- | --- | --- |
| Organizacao | Organizacao | Limite para multiempresa |
| Cliente | Cliente | Dados cadastrais, contatos e armas |
| Arma | Arma | Bem controlado vinculado ao cliente |
| Processo | Processo | Agregado operacional central |
| Workflow | Workflow | Definicao de etapas e transicoes |
| Documento | Documento | Artefato juridico versionado |
| Modelo | Modelo | Template juridico versionado |
| Auditoria | EventoAuditoria | Historico append-only |

## Services

- WorkflowEngine.
- GeradorDocumentos.
- LegalAutomationEngine.
- ValidadorSINARM.
- MotorIA.
- Notificador.

## Repositories Candidatos

- OrganizacaoRepository.
- ClienteRepository.
- ArmaRepository.
- ProcessoRepository.
- WorkflowRepository.
- DocumentoRepository.
- ModeloRepository.
- AuditoriaRepository.

## Eventos

- ClienteCriado.
- ClienteAtualizado.
- ArmaRegistrada.
- ProcessoCriado.
- ProcessoProtocolado.
- DocumentoGerado.
- DocumentoRevisado.
- WorkflowAlterado.

## Regra De Implementacao Futura

Quando houver regra de negocio, o acesso a Models Django deve ocorrer por
services e repositories, nao por acoplamento direto entre Models.
