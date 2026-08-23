from db.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey

CHORE_TIME = ["morning", "evening", "bedtime"]

class Chore(Base):
    """
    ORM mapped Parent class

    Primary key: id
    title: string
    avatar_url: str
    is_complete: bool
    owner: ForeignKey child
    time_for_chore: str
    """

    __tablename__ = "chore_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(30))
    avatar_url: Mapped[str] = mapped_column(String(30))
    is_complete: Mapped[bool] = mapped_column(default=False)
    assigned_to: Mapped[int] = mapped_column(ForeignKey("child_table.id"))
    time_for_chore: Mapped[str] = mapped_column(default=CHORE_TIME[0])

    def get_title(self):
        """return chore title"""
        return self.title

    def get_avatar_url(self):
        return self.avatar_url

    def get_assigned_to(self):
        """return who the chore is assigend to"""
        return self.assigned_to

    def get_chore_time(self):
        """return the time a chore belong to"""
        return self.time_for_chore

    def mark_complete(self):
        """mark chore complete"""
        self.is_complete = True

    def mark_incomplete(self):
        """mark chore incomplete"""
        self.is_complete = False

    def is_chore_complete(self):
        return self.is_complete

    def __repr__(self) -> str:
         return f"Chore(id={self.id!r}, title={self.title!r}, \
              avatar_url={self.avatar_url!r}), is_complete={self.is_complete!r}) \
               owner={self.owner!r}"