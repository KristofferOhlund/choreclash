from choreclash.db.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from typing import Optional
from datetime import datetime

class ChoreAssignment(Base):
    """
    ChoreAssignment model represents the assignment of a chore to a child.
    It includes details such as the chore's title, description, completion status,
    and the child to whom it is assigned.
    """
    __tablename__ = "chore_assignment_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chore_template_id: Mapped[int] = mapped_column(ForeignKey("chore_template_table.id"))
    child_id: Mapped[int] = mapped_column(ForeignKey("child_table.id"))

    def get_id(self):
        return self.id

    def get_chore_template_id(self):
        return self.chore_template_id

    def get_child_id(self):
        return self.child_id