# DevSecOps

## Introdução
DevSecOps (DevOps Security Operations) foca em proteger aplicativos e integrar a segurança nos processos de devOps.<br><br>
O DevSecOps ajuda a auditar as infraestruturas de TI existentes, automatizar as ferramentas de segurança executadas em pipelines e permitir uma melhor colaboração e comunicação entre as equipes de desenvolvimento, operações e segurança.

## Objetivo
O objetivo do DevSecOps é promover uma cultura de segurança em que todos os envolvidos no processo de desenvolvimento de software sejam responsáveis pela segurança do produto final.<br><br>
Isso inclui desenvolvedores, engenheiros de segurança, gerentes de operações de sistemas e outros profissionais envolvidos no ciclo de vida do software. <br><br>
Também há quem diga que DevSecOps, é uma evoluçaõ do DevOps.

## As 5 Fases do SEC em DevSecOps
1. **Planejamento**: Nesta fase define-se a estratégia de segurança, identificando riscos, requisitos regulatórios e políticas que devem ser incorporadas ao projeto.
2. **Desenvolvimento**: Os desenvolvedores aplicam práticas seguras de codificação, uso de bibliotecas confiáveis e revisões de código para reduzir vulnerabilidades.
3. **Testes**: São realizados testes de segurança como análise estática, dinâmica e testes de penetração para detectar falhas antes da entrega.
4. **Implantação**: A segurança é aplicada na configuração de ambientes, automação de pipelines e monitoramento de acessos para garantir que o software seja lançado de forma segura.
5. **Operações**: Inclui monitoramento contínuo, resposta a incidentes e aplicação de patches para manter o sistema protegido durante seu uso.

## Necessidade
Precisamos de DevSecOps porque ele integra segurança desde o início do ciclo de desenvolvimento, evitando que vulnerabilidades sejam descobertas apenas no fim, quando corrigir é mais caro e demorado. Ao unir desenvolvimento, operações e segurança em um fluxo contínuo, garantimos que cada etapa, do planejamento à operação, já incorpore práticas seguras, reduzindo riscos, acelerando entregas e aumentando a confiança no software. Em essência, o DevSecOps transforma a segurança em uma responsabilidade compartilhada, não em um obstáculo, permitindo que inovação e proteção caminhem juntas.

## DevOps X DevSecOps
DevOps foca em velocidade e colaboração entre desenvolvimento e operações, enquanto DevSecOps adiciona segurança como parte integral do processo, garantindo que o software seja entregue rápido e seguro. Em outras palavras, DevSecOps é a evolução natural do DevOps, trazendo a segurança para o centro da cultura e do pipeline.

| Aspecto | DevOps | DevSecOps |
| --- | --- | --- |
| **Objetivo** | Entregar software mais rápido e confiável | Entregar software rápido **e seguro por design** |
| **Foco** | Colaboração entre Dev e Ops, automação, CI/CD | Integração da segurança em todas as fases do SDLC |
| **Segurança** | Muitas vezes tratada como etapa final ou separada | “Shift Left”: segurança aplicada desde o planejamento e codificação |
| **Ferramentas** | CI/CD, automação de testes, monitoramento | CI/CD + análise estática, varredura de dependências, testes de vulnerabilidade |
| **Responsabilidade** | Equipes de Dev e Ops compartilham entrega | Todos compartilham segurança, não apenas o time de segurança |
| **Resultado** | Releases rápidos e estáveis | Releases rápidos, estáveis e **com menos vulnerabilidades** |

### Pontos-chave
- **DevOps** nasceu para quebrar silos entre desenvolvimento e operações, acelerando entregas com automação e integração contínua.
- **DevSecOps** surgiu como resposta ao aumento de ataques e requisitos regulatórios, integrando segurança diretamente no pipeline.
- No **DevSecOps**, cada commit dispara não só builds e testes, mas também checagens automáticas de segurança (ex.: análise de código, compliance, varredura de dependências).
- Isso reduz custos, já que corrigir falhas cedo é muito mais barato do que depois da implantação.

### Riscos e trade-offs
- **DevOps sem segurança**: pode gerar software rápido, mas vulnerável.
- **DevSecOps mal implementado**: se os controles forem pesados demais, podem atrasar entregas. O equilíbrio é essencial.
- **Cultura organizacional**: exige mudança de mentalidade — todos devem se sentir responsáveis pela segurança, não apenas o time especializado.