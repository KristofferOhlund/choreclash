from choreclash.db.db import Base
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from choreclash.models.chores import Chore

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
    last_name: Mapped[str] = mapped_column(String(30))
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    chores: Mapped[List["Chore"]] = relationship(cascade="all, delete")

    def get_chores(self):
         """Return list of chores"""
         return self.chores

    def get_fullname(self):
          return f"{self.first_name} + {self.last_name}"

    def __repr__(self) -> str:
         return f"Kid(id={self.id!r}, firstname={self.first_name!r}, \
              lastname={self.last_name!r}), chores={self.chores!r})"