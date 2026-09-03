from choreclash.db.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from choreclash.models.parent import Child
    from choreclash.models.chore_template import ChoreTemplate
    from choreclash.models.chore2child import Chore2Child

class ChoreOccurence(Base):
    """
    ChoreOccurence model represents a specific occurrence of a chore assigned to a child.
    It includes details such as the date of the occurrence, completion status,
    and the associated chore assignment.

    is_complete: bool, False default
    date: Optional|datetime, defaults datetime.today
    assignment: Chore2Child object
    """
    
    __tablename__ = "chore_occurrence_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chore_2_child_id: Mapped[int] = mapped_column(ForeignKey("chore_2_child_table.id"))
    is_complete: Mapped[bool] = mapped_column(default=False)
    date: Mapped[Optional[datetime]] = mapped_column(default=datetime.today)
    assignment: Mapped["Chore2Child"] = relationship(back_populates="occurrences")
