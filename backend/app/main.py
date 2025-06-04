from fastapi import FastAPI, Depends, HTTPException, status, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar aplicação FastAPI
app = FastAPI(
    title="GitHub RAG API",
    description="API para análise e rastreabilidade de requisitos de software usando RAG",
    version="0.1.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de dados
class ConsultaRequest(BaseModel):
    query: str
    repositorio: str
    filtros: Optional[Dict[str, Any]] = None

class RelatorioRequest(BaseModel):
    repositorio: str
    requisitos: Optional[List[str]] = None
    formato: str = "markdown"  # markdown ou pdf

class ConsultaResponse(BaseModel):
    resposta: str
    fontes: List[Dict[str, Any]]
    contexto: Optional[Dict[str, Any]] = None

class RelatorioResponse(BaseModel):
    url: str
    formato: str

# Função para verificar token de autenticação
async def verificar_token(x_api_key: str = Header(...)):
    if x_api_key != os.getenv("API_TOKEN"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de API inválido"
        )
    return x_api_key

# Rotas da API
@app.get("/health")
async def health_check():
    return {"status": "online", "version": "0.1.0"}

@app.get("/test")
async def test_route():
    return {"message": "Conexão com o backend estabelecida com sucesso!"}

@app.post("/api/consultar", response_model=ConsultaResponse, dependencies=[Depends(verificar_token)])
async def consultar(request: ConsultaRequest):
    # Implementação temporária - será substituída pela lógica RAG
    return {
        "resposta": f"Resposta para a consulta: {request.query}",
        "fontes": [
            {"tipo": "issue", "id": "123", "url": f"https://github.com/{request.repositorio}/issues/123"}
        ],
        "contexto": {"repositorio": request.repositorio}
    }

@app.post("/api/relatorio", response_model=RelatorioResponse, dependencies=[Depends(verificar_token)])
async def gerar_relatorio(request: RelatorioRequest):
    # Implementação temporária - será substituída pela geração real de relatórios
    return {
        "url": f"https://exemplo.com/relatorios/{request.repositorio.replace('/', '_')}.{request.formato}",
        "formato": request.formato
    }

# Ponto de entrada para execução direta
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
