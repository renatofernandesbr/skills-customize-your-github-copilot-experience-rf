# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar livros usando o framework FastAPI. Você praticará rotas HTTP, modelos de dados, operações CRUD e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Executar a Aplicação FastAPI

#### Descrição
Complete o starter code para criar uma aplicação FastAPI e uma rota de verificação em `/health`. Instale as dependências com `python -m pip install fastapi uvicorn`, inicie o servidor localmente e consulte a rota no navegador ou com uma ferramenta HTTP.

#### Requisitos
A aplicação concluída deve:

- Criar uma instância de `FastAPI`
- Responder a `GET /health` com um JSON indicando que a API está ativa
- Iniciar com `uvicorn starter-code:app --reload`


### 🛠️ Consultar Livros

#### Descrição
Crie um modelo `Book` com título, autor e ano de publicação. Use uma coleção em memória para guardar livros e implemente rotas para listar todos e consultar um livro por ID.

#### Requisitos
A API concluída deve:

- Definir os campos do livro usando um modelo Pydantic
- Responder a `GET /books` com a lista de livros
- Responder a `GET /books/{book_id}` com o livro solicitado
- Retornar o status HTTP `404` quando o ID não existir


### 🛠️ Adicionar e Remover Livros

#### Descrição
Implemente a criação e a remoção de livros para completar mais operações CRUD. Atribua um ID único a cada livro criado e retorne respostas HTTP coerentes com o resultado.

#### Requisitos
A API concluída deve:

- Criar um livro com `POST /books` e retornar o status HTTP `201`
- Atribuir e devolver um ID para cada livro criado
- Remover um livro com `DELETE /books/{book_id}`
- Retornar o status HTTP `404` ao tentar remover um ID inexistente


### 🛠️ Atualizar um Livro

#### Descrição
Implemente `PUT /books/{book_id}` para atualizar os dados de um livro existente. Teste o fluxo completo enviando requisições para criar, consultar, atualizar e remover livros.

#### Requisitos
A API concluída deve:

- Atualizar título, autor e ano de um livro existente
- Retornar o livro atualizado na resposta
- Retornar o status HTTP `404` quando o livro não existir
- Manter os dados consistentes ao listar livros após uma atualização ou remoção
