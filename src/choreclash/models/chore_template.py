from choreclash.db.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from typing import Optional
from datetime import datetime

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
    title: Mapped[str] = mapped_column(String(30), unique=True)
    icon: Mapped[Optional[str]] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(100))
    is_complete: Mapped[bool] = mapped_column(default=False)
    deadline: Mapped[Optional[datetime]] = mapped_column()

    def get_id(self):
        return self.id

    def get_parent_id(self):
        return self.parent_id

    def get_title(self):
        return self.title

    def get_icon(self):
        return self.icon

    def get_description(self):
        return self.description

    def get_is_complete(self):
        return self.is_complete

    def get_deadline(self):
        return self.deadline