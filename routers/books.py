from fastapi import HTTPException
from fastapi import Depends
from sqlmodel import Session, select
from fastapi import APIRouter

from db import get_session
from schema import BookInput, Book, User
from routers.auth import get_current_user

router = APIRouter(prefix="/api/books")


@router.get("/")
def get_books(
    type_: str | None = None,
    id_: int | None = None,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
) -> list[Book]:
    query = select(Book)
    if type_:
        query = query.where(Book.type_ == type_)
    if id_:
        query = query.where(Book.id_ == id_)
    return session.exec(query).all()


@router.get("/{id_}")
def get_book_by_id(id_: int, session: Session = Depends(get_session)) -> Book:
    book = session.get(Book, id_)
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail=f"No book with id_={id_}")


@router.delete("/{id_}", status_code=204)
def delete_book(id_: int, session: Session = Depends(get_session)):
    book = session.get(Book, id_)
    if book:
        session.delete(book)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No book with id_={id_}")


@router.put("/{id_}")
def update_book(
    id_: int, new_book: BookInput, session: Session = Depends(get_session)
) -> Book:
    book = session.get(Book, id_)
    if book:
        book.name = new_book.name
        book.isbn = new_book.isbn
        book.type_ = new_book.type_
        book.publish = new_book.publish
        book.price = new_book.price
        session.commit()
        return book
    else:
        raise HTTPException(status_code=404, detail=f"No book with id_={id_}")
