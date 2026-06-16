# ADR 0002 - Integrar HelpUS AI e AI Bridge Local ao WS AI Office

## Status

Proposto.

## Contexto

O projeto possui dois ativos importantes em andamento:

- AI Bridge Local
- HelpUS AI

Também existe o novo projeto AI Office, criado para representar um escritório virtual com agentes especializados.

Criar o AI Office do zero sem reaproveitar esses ativos geraria duplicação e desperdício.

## Decisão

Usar o AI Office como camada superior de produto e orquestração.

Usar a HelpUS AI como runtime multiagente.

Usar o AI Bridge Local como executor local seguro.

Usar Git como trilha de auditoria.

Usar Vercel para frontend.

Usar Railway para backend, workers, banco e serviços persistentes.

## Consequências positivas

- Reaproveita projetos existentes.
- Reduz retrabalho.
- Mantém o histórico técnico.
- Permite evolução por micros.
- Separa cérebro, executor e interface.
- Aumenta segurança operacional.

## Consequências negativas

- Exige inventário antes de copiar código.
- Exige contratos claros entre componentes.
- Pode exigir refatoração da HelpUS AI.
- Pode exigir adaptação do AI Bridge Local.

## Alternativas consideradas

### Criar AI Office isolado

Rejeitado por duplicar esforço.

### Copiar tudo sem análise

Rejeitado por risco de conflito e manutenção difícil.

### Integrar por contratos

Escolhido.

## Regra de implementação

Antes de copiar código, criar inventário e definir contratos.
