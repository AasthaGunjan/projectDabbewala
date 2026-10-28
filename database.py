from sqlmodel import SQLModel, create_engine, Session

# Database URL for SQLite
DATABASE_URL = "sqlite:///./projectdabbewala.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    """
    Provides a new database session"""
    with Session(engine) as session:
        yield session