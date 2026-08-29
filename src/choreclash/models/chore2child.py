from choreclash.db.db import Base
import choreclash.models as models
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from choreclash.models.children import Child
    from choreclash.models.chores import Chore
    from choreclash.models.chore_occurence import ChoreOccurence



class Chore2Child(Base):
    """
    Chore2Child model represents the assignment of a chore to a child.
    It contains foreign keys to both the Chore and Child models, and have relationshops with them both.

    child: Mapped["Child"] back-populates: chore_assignment
        - this allows for chore2Child.child to access the child object

    chore: Mapped["Chore"] back-populates: child_assignment
        - this allows for chore2child.chore to access the chore object

    occurences: Mapped[List[ChoreOccurence]] backpopulates: assignment
        - this allows for chore2child.occurences to access the occurrences object

    params:
        child: Child object
        chore: Chore object
        occurences: Occurences object
    """
    __tablename__ = "chore_2_child_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chore_id: Mapped[int] = mapped_column(ForeignKey("chores_table.id"))
    child_id: Mapped[int] = mapped_column(ForeignKey("child_table.id"))
    # Relationships allows to pass Objects directly insted of object.id
    child: Mapped["Child"] = relationship(back_populates="chore_assignments")
    chore: Mapped["Chore"] = relationship(back_populates="child_assignments")
    occurrences: Mapped[List["ChoreOccurence"]] = relationship(
        back_populates="assignment",
        cascade="all, delete"
    )