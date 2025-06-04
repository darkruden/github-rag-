# GitHub RAG - Análise e Rastreabilidade de Requisitos

![GitHub RAG Logo](./frontend/public/logo128.png)

## Sobre o Projeto

GitHub RAG é uma extensão para o navegador Google Chrome que integra uma arquitetura de Geração Aumentada por Recuperação (RAG) para análise e rastreabilidade de requisitos de software, utilizando insights extraídos de repositórios do GitHub.

A extensão permite que desenvolvedores e gerentes de projeto consultem informações sobre requisitos em linguagem natural, recebendo respostas contextualizadas baseadas nos dados do repositório (issues, pull requests e commits) e gerem relatórios detalhados sobre a rastreabilidade dos requisitos.

## Arquitetura

O projeto é dividido em duas partes principais:

### Backend (FastAPI)

O backend é responsável por:
- Coletar dados do GitHub através da API oficial
- Processar textos usando vetorização semântica (sentence-transformers)
- Armazenar e consultar embeddings no banco vetorial ChromaDB
- Integrar com o modelo de linguagem GPT-4 via API OpenAI
- Gerar relatórios em Markdown e PDF

### Frontend (Extensão Chrome com React)

O frontend é responsável por:
- Fornecer uma interface amigável através de um popup modal
- Permitir consultas em linguagem natural
- Exibir resultados contextualizados com links para as fontes
- Solicitar e baixar relatórios de rastreabilidade

## Funcionalidades

- **Consulta em Linguagem Natural**: Faça perguntas sobre requisitos e receba respostas contextualizadas
- **Análise de Repositórios**: Extraia insights de issues, pull requests e commits
- **Rastreabilidade de Requisitos**: Visualize como os requisitos estão relacionados ao código
- **Geração de Relatórios**: Exporte relatórios detalhados em Markdown ou PDF
- **Integração com GitHub**: Funciona diretamente na interface do GitHub

## Pré-requisitos

- Python 3.8+
- Node.js 16+
- Conta no GitHub com token de acesso pessoal
- Chave de API da OpenAI
- Google Chrome

## Instalação e Configuração

### Backend

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/github-rag.git
cd github-rag/backend
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas chaves e configurações
```

5. Inicie o servidor:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend (Extensão Chrome)

1. Navegue até a pasta do frontend:
```bash
cd ../frontend
```

2. Instale as dependências:
```bash
npm install
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com a URL do seu backend
```

4. Construa a extensão:
```bash
npm run build
```

5. Carregue a extensão no Chrome:
   - Abra o Chrome e navegue para `chrome://extensions/`
   - Ative o "Modo do desenvolvedor"
   - Clique em "Carregar sem compactação"
   - Selecione a pasta `build` gerada no passo anterior

## Uso

1. Navegue até um repositório no GitHub
2. Clique no ícone da extensão na barra de ferramentas do Chrome
3. Na aba "Consulta":
   - Digite o nome do repositório (ou use o atual se estiver em uma página do GitHub)
   - Faça sua pergunta em linguagem natural
   - Clique em "Consultar"
4. Na aba "Relatório":
   - Digite o nome do repositório
   - Selecione o formato desejado (Markdown ou PDF)
   - Clique em "Gerar Relatório"
   - Baixe o relatório gerado

## Exemplos de Consultas

- "Quais são os requisitos principais deste projeto?"
- "Mostre as issues relacionadas à autenticação de usuários"
- "Quem implementou o requisito de exportação de relatórios?"
- "Qual é o status atual do requisito de integração com API externa?"
- "Liste todos os commits relacionados ao requisito de segurança"

## Estrutura do Projeto

```
github-rag/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── services/
│   │   │   ├── github_service.py
│   │   │   ├── embedding_service.py
│   │   │   ├── llm_service.py
│   │   │   └── report_service.py
│   │   └── main.py
│   ├── tests/
│   └── requirements.txt
└── frontend/
    ├── public/
    │   ├── manifest.json
    │   ├── background.js
    │   └── content.js
    ├── src/
    │   ├── components/
    │   ├── services/
    │   ├── utils/
    │   └── App.js
    └── package.json
```

## API Endpoints

- `GET /health`: Verifica o status do backend
- `GET /test`: Testa a comunicação com o backend
- `POST /api/consultar`: Processa consultas em linguagem natural
- `POST /api/relatorio`: Gera relatórios de rastreabilidade

## Tecnologias Utilizadas

### Backend
- FastAPI: Framework web de alta performance
- sentence-transformers: Biblioteca para geração de embeddings
- ChromaDB: Banco de dados vetorial para armazenamento e busca semântica
- OpenAI API: Acesso ao modelo GPT-4
- PyGithub: Cliente Python para a API do GitHub
- pdfkit: Geração de PDFs a partir de HTML/Markdown

### Frontend
- React: Biblioteca JavaScript para construção de interfaces
- Styled Components: Estilização de componentes React
- Axios: Cliente HTTP para comunicação com o backend
- React Markdown: Renderização de conteúdo Markdown

## Segurança

- Autenticação via token para proteger as rotas da API
- Comunicação HTTPS entre frontend e backend
- Validação de dados de entrada
- Controle de acesso aos recursos do GitHub

## Limitações Conhecidas

- A extensão funciona apenas no Google Chrome
- É necessário ter um token de acesso do GitHub com permissões adequadas
- O consumo da API OpenAI pode gerar custos dependendo do volume de uso
- A análise é limitada aos dados disponíveis no repositório público

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato através de [seu-email@exemplo.com].

---

Desenvolvido como parte de um projeto de TCC - 2025
