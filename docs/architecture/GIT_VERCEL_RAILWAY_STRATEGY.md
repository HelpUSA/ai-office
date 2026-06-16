# Estratégia com Git, Vercel e Railway

## Git

Git deve ser a trilha de auditoria técnica do projeto.

Tudo que for código, documentação ou configuração deve passar por:

- branch
- diff
- teste
- revisão
- commit aprovado
- deploy controlado

## Vercel

Vercel deve hospedar a interface web do AI Office.

Responsabilidades:

- dashboard
- páginas de agentes
- fila de tarefas
- aprovações
- relatórios
- experiência do usuário

Não usar Vercel como worker pesado.

## Railway

Railway deve hospedar backend e serviços persistentes.

Responsabilidades:

- API principal
- banco
- workers
- filas
- runtime de agentes
- integrações externas

## Local

O ambiente local continua importante para:

- AI Bridge Local
- repositórios locais
- testes
- desenvolvimento
- comandos PowerShell e Python

## Estratégia de deploy

### Frontend

Deploy via Vercel a partir de Git.

### Backend

Deploy via Railway a partir de Git.

### Executor local

Permanece local e se comunica com o AI Office por eventos, fila ou relay autorizado.

## Regra

Nenhum deploy deve acontecer sem aprovação humana explícita enquanto o sistema estiver em fase inicial.
