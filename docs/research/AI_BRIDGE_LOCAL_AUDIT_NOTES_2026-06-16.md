# AI Bridge Local - Auditoria Inicial

Data: 2026-06-16
Projeto origem: D:\dev\autocode\ai-bridge-local
Projeto destino: D:\dev\autocode\ai-office
Inventário: D:\dev\autocode\ai-office\reports\ai-bridge-local-inventory\20260616_203921

## Objetivo

Comparar o ai-bridge-local com os scripts/delivery da AI Bridge web para decidir qual deve ser a linha oficial de execução local do WS AI Office.

## Hipótese inicial

O ai-bridge-local deve ser tratado como laboratório/accelerator do executor local, enquanto a AI Bridge web/API deve ser tratada como base cloud/API.

## Pontos a verificar

- Formato de envelopes.
- Marcadores locais.
- Rotas run-command e send-chat-message.
- Gateway local e gateway-brain-supervisor.
- Contrato AI_LOCAL_RUN e AI_LOCAL_ERRO.
- Preflight/validator.
- Smokes.
- Políticas de git, commit, rollback e segurança.

## Decisão ainda pendente

Ainda não copiar código. Primeiro comparar inventário do ai-bridge-local com scripts/delivery da AI Bridge web.

Status: EM AUDITORIA.
