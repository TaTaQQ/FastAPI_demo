from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn

app = FastAPI()

books = [
    {
        "name": "The Lost Chronicles",
        "isbn": "978-1234567890",
        "type_": "Fiction",
        "publish": "2023-01-15",
        "price": 60.0,
        "id_": 1,
    },
    {
        "name": "A Journey to Knowledge",
        "isbn": "978-0987654321",
        "type_": "Fiction",
        "publish": "2022-05-20",
        "price": 199.0,
        "id_": 2,
    },
    {
        "name": "Exploring the Cosmos",
        "isbn": "978-5555555555",
        "type_": "Science",
        "publish": "2021-11-10",
        "price": 30.0,
        "id_": 3,
    },
    {
        "name": "Realm of Legends",
        "isbn": "978-7777777777",
        "type_": "Fantasy",
        "publish": "2023-03-25",
        "price": 90.0,
        "id_": 4,
    },
    {
        "name": "Secrets Unveiled",
        "isbn": "978-9999999999",
        "type_": "Mystery",
        "publish": "2022-08-12",
        "price": 39.0,
        "id_": 5,
    },
    {
        "name": "The Inspiring Lives",
        "isbn": "978-1111111111",
        "type_": "Biography",
        "publish": "2020-04-05",
        "price": 56.0,
        "id_": 6,
    },
    {
        "name": "test",
        "isbn": "adbsdfdf-12121",
        "type_": "Mystery",
        "publish": "2020-1-1",
        "price": 100.0,
        "id_": 7,
    },
    {
        "name": "test",
        "isbn": "aabbabc",
        "type_": "Biography",
        "publish": "2024-02-03",
        "price": 100.0,
        "id_": 8,
    },
]


@app.get("/api/books")
def get_books(type_: str | None = None, id_: int | None = None) -> list:
    result = books
    if type_:
        result = [book for book in books if book["type_"] == type_]
    if id_:
        result = [book for book in books if book["id_"] == id_]
    return result


@app.get("/api/books/{id_}")
def get_book_by_id(id_: int) -> dict:
    result = [book for book in books if book["id_"] == id_]
    if result:
        return result[0]
    raise HTTPException(status_code=404, detail=f"No book with id_={id_}")


if __name__ == "__main__":
    uvicorn.run("book:app", reload=True)
