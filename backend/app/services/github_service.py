import os
from github import Github
from typing import List, Dict, Any, Optional

class GitHubService:
    """
    Serviço para interação com a API do GitHub.
    Responsável por coletar dados de repositórios, issues, pull requests e commits.
    """
    
    def __init__(self, token: str = None):
        """
        Inicializa o serviço GitHub com um token de autenticação.
        
        Args:
            token: Token de acesso à API do GitHub
        """
        self.token = token or os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("Token do GitHub não fornecido")
        
        self.github = Github(self.token)
    
    def get_repository(self, repo_name: str):
        """
        Obtém um repositório do GitHub.
        
        Args:
            repo_name: Nome do repositório no formato 'usuario/repositorio'
            
        Returns:
            Objeto repositório do GitHub
        """
        try:
            return self.github.get_repo(repo_name)
        except Exception as e:
            raise Exception(f"Erro ao acessar repositório {repo_name}: {str(e)}")
    
    def get_issues(self, repo_name: str, state: str = "all", labels: List[str] = None) -> List[Dict[str, Any]]:
        """
        Obtém issues de um repositório.
        
        Args:
            repo_name: Nome do repositório no formato 'usuario/repositorio'
            state: Estado das issues ('open', 'closed', 'all')
            labels: Lista de labels para filtrar
            
        Returns:
            Lista de issues formatadas como dicionários
        """
        repo = self.get_repository(repo_name)
        issues = []
        
        for issue in repo.get_issues(state=state, labels=labels):
            # Pular pull requests (que também são considerados issues na API)
            if issue.pull_request:
                continue
                
            issues.append({
                "id": issue.number,
                "title": issue.title,
                "body": issue.body,
                "state": issue.state,
                "created_at": issue.created_at.isoformat(),
                "updated_at": issue.updated_at.isoformat(),
                "labels": [label.name for label in issue.labels],
                "url": issue.html_url,
                "author": issue.user.login if issue.user else None,
                "comments_count": issue.comments
            })
        
        return issues
    
    def get_pull_requests(self, repo_name: str, state: str = "all") -> List[Dict[str, Any]]:
        """
        Obtém pull requests de um repositório.
        
        Args:
            repo_name: Nome do repositório no formato 'usuario/repositorio'
            state: Estado dos PRs ('open', 'closed', 'all')
            
        Returns:
            Lista de pull requests formatados como dicionários
        """
        repo = self.get_repository(repo_name)
        pull_requests = []
        
        for pr in repo.get_pulls(state=state):
            pull_requests.append({
                "id": pr.number,
                "title": pr.title,
                "body": pr.body,
                "state": pr.state,
                "created_at": pr.created_at.isoformat(),
                "updated_at": pr.updated_at.isoformat(),
                "merged": pr.merged,
                "url": pr.html_url,
                "author": pr.user.login if pr.user else None,
                "comments_count": pr.comments
            })
        
        return pull_requests
    
    def get_commits(self, repo_name: str, branch: str = None, path: str = None) -> List[Dict[str, Any]]:
        """
        Obtém commits de um repositório.
        
        Args:
            repo_name: Nome do repositório no formato 'usuario/repositorio'
            branch: Nome da branch (opcional)
            path: Caminho do arquivo para filtrar commits (opcional)
            
        Returns:
            Lista de commits formatados como dicionários
        """
        repo = self.get_repository(repo_name)
        commits = []
        
        for commit in repo.get_commits(sha=branch, path=path):
            commits.append({
                "sha": commit.sha,
                "message": commit.commit.message,
                "author": commit.commit.author.name,
                "author_email": commit.commit.author.email,
                "date": commit.commit.author.date.isoformat(),
                "url": commit.html_url
            })
        
        return commits
    
    def get_repository_info(self, repo_name: str) -> Dict[str, Any]:
        """
        Obtém informações gerais sobre um repositório.
        
        Args:
            repo_name: Nome do repositório no formato 'usuario/repositorio'
            
        Returns:
            Dicionário com informações do repositório
        """
        repo = self.get_repository(repo_name)
        
        return {
            "name": repo.name,
            "full_name": repo.full_name,
            "description": repo.description,
            "url": repo.html_url,
            "stars": repo.stargazers_count,
            "forks": repo.forks_count,
            "open_issues": repo.open_issues_count,
            "created_at": repo.created_at.isoformat(),
            "updated_at": repo.updated_at.isoformat(),
            "language": repo.language,
            "topics": repo.get_topics()
        }
    
    def search_code(self, repo_name: str, query: str) -> List[Dict[str, Any]]:
        """
        Pesquisa código em um repositório.
        
        Args:
            repo_name: Nome do repositório no formato 'usuario/repositorio'
            query: Termo de pesquisa
            
        Returns:
            Lista de resultados da pesquisa
        """
        results = []
        search_query = f"repo:{repo_name} {query}"
        
        for code_result in self.github.search_code(search_query):
            results.append({
                "name": code_result.name,
                "path": code_result.path,
                "url": code_result.html_url,
                "repository": code_result.repository.full_name
            })
        
        return results
