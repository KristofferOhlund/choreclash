from choreclash.db.db import Base
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from sqlalchemy import String, ForeignKey, Boolean, DateTime

from datetime import datetime 
from choreclash.models import Child

class Reward(Base):
    """
    Reward model represents the reward object being assigned to a child when chores are completed.

    Columns:
        id: int: the id of the record
        title: str: the title of the reward
        descritpion: str: the description of the reward
        reward_type: str: the reward_type of the reward
        icon: str: path to icon

        assignments: Mapped List[Reward2Child] populates: reward
        - this allows for access to the list of Reward2Child objects 
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

    Columns:
        child_id: int: ForeignKey to child_table
        reward_id: int: ForeignKey to reward_table
        
        child: Mapped["Child"] back-populates: reward_assignments
                - this allows for Reward2Child.child to access the child object
        
        reward: Mapped["Reward"] back-populates: assignments
            - this allows for Reward2Child.reward to access the reward object
        
        occurrences: Mapped["RewardOccurrence"] back-populates: assignment
            - this allows for Reward2Child.occurrences to access a list of RewardOccurence objects
"""
    __tablename__ = "reward_2_child_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    child_id: Mapped[int] = mapped_column(ForeignKey("child_table.id"))
    reward_id: Mapped[int] = mapped_column(ForeignKey("reward_table.id"))

    # Relationships allows to pass Objects directly insted of object.id
    child: Mapped["Child"] = relationship(back_populates="reward_assignments")

    reward: Mapped["Reward"] = relationship(back_populates="assignments")

    occurrences: Mapped[List["RewardOccurrence"]] = relationship(
        back_populates="assignment",
        cascade="all, delete-orphan"
    )

class RewardOccurrence(Base):
    """
    RewardOccurencerence model represents a specific occurrence of a reward assigned to a child.
    It includes details such as the date of the occurrence, status such as used, unused and the associated reward assignment.

    Columns:
        reward_2_child_id: int : foreignkey to reward_2_child table
        used: bool, False default
        used_at: datetime.datime: this is set when used is changed, using the @validates decorator
        assigned_at: datetime, defaults date.today

        assignment: Mapped["Reward2Child"] backpopulates occurrences
            - this gives access to the Reward2Child object
    """
    
    __tablename__ = "reward_occurrence_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    reward_2_child_id: Mapped[int] = mapped_column(ForeignKey("reward_2_child_table.id"))
    used: Mapped[bool] = mapped_column(Boolean, default=False)
    used_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    assigned_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.today)

    assignment: Mapped["Reward2Child"] = relationship(back_populates="occurrences")

    @validates("used")
    def set_used_at(self, key, value):
        """Triggers when value of used is changed"""
        if value is True:
            self.used_at = datetime.today()
        else:
            self.used_at = None
        
        return value