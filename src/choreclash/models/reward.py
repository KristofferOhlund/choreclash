from choreclash.db.db import Base
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Boolean, DateTime
from datetime import datetime 
from choreclash.models import Child

class Reward(Base):
    """
    Args:
        title: str
        descirpiton: str
        reward_type: str: weekly | daily
        icon: str | path
    """
    __tablename__ = "reward_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100))
    reward_type: Mapped[str] = mapped_column(String(20))
    icon: Mapped[str] = mapped_column(String(30), default="default_icon.png")
    
    # Reward is assigned to child
    assignments: Mapped[List["Reward2Child"]] = relationship(
        back_populates="reward",
        cascade="all, delete-orphan"
    )

class Reward2Child(Base):
    """
    Reward2Child model represents the assignment of a reward to a child.
    It contains foreign keys to Child model.

    child: Mapped["Child"] back-populates: chore_assignment
        - this allows for chore2Child.child to access the child object

    params:
        child_id: int: ForeignKey to child_table
        reward_id: int: ForeignKey to reward_table
    """
    __tablename__ = "reward_2_child_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    child_id: Mapped[int] = mapped_column(ForeignKey("child_table.id"))
    reward_id: Mapped[int] = mapped_column(ForeignKey("reward_table.id"))

    # Relationships allows to pass Objects directly insted of object.id
    child: Mapped[List["Child"]] = relationship(back_populates="reward_assignments")

    reward: Mapped[List["Reward"]] = relationship(back_populates="assignments")

    occurrences: Mapped[List["RewardOccurrence"]] = relationship(
        back_populates="assignment",
        cascade="all, delete-orphan"
    )

class RewardOccurrence(Base):
    """
    ChoreOccuRewardOccurencerence model represents a specific occurrence of a reward assigned to a child.
    It includes details such as the date of the occurrence, status such as used, unused,
    and the associated reward assignment.

    Params:
        reward_2_child_id: int : foreignkey to reward_2_child table
        used: bool, False default
        date: datetime, defaults date.today
    """
    
    __tablename__ = "reward_occurrence_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    reward_2_child_id: Mapped[int] = mapped_column(ForeignKey("reward_2_child_table.id"))
    used: Mapped[bool] = mapped_column(Boolean, default=False)
    used_at: Mapped[datetime] = mapped_column(DateTime)
    assigned_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.today)

    assignment: Mapped["Reward2Child"] = relationship(back_populates="occurrences")