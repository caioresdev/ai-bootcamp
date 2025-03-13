# RAG

Temos um Embedding Model que consulta um VectorDB que possui as informações de Documentos, Sites..

É feito uma pergunta pro Embedding Model, o Embedding Model busca os Chunks mais relevantes de informações no VectorDB. 

Isso é passado como contexto para um Modelo de LLM e é transformado em uma resposta para o Usuário final.

Ferramentas existentes:

https://smallpdf.com/chat-pdf
https://pdf.ai/
https://www.chatpdf.com/pt
https://www.chatbase.co/
https://askyourpdf.com/pt

# Arquitetura

