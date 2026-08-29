from choreclash.db.db import Base
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from choreclash.models.chore2child import Chore2Child

class Chore(Base):
    """
    ORM mapped Chore class

    Primary key: id
    title: string
    description: string
    avatar_url: str
    """

    __tablename__ = "chores_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(30), unique=True)
    icon: Mapped[str] = mapped_column(String(30), default="default_icon.png")
    description: Mapped[Optional[str]] = mapped_column(String(100))
    child_assignments: Mapped[List["Chore2Child"]] = relationship(back_populates="chore", cascade="all, delete") # not a column, only for convenience