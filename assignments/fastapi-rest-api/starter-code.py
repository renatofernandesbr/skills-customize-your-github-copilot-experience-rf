from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Library API")


class Book(BaseModel):
    title: str
    author: str
    year: int


class BookWithId(Book):
    id: int


books: dict[int, BookWithId] = {}
next_book_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books")
def list_books():
    # TODO: Return all books.
    return []


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find the book and return HTTP 404 if it does not exist.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    # TODO: Assign a unique ID, store the book, and return it.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    # TODO: Replace the existing book data or return HTTP 404.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Remove the book or return HTTP 404.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")
