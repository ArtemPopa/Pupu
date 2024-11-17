from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from database.dao.base import BaseDAO
from database.models import User
from database.database import session_maker

class UserDAO(BaseDAO):
    model = User