# Documentação Técnica - GitHub RAG

## Arquitetura Detalhada

### Visão Geral

O GitHub RAG implementa uma arquitetura de Geração Aumentada por Recuperação (RAG) para análise de requisitos de software. A arquitetura é dividida em camadas bem definidas:

1. **Camada de Interface (Frontend)**: Extensão Chrome desenvolvida com React
2. **Camada de API (Backend)**: Servidor FastAPI para processamento e integração
3. **Camada de Serviços**: Módulos especializados para diferentes funcionalidades
4. **Camada de Armazenamento**: ChromaDB para vetores e sistema de arquivos para relatórios

### Diagrama de Componentes

```
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|  Extensão Chrome  +---->+  Backend FastAPI  +---->+  API do GitHub    |
|  (React)          |     |                   |     |                   |
|                   |     |                   |     +-------------------+
+-------------------+     +--------+----------+
                                   |
                                   v
                          +--------+----------+     +-------------------+
                          |                   |     |                   |
                          |  ChromaDB         |     |  API OpenAI       |
                          |  (Banco Vetorial) |     |  (GPT-4)          |
                          |                   |     |                   |
                          +-------------------+     +-------------------+
```

### Fluxo de Dados

1. O usuário interage com a extensão Chrome, enviando consultas ou solicitando relatórios
2. A extensão comunica-se com o backend via API REST
3. O backend processa a solicitação:
   - Para consultas: coleta dados do GitHub, processa embeddings, consulta o ChromaDB e gera resposta via OpenAI
   - Para relatórios: coleta dados do GitHub, analisa relações entre requisitos e gera relatório formatado
4. O resultado é retornado para a extensão e apresentado ao usuário

## Componentes do Backend

### Serviços Principais

#### 1. GitHub Service (`github_service.py`)

Responsável pela comunicação com a API do GitHub e coleta de dados.

**Funcionalidades principais:**
- Obtenção de issues, pull requests e commits
- Pesquisa de código em repositórios
- Extração de metadados de repositórios

**Dependências:**
- PyGithub

#### 2. Embedding Service (`embedding_service.py`)

Responsável pelo processamento de embeddings e interação com o ChromaDB.

**Funcionalidades principais:**
- Geração de embeddings para textos usando sentence-transformers
- Armazenamento e consulta de embeddings no ChromaDB
- Processamento de dados do GitHub para indexação vetorial

**Dependências:**
- sentence-transformers
- ChromaDB

#### 3. LLM Service (`llm_service.py`)

Responsável pela integração com modelos de linguagem grandes (LLMs).

**Funcionalidades principais:**
- Geração de respostas contextuais usando a API OpenAI
- Formatação de prompts com contexto relevante
- Geração de relatórios em formato Markdown
- Monitoramento de uso de tokens

**Dependências:**
- OpenAI API

#### 4. Report Service (`report_service.py`)

Responsável pela geração de relatórios em diferentes formatos.

**Funcionalidades principais:**
- Conversão de Markdown para HTML e PDF
- Formatação e estilização de relatórios
- Armazenamento de relatórios gerados

**Dependências:**
- markdown
- pdfkit

### API Endpoints

#### Rotas Principais

1. **Health Check**
   - Endpoint: `GET /health`
   - Descrição: Verifica o status do backend
   - Resposta: `{"status": "online", "version": "0.1.0"}`

2. **Teste de Conexão**
   - Endpoint: `GET /test`
   - Descrição: Testa a comunicação com o backend
   - Resposta: `{"message": "Conexão com o backend estabelecida com sucesso!"}`

3. **Consulta**
   - Endpoint: `POST /api/consultar`
   - Descrição: Processa consultas em linguagem natural
   - Autenticação: Token via header `X-API-Key`
   - Corpo da requisição:
     ```json
     {
       "query": "Como funciona o sistema de autenticação?",
       "repositorio": "usuario/repositorio",
       "filtros": {}
     }
     ```
   - Resposta:
     ```json
     {
       "resposta": "O sistema de autenticação utiliza...",
       "fontes": [
         {
           "tipo": "issue",
           "id": 123,
           "url": "https://github.com/usuario/repositorio/issues/123"
         }
       ],
       "contexto": {
         "repositorio": "usuario/repositorio"
       }
     }
     ```

4. **Relatório**
   - Endpoint: `POST /api/relatorio`
   - Descrição: Gera relatórios de rastreabilidade
   - Autenticação: Token via header `X-API-Key`
   - Corpo da requisição:
     ```json
     {
       "repositorio": "usuario/repositorio",
       "requisitos": ["req1", "req2"],
       "formato": "markdown"
     }
     ```
   - Resposta:
     ```json
     {
       "url": "https://exemplo.com/relatorios/usuario_repositorio.markdown",
       "formato": "markdown"
     }
     ```

#### Autenticação

Todas as rotas da API (exceto `/health` e `/test`) são protegidas por autenticação via token. O token deve ser enviado no header `X-API-Key` e deve corresponder ao valor configurado na variável de ambiente `API_TOKEN`.

## Componentes do Frontend

### Estrutura da Extensão Chrome

```
frontend/
├── public/
│   ├── manifest.json    # Configuração da extensão
│   ├── background.js    # Script de background
│   ├── content.js       # Script injetado nas páginas do GitHub
│   └── index.html       # Página HTML do popup
├── src/
│   ├── components/      # Componentes React
│   │   ├── ConsultaForm.js
│   │   ├── RelatorioForm.js
│   │   ├── ResultadoConsulta.js
│   │   └── Header.js
│   ├── services/        # Serviços e APIs
│   │   └── api.js
│   ├── utils/           # Utilitários
│   ├── App.js           # Componente principal
│   └── index.js         # Ponto de entrada
└── package.json         # Dependências e scripts
```

### Componentes Principais

#### 1. App.js

Componente principal que gerencia o estado da aplicação e coordena os demais componentes.

**Funcionalidades:**
- Gerenciamento de abas (Consulta/Relatório)
- Verificação de conexão com o backend
- Coordenação de consultas e exibição de resultados

#### 2. ConsultaForm.js

Formulário para envio de consultas em linguagem natural.

**Funcionalidades:**
- Entrada de dados do repositório
- Campo para consulta em texto livre
- Validação de formulário
- Feedback visual durante carregamento

#### 3. ResultadoConsulta.js

Componente para exibição dos resultados de consultas.

**Funcionalidades:**
- Renderização de Markdown
- Exibição de fontes com links
- Formatação de diferentes tipos de fontes (issues, PRs, commits)

#### 4. RelatorioForm.js

Formulário para geração de relatórios.

**Funcionalidades:**
- Entrada de dados do repositório
- Seleção de formato (Markdown/PDF)
- Link para download do relatório gerado
- Feedback visual durante geração

### Serviços

#### api.js

Serviço para comunicação com o backend.

**Funcionalidades:**
- Configuração do cliente Axios
- Métodos para consulta e geração de relatórios
- Tratamento de erros de comunicação
- Extração de informações do repositório atual

## Fluxos de Uso

### Fluxo de Consulta

1. Usuário abre a extensão em uma página do GitHub
2. A extensão extrai automaticamente o nome do repositório atual
3. Usuário digita uma consulta em linguagem natural
4. A extensão envia a consulta para o backend
5. O backend:
   - Coleta dados do repositório via API do GitHub
   - Processa os textos e gera embeddings
   - Armazena os embeddings no ChromaDB
   - Consulta o ChromaDB para encontrar documentos relevantes
   - Envia os documentos relevantes para a API OpenAI
   - Recebe e formata a resposta
6. A extensão exibe a resposta com links para as fontes

### Fluxo de Geração de Relatório

1. Usuário abre a extensão e seleciona a aba "Relatório"
2. Usuário insere o nome do repositório e seleciona o formato
3. A extensão envia a solicitação para o backend
4. O backend:
   - Coleta dados do repositório via API do GitHub
   - Analisa as relações entre issues, PRs e commits
   - Identifica padrões de requisitos
   - Gera um relatório estruturado usando a API OpenAI
   - Converte o relatório para o formato solicitado
   - Armazena o relatório e retorna a URL
5. A extensão exibe um link para download do relatório

## Considerações de Segurança

### Autenticação e Autorização

- Token de API para proteger endpoints do backend
- Token do GitHub com escopo limitado
- Chave da API OpenAI protegida por variáveis de ambiente

### Validação de Dados

- Validação de entrada em todos os endpoints
- Sanitização de dados antes do processamento
- Tratamento adequado de erros

### Comunicação Segura

- HTTPS para todas as comunicações
- Headers de segurança configurados
- Proteção contra CSRF

## Otimizações

### Performance

- Cache de embeddings para consultas frequentes
- Reutilização de conexões HTTP
- Processamento assíncrono de tarefas pesadas

### Consumo de API

- Controle de taxa de requisições para GitHub e OpenAI
- Monitoramento de uso de tokens da OpenAI
- Estratégias para minimizar chamadas redundantes

## Extensibilidade

O sistema foi projetado para ser facilmente extensível:

1. **Novos Modelos LLM**: A arquitetura permite substituir o GPT-4 por outros modelos
2. **Fontes de Dados Adicionais**: Além do GitHub, outras fontes podem ser integradas
3. **Formatos de Relatório**: Novos formatos podem ser adicionados ao serviço de relatórios
4. **Análises Personalizadas**: Novos tipos de análise podem ser implementados como serviços adicionais
