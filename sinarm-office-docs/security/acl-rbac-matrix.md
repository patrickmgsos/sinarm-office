# Matriz ACL/RBAC

## Perfis Iniciais

- Administrador.
- Socio.
- Advogado.
- Despachante.
- Assistente.
- Financeiro.
- Estagiario.
- Somente leitura.

## Matriz Inicial

| Acao | Administrador | Socio | Advogado | Despachante | Assistente | Financeiro | Estagiario | Somente leitura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Visualizar cliente | Sim | Sim | Sim | Sim | Sim | Parcial | Parcial | Sim |
| Editar cliente | Sim | Sim | Sim | Sim | Sim | Nao | Parcial | Nao |
| Cadastrar arma | Sim | Sim | Sim | Sim | Sim | Nao | Parcial | Nao |
| Abrir processo | Sim | Sim | Sim | Sim | Parcial | Nao | Nao | Nao |
| Alterar workflow | Sim | Sim | Sim | Parcial | Parcial | Nao | Nao | Nao |
| Gerar documento | Sim | Sim | Sim | Sim | Parcial | Nao | Nao | Nao |
| Revisar documento | Sim | Sim | Sim | Nao | Nao | Nao | Nao | Nao |
| Acessar financeiro | Sim | Sim | Nao | Nao | Nao | Sim | Nao | Nao |
| Editar modelos | Sim | Sim | Parcial | Nao | Nao | Nao | Nao | Nao |
| Exportar dados | Sim | Sim | Parcial | Nao | Nao | Nao | Nao | Nao |

## Observacao

A matriz sera refinada antes da implementacao. Permissoes finais devem considerar
organizacao, contexto e sensibilidade da acao.
