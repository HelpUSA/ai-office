# Próximos Passos

## Micro 1 - Validar documentação

Rodar:

`powershell
Set-Location D:\dev\autocode\ai-office
Get-ChildItem docs -Recurse
`",
    ",
    

Criar:

- config/agents.json
- config/policies.json
- config/tools.json

## Micro 3 - Criar banco SQLite

Criar:

- data/ai_office.db
- tabela agents
- tabela tasks
- tabela task_logs
- tabela approvals
- tabela costs

## Micro 4 - Criar CLI

Comandos desejados:

`powershell
python -m ai_office list-agents
python -m ai_office create-task
python -m ai_office list-tasks
python -m ai_office show-task
`",
    ",
    

Projetos:

- D:\dev\autocode\ai-bridge-local
- D:\dev\ai
- D:\dev\autocode\ai-office

Relatórios esperados:

- reports/AI_BRIDGE_LOCAL_INVENTORY.md
- reports/HELPUS_AI_INVENTORY.md
- reports/AI_OFFICE_INTEGRATION_PLAN.md

## Micro 6 - Definir contratos de integração

Criar:

- packages/schemas/agent.schema.json
- packages/schemas/task.schema.json
- packages/schemas/tool.schema.json
- packages/schemas/approval.schema.json
- packages/schemas/execution-result.schema.json

## Micro 7 - Adaptar HelpUS AI para multiagente

Criar agentes:

- CEO
- Product
- Architect
- Dev
- Auditor
- Docs
- SDR
- Traffic
- Support
- Finance
- Legal
- Release Manager

## Micro 8 - Criar bridge-relay

Objetivo:

- transformar tarefa aprovada em comando seguro
- enviar ao AI Bridge Local
- registrar resultado AI_LOCAL_RUN
- enviar para auditoria
- atualizar memória operacional

## Micro 9 - Criar dashboard

Primeira versão:

- lista de agentes
- fila de tarefas
- aprovações pendentes
- logs recentes
- custos estimados
- status dos projetos

## Micro 10 - Preparar estratégia Git, Vercel e Railway

- Git para auditoria
- Vercel para frontend
- Railway para backend e workers
- Local para AI Bridge Local
