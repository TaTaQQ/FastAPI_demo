from sqlmodel import SQLModel, Field, Relationship, Column, VARCHAR

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


class BookInput(SQLModel):
    name: str
    isbn: str
    type_: str
    publish: str
    price: float

    class Config:
        json_schema_extra = {
            "example": {
                "name": "The Book Name",
                "isbn": "abcd-1234",
                "type_": "Fiction",
                "publish": "2024-02-20",
                "price": 120,
            }
        }


class Book(BookInput, table=True):
    id_: int | None = Field(primary_key=True, default=None)
    auth_id: int = Field(foreign_key="author.id_")
    author: "Author" = Relationship(back_populates="books")


class AuthorInput(SQLModel):
    name: str
    nationality: str


class AuthorOutput(AuthorInput):
    id_: int
    books: list[Book] = []


class Author(AuthorInput, table=True):
    id_: int | None = Field(primary_key=True, default=None)
    books: list[Book] = Relationship(back_populates="author")


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(
        sa_column=Column("username", VARCHAR, unique=True, index=True)
    )
    password_hash: str = ""

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class UserOutput(SQLModel):
    id: int
    username: str
