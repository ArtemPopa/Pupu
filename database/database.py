from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker, Session
 
database_url = 'sqlite:///db.sqlite3'
engine = create_engine(url=database_url)
session_maker = sessionmaker(engine, class_=Session)


class Base(DeclarativeBase):
    pass
