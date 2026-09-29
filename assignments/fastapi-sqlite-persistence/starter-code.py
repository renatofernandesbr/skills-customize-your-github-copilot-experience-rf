import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Library API with SQLite")
DATABASE_PATH = Path(__file__).with_name("books.db")


class Book(BaseModel):
    title: str
    author: str
    year: int


class BookWithId(Book):
    id: int


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with closing(get_connection()) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
            """
        )
        connection.commit()


initialize_database()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books")
def list_books():
    with closing(get_connection()) as connection:
        # TODO: Select all books, ordered by ID, and return them as dictionaries.
        return []


@app.get("/books/{book_id}")
def get_book(book_id: int):
    with closing(get_connection()) as connection:
        # TODO: Select the book by ID and raise HTTP 404 if it does not exist.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    with closing(get_connection()) as connection:
        # TODO: Insert the book with SQL parameters, commit, and return it with its ID.
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Not implemented",
        )


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    with closing(get_connection()) as connection:
        # TODO: Update the book, commit, and return HTTP 404 if the ID is missing.
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Not implemented",
        )


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    with closing(get_connection()) as connection:
        # TODO: Delete the book, commit, and return HTTP 404 if the ID is missing.
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Not implemented",
        )