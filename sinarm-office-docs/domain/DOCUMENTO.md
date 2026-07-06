# Documento

## Proposito

Representa documentos gerados, importados, revisados ou anexados ao processo.

## Entidade

Documento e uma entidade porque possui identidade, versoes, origem, status de
revisao e relacao com processo, cliente e usuario.

## Identidade

- `documento_id`
- codigo interno
- hash ou checksum do arquivo quando aplicavel

## Tipos Candidatos

- Efetiva necessidade
- Procuracao
- Autorizacao
- Requerimento
- Recurso
- Certidao
- Anexo
- PDF final
- DOCX editavel

## Relacionamentos

- Documento pode pertencer a cliente, arma ou processo.
- Documento pode derivar de um modelo.
- Documento pode possuir varias versoes.
- Documento pode possuir assinaturas.
- Documento pode ter sido auxiliado por IA, sempre com revisao humana.

## Regras Iniciais

- Documento juridico gerado por IA deve exigir revisao humana.
- Documento final deve preservar versao do modelo usado.
- Alteracoes em documentos sensiveis devem gerar versao.
- Documento excluido logicamente deve preservar trilha de auditoria.
- Documento pode ser gerado, editado, revisado, assinado e arquivado.
- Documento nao e apenas PDF; ele e um artefato juridico versionado.

## Time Machine

Cada versao deve registrar:

- Versao.
- Autor.
- Data.
- Motivo.
- Conteudo ou referencia ao arquivo.
- Diferencas quando possivel.

## Questoes Em Aberto

- O conteudo textual ficara no banco, em arquivo, ou ambos?
- Como comparar versoes DOCX de forma confiavel?
- Quais documentos exigem assinatura?
