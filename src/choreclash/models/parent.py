from choreclash.db.db import Base
from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from choreclash.models.children import Child


class Parent(Base):
    """
    ORM mapped Parent class

    Primary key: id
    first_name: str
    last_name: str
    email: str
    password_hash: bcrypt hash
    created_at: datetime
    children: List of Child objects
    """

    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    avatar_url: Mapped[Optional[str]] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))
    password_hash: Mapped[Optional[str]] = mapped_column(String(30))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    children: Mapped[Optional[List["Child"]]] = relationship(cascade="all, delete") # not a column, only for convenience