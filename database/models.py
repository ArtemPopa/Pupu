from sqlalchemy import Integer, Text
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base

class User(Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(Text, primary_key=True, nullable=False)
    best_score: Mapped[int] = mapped_column(Integer, default=0)