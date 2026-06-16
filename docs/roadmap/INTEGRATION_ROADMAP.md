# Roadmap de Integração dos Projetos

## Micro 1 - Inventário dos repositórios

Gerar relatórios:

- reports/AI_BRIDGE_LOCAL_INVENTORY.md
- reports/HELPUS_AI_INVENTORY.md
- reports/AI_OFFICE_INTEGRATION_PLAN.md

Objetivo:

- entender o que existe
- identificar componentes reaproveitáveis
- evitar duplicação desnecessária
- mapear riscos

## Micro 2 - Contratos JSON

Criar schemas:

- packages/schemas/agent.schema.json
- packages/schemas/task.schema.json
- packages/schemas/tool.schema.json
- packages/schemas/approval.schema.json
- packages/schemas/execution-result.schema.json

## Micro 3 - Manifesto multiagente

Criar:

- config/agents.json
- config/tools.json
- config/policies.json

## Micro 4 - Adaptar HelpUS AI

Criar estrutura:

- agents/ceo.md
- agents/product.md
- agents/architect.md
- agents/dev.md
- agents/auditor.md
- agents/docs.md
- agents/sdr.md
- agents/traffic.md
- agents/support.md
- agents/finance.md
- agents/legal.md

## Micro 5 - Criar bridge-relay

Criar serviço que conecta AI Office ao AI Bridge Local.

Responsabilidades:

- enviar tarefa local
- receber resultado
- registrar logs
- acionar auditor

## Micro 6 - Criar painel mínimo

Telas:

- agentes
- tarefas
- aprovações
- logs
- relatórios

## Micro 7 - Deploy inicial

- Vercel para frontend
- Railway para backend
- local para bridge

## Micro 8 - Auditoria e governança

Adicionar:

- classificação de risco
- aprovação humana
- logs de execução
- bloqueios de segurança
- relatório de diff

## Micro 9 - Operação assistida

O sistema começa assistido, não autônomo.

Agentes podem:

- planejar
- sugerir
- criar documentação
- criar tarefas
- preparar patches

Agentes não podem, sem aprovação:

- deploy
- push
- commit
- envio externo
- alteração de campanha
- exclusão de arquivos
