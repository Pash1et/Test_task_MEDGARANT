from datetime import time

from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Doctors(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    specialization: Mapped[str] = mapped_column(nullable=False)
    busy_time: Mapped[list[dict[str, time]]] = mapped_column(
        JSON,
        nullable=False,
    )
