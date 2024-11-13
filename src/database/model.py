
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import enum 
from datetime import datetime
from sqlalchemy import String, func 

class Base(DeclarativeBase):
    create_time: datetime = mapped_column(func.now)
    edit_time: datetime = mapped_column(func.now)


class Rate(enum.Enum):
    pass

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(16))
    rate: Mapped[Rate] = relationship()