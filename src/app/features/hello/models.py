from __future__ import annotations

from datetime import datetime
from typing import AsyncSequence

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base import Base


class Greeting(Base):
    __tablename__ = "greetings"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    message: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=Base.now)
