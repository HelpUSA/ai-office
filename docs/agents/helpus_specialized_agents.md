# Agentes Especializados da HelpUS AI

## Estratégia

A HelpUS AI deve ser transformada em um conjunto de agentes especializados para operar o escritório virtual.

## Lista inicial

| Agente | Função | Risco padrão |
|---|---|---|
| HelpUS CEO | Orquestrar tarefas | Médio |
| HelpUS Product | Requisitos e backlog | Baixo |
| HelpUS Architect | Arquitetura e ADRs | Médio |
| HelpUS Dev | Código e scripts | Médio |
| HelpUS Auditor | Revisão e risco | Baixo |
| HelpUS Docs | Documentação | Baixo |
| HelpUS SDR | Leads e prospecção | Médio |
| HelpUS Traffic | Campanhas | Alto |
| HelpUS Support | Atendimento | Médio |
| HelpUS Finance | Custos e financeiro | Alto |
| HelpUS Legal | Risco jurídico | Alto |
| HelpUS Release Manager | Deploy e release | Alto |

## Regras

- Todo agente tem missão clara.
- Todo agente tem ferramentas limitadas.
- Todo agente registra saída estruturada.
- Todo agente de alto risco exige aprovação.
- Auditor pode bloquear execução.

## Próximo passo

Criar arquivos de prompt para cada agente e conectar ao manifesto config/agents.json.
