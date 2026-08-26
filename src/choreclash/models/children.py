from choreclash.db.db import Base
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from choreclash.models.chore_assignment import ChoreAssignment
from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from choreclash.models.parent import Parent

class Child(Base):
    """
    ORM mapped Child class

    Primary key: id
    Name: string
    Has ForeignKey to Parent
    """

    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(back_populates="children")
    avatar_url: Mapped[Optional[str]] = mapped_column(String(30))
    chores: Mapped[List["ChoreAssignment"]] = relationship(cascade="all, delete", back_populates="child") # not a column, only for convenience

    def get_chores(self):
         """Return list of chores"""
         return self.chores

    def get_avatar_url(self):
         return self.avatar_url

    def get_name(self):
          return f"{self.first_name}"

    def get_id(self):
         return self.id

    def get_parent_id(self):
         return self.parent_id