from choreclash.db.db import Base
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from choreclash.models.parent import Parent
     from choreclash.models.chore2child import Chore2Child

class Child(Base):
    """
    __tablename__ = 'child_table'
    first_name: str
    parent_id: int
    avatar_url: str
    chore_assignments: List of Chore2Child objects
    """

    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(back_populates="children")
    avatar_url: Mapped[str] = mapped_column(String(30), default="default.png")
    chore_assignments: Mapped[List["Chore2Child"]] = relationship(back_populates="child",cascade="all, delete") # not a column, only for convenience