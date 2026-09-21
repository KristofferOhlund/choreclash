from choreclash.db.db import Base
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from datetime import datetime as date_type # to avoid sqlalchemy date

class Reward(Base):
    __tablename__ = "reward_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    descritpion: Mapped[str] = mapped_column(String(100))
    reward_type: Mapped[str] = mapped_column(String(20))
    icon: Mapped[str] = mapped_column(String(30), default="default_icon.png")

class Reward2Child(Base):
    """
    Reward2Child model represents the assignment of a reward to a child.
    It contains foreign keys to Child model.

    child: Mapped["Child"] back-populates: chore_assignment
        - this allows for chore2Child.child to access the child object

    params:
        child: Child object
        chore: Chore object
        occurences: Occurences object
    """
    __tablename__ = "reward_2_child_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    child_id: Mapped[int] = mapped_column(ForeignKey("child_table.id"))
    reward_id: Mapped[int] = mapped_column(ForeignKey("reward_table.id"))
    
    # Relationships allows to pass Objects directly insted of object.id
    occurrences: Mapped[List["RewardOccurence"]] = relationship(
        back_populates="reward",
        cascade="all, delete"
    )

class RewardOccurence(Base):
    """
    ChoreOccuRewardOccurencerence model represents a specific occurrence of a reward assigned to a child.
    It includes details such as the date of the occurrence, status such as used, unused,
    and the associated reward assignment.

    used: bool, False default
    date: Optional|datetime, defaults datetime.today
    """
    
    __tablename__ = "reward_occurrence_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    reward_2_child_id: Mapped[int] = mapped_column(ForeignKey("reward_2_child_table.id"))
    used: Mapped[bool] = mapped_column(default=False)
    date: Mapped[Optional[date_type]] = mapped_column(default=date_type.today)
    reward: Mapped["Reward2Child"] = relationship(back_populates="occurrences")