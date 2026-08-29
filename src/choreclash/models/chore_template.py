from choreclash.db.db import Base
from sqlalchemy.orm import Mapped, mapped_column, Relationship
from sqlalchemy import String, ForeignKey
from typing import Optional
from datetime import datetime
from choreclash.models.parent import Parent

class ChoreTemplate(Base):
    """
    ORM mapped Parent class

    Primary key: id
    title: string
    avatar_url: str
    is_complete: bool
    owner: ForeignKey child
    time_for_chore: str
    """

    __tablename__ = "chore_template_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("parent_table.id"), nullable=True)
    parent: Mapped["Parent"] = Relationship()
    title: Mapped[str] = mapped_column(String(30), unique=True)
    icon: Mapped[Optional[str]] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(100))
    is_complete: Mapped[bool] = mapped_column(default=False)
    deadline: Mapped[Optional[datetime]] = mapped_column()