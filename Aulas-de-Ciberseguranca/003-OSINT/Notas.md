# OSINT 🔍
## O que é OSINT?
OSINT (Open Source Intelligence, ou Inteligência de Fontes Abertas) é a prática de coletar, processar e analisar informações disponíveis publicamente (como redes sociais, registros oficiais e notícias) para transformá-las em conhecimento útil e estratégico. Diferente de espionagem ou hacking, o OSINT só utiliza fontes abertas e legais, mas exige metodologia rigorosa para gerar inteligência confiável.

## Mentalidade OSINT
### Perguntas norteadoras:
- Quais as fontes escolhidas?
- Qual a confiabilidade das fontes?
- Quais palavras chaves utilizar?
- Quais as melhores ferramentas?

### Estratégias:
| Ofensiva | Passiva |
| -- | -- |
| Faz contato direto com o alvo | Não faz contato direto com o alvo |
| Consegue informações mais acuradas | Depende de informações de terceiros |
| Risco maior de ser detectado pelo alvo | Menor risco de ser detectado pelo alvo |

## Google Hacking 
Google hacking (ou Google dorking) é o uso de operadores avançados de busca para localizar informações sensíveis que estão publicamente indexadas pelo Google, mas que não deveriam ser facilmente acessíveis. Esses “dorks” são consultas específicas que podem revelar páginas de login, arquivos expostos ou dados confidenciais, por isso são ferramentas poderosas tanto para auditorias de segurança quanto para cibercriminosos.

### Exemplos de Dorks
- `site:` Busca em um site específico: `site:exemplo.com.br`
- `intitle:` Busca por título de páginas: `intitle:"< Fazer Login"`
- `inurl:` Busca de termos presentes na url: `inurl:/wp-admin`
- `intext:` Busca por termos no conteúdo do site: `intext:adminpass`
- `filetype:` Busca por formato de arquivos: `filetype:.txt`
- `-termo:` O sinal de "-" exclui um termo da pesquisa
- `2022...2023:` Busca entre duas datas
> Banco de dados de Dorks: `Exploit-db` e `InurlBR`

### Exercício prático com Dorks
```txt
intext:"index of" ".sql"

intitle:"llS Windows Server"

inurl:"admin/default.aspx"
```

## Shodan
O Shodan é um motor de busca especializado que **indexa dispositivos conectados à internet** (como câmeras IP, roteadores, servidores, bancos de dados e sistemas industriais) permitindo que qualquer pessoa veja quais serviços estão expostos publicamente. Diferente do Google, que indexa páginas web, o Shodan coleta informações técnicas (banners, portas abertas, versões de software) e organiza em um catálogo pesquisável.

**Definição**: Motor de busca criado em 2009 por John Matherly, focado em dispositivos e serviços expostos na internet.
**Apelido**: Muitas vezes chamado de “o motor de busca mais assustador do mundo”, porque revela a quantidade de sistemas acessíveis sem proteção.
**Escopo**: Indexa mais de 500 milhões de dispositivos em mais de 200 países.

### Como funciona
- **Banner grabbing**: O Shodan conecta-se a portas TCP/UDP de endereços IPv4 públicos e coleta os “banners” (informações que serviços de rede apresentam ao se conectar).
- **Dados coletados**:
  - Tipo de serviço (HTTP, FTP, SSH, RDP etc.)
  - Versão do software
  - Certificados SSL/TLS
  - Geolocalização do IP
  - Organização responsável pelo bloco de endereços
- **Interface**: Disponível via web, linha de comando (CLI) e API para integração com scripts e ferramentas de segurança.

### Exemplos de uso
- **Segurança defensiva**:
  - Monitorar se servidores internos foram expostos por engano.
  - Detectar bancos de dados sem autenticação ou portas administrativas abertas.
- **OSINT e pesquisa**:
  - Jornalistas e analistas usam para documentar falhas em infraestrutura digital.
- **Filtros poderosos**:
  - `country:BR port:3389` - lista serviços de Remote Desktop expostos no Brasil.
  - `product:Apache version:2.4.49` - encontra servidores vulneráveis a exploits conhecidos.
