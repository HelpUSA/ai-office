# 09 - Integração com Projetos Atuais

## Objetivo

Definir como o WS AI Office deve reaproveitar os projetos já existentes em vez de começar do zero.

Os projetos principais são:

- AI Bridge Local
- HelpUS AI
- AI Office

## Visão consolidada

O WS AI Office deve ser a camada superior de produto e orquestração.

A HelpUS AI deve ser o cérebro conversacional e o runtime de agentes.

O AI Bridge Local deve ser o executor local seguro, responsável por comandos, validações, smokes, inspeções e integração com repositórios locais.

Git deve ser a trilha de auditoria técnica.

Vercel deve hospedar o painel web e a experiência do usuário.

Railway deve hospedar backend, workers, filas, banco e serviços persistentes.

## Papel de cada parte

### AI Office

- Painel central.
- Orquestrador.
- Cadastro de agentes.
- Fila de tarefas.
- Aprovações humanas.
- Logs e relatórios.
- Visão operacional do escritório.

### HelpUS AI

- Motor de inteligência.
- Conversa com usuário.
- Classificação de intenção.
- Criação de planos.
- Execução de agentes especializados.
- Memória operacional.
- Handoff entre agentes.

### AI Bridge Local

- Execução local segura.
- Comandos em repositórios locais.
- git status, git diff e validações.
- Smokes e testes.
- Aplicação de patches controlados.
- Retorno padronizado de resultados.

## Decisão central

Não criar um terceiro sistema isolado.

O AI Office deve aproveitar HelpUS AI e AI Bridge Local como blocos estruturais.

## Regra de segurança

Nenhuma IA deve fazer commit, push, deploy, alteração de campanha, envio externo ou operação destrutiva sem aprovação humana explícita.
