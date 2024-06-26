from sqlmodel import create_engine, Session


engine = create_engine(
    "sqlite:///book.db", connect_args={"check_same_thread": False}, echo=True
)


def get_session():
    with Session(engine) as session:
        yield session
