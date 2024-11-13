from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


engine = create_engine(url='sqlite:///db.sqlite3')

session_maker = sessionmaker(engine)

class Databaser():
    @classmethod
    def add(cls, **values):
        with session_maker() as session:
            with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                try:
                    session.commit()
                except SQLAlchemyError as e:
                    session.rollback()
                    raise e
                return new_instance