# Projeto Agente Automotivo - Desafio C2S

Este sistema usa o terminal como um agente virtual que vai le auxilia na busca por veículos, utilizando:
- Banco de dados SQLite
- SQLAlchemy
- Comunicação Client-Server via protocolo MCP (baseado em socket)
- Testes automatizados com Pytest

---

## Funcionalidades

- Cadastro automático de 100 veículos fictícios
- Busca por marca, ano, combustível, valor máximo
- Resposta interativa no terminal
- Código limpo, modular e testável

---

## Como rodar o Sistema

**Todos os Comandos tem que ser via terminal** 

1. **Instalar dependências**
    Use o comanado: pip install -r requirements.txt 
    (pra poder instalar as dependencias)

2. **Iniciar servidor**
   Use o comanado: python run.py server  
   (Para o servidor começar a rodar.).

3. **Inserindo Informaçoes no Banco de Dados**
   Use o comanado: python run.py populate 
   (Para Popular(Inserir Informaçoes) no Banco)

4. **Usando o Sistema**
     Use o comanado: python run.py --client
     (para o sistama rodar)

---

## Video de Demonstração do Sistema

[clique ou copiá, para ver o vídeo](https://youtu.be/Hk7AFqTp7gE)

Ao clicar, voce via ser direcionado para o yutube.
