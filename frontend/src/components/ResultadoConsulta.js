import React from 'react';
import styled from 'styled-components';
import ReactMarkdown from 'react-markdown';

const ResultadoContainer = styled.div`
  margin-top: 20px;
  padding: 15px;
  border: 1px solid #e1e4e8;
  border-radius: 6px;
  background-color: #f6f8fa;
`;

const RespostaContainer = styled.div`
  margin-bottom: 15px;
`;

const FontesContainer = styled.div`
  margin-top: 15px;
  border-top: 1px solid #e1e4e8;
  padding-top: 10px;
`;

const FonteItem = styled.div`
  margin-bottom: 8px;
  font-size: 13px;
`;

const FonteLink = styled.a`
  color: #0366d6;
  text-decoration: none;
  
  &:hover {
    text-decoration: underline;
  }
`;

const ResultadoConsulta = ({ resultado }) => {
  if (!resultado) return null;
  
  const { resposta, fontes } = resultado;
  
  return (
    <ResultadoContainer>
      <RespostaContainer>
        <ReactMarkdown>{resposta}</ReactMarkdown>
      </RespostaContainer>
      
      {fontes && fontes.length > 0 && (
        <FontesContainer>
          <h4>Fontes:</h4>
          {fontes.map((fonte, index) => (
            <FonteItem key={index}>
              {fonte.tipo === 'issue' && (
                <span>
                  Issue #{fonte.id}: <FonteLink href={fonte.url} target="_blank" rel="noopener noreferrer">
                    {fonte.url}
                  </FonteLink>
                </span>
              )}
              
              {fonte.tipo === 'pull_request' && (
                <span>
                  Pull Request #{fonte.id}: <FonteLink href={fonte.url} target="_blank" rel="noopener noreferrer">
                    {fonte.url}
                  </FonteLink>
                </span>
              )}
              
              {fonte.tipo === 'commit' && (
                <span>
                  Commit {fonte.sha?.substring(0, 7)}: <FonteLink href={fonte.url} target="_blank" rel="noopener noreferrer">
                    {fonte.url}
                  </FonteLink>
                </span>
              )}
            </FonteItem>
          ))}
        </FontesContainer>
      )}
    </ResultadoContainer>
  );
};

export default ResultadoConsulta;
