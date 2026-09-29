# 📘 Assignment: Persistência de Dados com SQLite e FastAPI

## 🎯 Objective

Atualize uma API de livros em FastAPI para armazenar os dados em SQLite em vez de mantê-los apenas na memória. Pratique consultas SQL parametrizadas e verifique que os registros continuam disponíveis depois que o servidor reiniciar.

## 📝 Tasks

### 🛠️ Consultar livros no banco de dados

#### Descrição
Complete as rotas de leitura para buscar livros na tabela `books` criada pelo starter code.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` com uma consulta `SELECT` que retorne todos os livros
- Implementar `GET /books/{book_id}` para buscar um livro pelo ID
- Retornar o status HTTP `404` quando o ID solicitado não existir
- Converter os resultados do SQLite em dados que a API possa retornar como JSON

### 🛠️ Implementar operações CRUD com SQLite

#### Descrição
Substitua o armazenamento em memória por comandos SQL para criar, atualizar e remover livros. Use os IDs gerados pelo banco para identificar cada registro.

#### Requisitos
O programa concluído deve:

- Criar livros com `POST /books` e retornar o status HTTP `201` e o livro criado com seu ID
- Atualizar livros com `PUT /books/{book_id}` e retornar o registro atualizado
- Remover livros com `DELETE /books/{book_id}`
- Retornar o status HTTP `404` ao atualizar ou remover um ID inexistente
- Usar parâmetros `?` nas consultas SQL para inserir valores fornecidos pelo usuário

### 🛠️ Verificar a persistência dos dados

#### Descrição
Teste o ciclo completo da API e confirme que os livros são mantidos no arquivo `books.db` após o servidor ser encerrado e iniciado novamente.

#### Requisitos
O programa concluído deve:

- Criar um livro e consultar seus dados por ID
- Atualizar e remover um livro, confirmando cada resultado por meio da API
- Reiniciar o servidor e confirmar que um livro não removido continua disponível
- Manter a tabela e os registros existentes quando a aplicação for iniciada novamente