from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete
from database.database import session_maker


class BaseDAO:
    model = None

    @classmethod
    def update(cls, value):
        with session_maker() as session:
            session.execute(sqlalchemy_update(cls.model).where(cls.model.best_score == value))

    @classmethod
    def find_one_or_none(cls, **filter_by):
        with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    def find_all_or_none(cls, **filter_by):
        with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = session.execute(query)
            if result:
                return result.scalars().all()
            return None

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
    

