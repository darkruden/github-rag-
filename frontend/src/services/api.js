import axios from 'axios';

// URL base da API - deve ser configurada no ambiente
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Token de autenticação - deve ser configurado no ambiente
const API_TOKEN = process.env.REACT_APP_API_TOKEN || 'token_temporario';

// Configuração do cliente axios
const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': API_TOKEN
  }
});

/**
 * Testa a conexão com o backend
 * @returns {Promise} Resposta da API
 */
export const testarConexao = async () => {
  try {
    const response = await apiClient.get('/health');
    return response.data;
  } catch (error) {
    console.error('Erro ao testar conexão:', error);
    throw error;
  }
};

/**
 * Envia uma consulta para a API
 * @param {Object} dados - Dados da consulta
 * @returns {Promise} Resposta da API
 */
export const consultarAPI = async (dados) => {
  try {
    const response = await apiClient.post('/api/consultar', dados);
    return response.data;
  } catch (error) {
    console.error('Erro na consulta:', error);
    throw error;
  }
};

/**
 * Solicita a geração de um relatório
 * @param {Object} dados - Dados para geração do relatório
 * @returns {Promise} Resposta da API com URL do relatório
 */
export const gerarRelatorio = async (dados) => {
  try {
    const response = await apiClient.post('/api/relatorio', dados);
    return response.data;
  } catch (error) {
    console.error('Erro ao gerar relatório:', error);
    throw error;
  }
};

/**
 * Extrai informações do repositório atual no GitHub
 * @returns {Object} Informações do repositório
 */
export const extrairInfoRepositorio = async () => {
  // Esta função será chamada pelo content script para extrair informações da página atual
  try {
    // Implementação básica para extrair o nome do repositório da URL
    const url = window.location.href;
    const match = url.match(/github\.com\/([^\/]+\/[^\/]+)/);
    
    if (match && match[1]) {
      return {
        repositorio: match[1],
        url: url
      };
    }
    
    throw new Error('Não foi possível identificar o repositório');
  } catch (error) {
    console.error('Erro ao extrair informações do repositório:', error);
    throw error;
  }
};
