# Exemplos de Uso - GitHub RAG

Este documento contém exemplos práticos de uso da extensão GitHub RAG para análise e rastreabilidade de requisitos.

## Exemplo 1: Consulta Básica sobre Requisitos

### Cenário
Você está trabalhando em um projeto e precisa entender rapidamente quais são os requisitos principais.

### Passos
1. Navegue até o repositório do projeto no GitHub
2. Clique no ícone da extensão GitHub RAG na barra de ferramentas
3. Na aba "Consulta", o nome do repositório já estará preenchido automaticamente
4. Digite a consulta: "Quais são os principais requisitos deste projeto?"
5. Clique em "Consultar"

### Resultado
A extensão retornará uma resposta contextualizada, listando os principais requisitos identificados no repositório, com links para as issues, pull requests e commits relacionados.

![Exemplo de Consulta](./docs/images/exemplo_consulta.png)

## Exemplo 2: Análise de Rastreabilidade

### Cenário
Você precisa entender como um requisito específico foi implementado e testado.

### Passos
1. Navegue até o repositório do projeto no GitHub
2. Clique no ícone da extensão GitHub RAG
3. Na aba "Consulta", digite: "Como foi implementado o requisito de autenticação de usuários?"
4. Clique em "Consultar"

### Resultado
A extensão analisará issues, pull requests e commits relacionados à autenticação de usuários, fornecendo uma resposta detalhada sobre a implementação, com links para os artefatos relevantes.

## Exemplo 3: Geração de Relatório de Requisitos

### Cenário
Você precisa gerar um relatório completo sobre os requisitos do projeto para uma reunião de revisão.

### Passos
1. Navegue até o repositório do projeto no GitHub
2. Clique no ícone da extensão GitHub RAG
3. Selecione a aba "Relatório"
4. Verifique se o nome do repositório está correto
5. Selecione o formato "PDF"
6. Clique em "Gerar Relatório"

### Resultado
A extensão gerará um relatório PDF detalhado contendo:
- Lista de todos os requisitos identificados
- Mapeamento entre requisitos e artefatos (issues, PRs, commits)
- Análise de status e progresso
- Recomendações para melhorias na documentação

![Exemplo de Relatório](./docs/images/exemplo_relatorio.png)

## Exemplo 4: Consulta sobre Histórico de Alterações

### Cenário
Você precisa entender como um requisito evoluiu ao longo do tempo.

### Passos
1. Navegue até o repositório do projeto no GitHub
2. Clique no ícone da extensão GitHub RAG
3. Na aba "Consulta", digite: "Como o requisito de exportação de dados evoluiu desde o início do projeto?"
4. Clique em "Consultar"

### Resultado
A extensão fornecerá uma linha do tempo das alterações relacionadas ao requisito de exportação de dados, mostrando como ele evoluiu através de diferentes issues, pull requests e commits.

## Exemplo 5: Identificação de Dependências entre Requisitos

### Cenário
Você precisa entender as dependências entre diferentes requisitos do projeto.

### Passos
1. Navegue até o repositório do projeto no GitHub
2. Clique no ícone da extensão GitHub RAG
3. Na aba "Consulta", digite: "Quais requisitos dependem do sistema de autenticação?"
4. Clique em "Consultar"

### Resultado
A extensão analisará as relações entre requisitos e identificará quais dependem do sistema de autenticação, fornecendo links para as issues e pull requests relevantes.

## Dicas para Consultas Eficientes

1. **Seja específico**: Quanto mais específica for sua consulta, mais precisa será a resposta.
   - Bom: "Como foi implementada a autenticação via OAuth?"
   - Menos eficiente: "Como funciona a autenticação?"

2. **Use termos técnicos**: A extensão reconhece termos técnicos e jargões de desenvolvimento.
   - Bom: "Quais padrões de design foram usados na implementação do módulo de pagamento?"
   - Menos eficiente: "Como foi feito o módulo de pagamento?"

3. **Referencie artefatos específicos**: Você pode referenciar issues, PRs ou commits específicos.
   - Bom: "Quais requisitos foram afetados pela issue #123?"
   - Menos eficiente: "Quais requisitos foram alterados recentemente?"

4. **Combine com filtros**: Use filtros para refinar suas consultas.
   - Bom: "Mostre os requisitos de segurança implementados no último mês"
   - Menos eficiente: "Mostre os requisitos de segurança"

## Troubleshooting Comum

### Problema: A extensão não consegue conectar ao backend
**Solução**: Verifique se o servidor backend está em execução e se a URL configurada no arquivo .env da extensão está correta.

### Problema: A consulta retorna "Não foi possível encontrar informações relevantes"
**Solução**: Tente reformular sua consulta usando termos que aparecem nas issues e commits do repositório.

### Problema: O relatório gerado está incompleto
**Solução**: Verifique se o token do GitHub tem permissões suficientes para acessar todos os dados do repositório.

### Problema: A extensão está lenta para responder
**Solução**: Para repositórios muito grandes, a primeira consulta pode levar mais tempo enquanto os dados são processados e armazenados. Consultas subsequentes serão mais rápidas.

### Problema: Erro de autenticação ao acessar a API
**Solução**: Verifique se o token de API configurado no arquivo .env do backend corresponde ao token enviado pela extensão.
