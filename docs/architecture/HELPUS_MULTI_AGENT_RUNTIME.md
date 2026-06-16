# HelpUS AI como Runtime Multiagente

## Ideia

A HelpUS AI deve deixar de ser apenas uma IA única e passar a operar como uma fábrica de agentes especializados.

Cada agente usa a mesma base da HelpUS, mas com:

- identidade própria
- missão específica
- ferramentas permitidas
- nível de autonomia
- regras de aprovação
- memória operacional filtrada
- critérios de qualidade

## Agentes propostos

### HelpUS CEO

- Orquestra o escritório.
- Recebe pedidos.
- Divide tarefas.
- Escolhe agentes.
- Consolida resultados.

### HelpUS Product

- Transforma ideias em requisitos.
- Cria backlog.
- Define MVP.
- Escreve histórias de usuário.

### HelpUS Architect

- Define arquitetura.
- Avalia trade-offs.
- Cria ADRs.
- Revisa decisões técnicas.

### HelpUS Dev

- Implementa código.
- Cria scripts.
- Corrige bugs.
- Roda testes.
- Entrega relatório técnico.

### HelpUS Auditor

- Revisa diff.
- Classifica risco.
- Confere testes.
- Bloqueia ações inseguras.

### HelpUS Docs

- Atualiza documentação.
- Cria runbooks.
- Registra decisões.
- Mantém changelog.

### HelpUS SDR

- Busca oportunidades.
- Organiza leads.
- Classifica prospects.
- Prepara abordagem.

### HelpUS Traffic

- Analisa campanhas.
- Detecta anomalias.
- Sugere ajustes.
- Gera relatórios.

### HelpUS Support

- Classifica mensagens.
- Sugere respostas.
- Cria base de conhecimento.

### HelpUS Finance

- Monitora custos.
- Gera relatórios financeiros.
- Alerta gastos.

### HelpUS Legal

- Identifica riscos jurídicos.
- Sugere cautelas.
- Revisa textos sensíveis.

## Contrato de agente

Cada agente deve ter:

- id
- name
- role
- mission
- tools
- can_do
- cannot_do
- approval_required_for
- output_format
- quality_gates

## Níveis de autonomia

- Nível 0: só responde.
- Nível 1: lê e resume.
- Nível 2: sugere.
- Nível 3: cria arquivos seguros.
- Nível 4: executa comandos seguros.
- Nível 5: executa ações externas com aprovação.
- Nível 6: autonomia parcial auditada.
