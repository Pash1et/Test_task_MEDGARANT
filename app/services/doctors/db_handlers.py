from typing import Sequence

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.doctors.models import Doctors


async def get_all_doctors(session: AsyncSession) -> Sequence[Doctors]:
    stmt = sa.select(Doctors)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_doctor_by_id(session: AsyncSession, id_doctor: int) -> Doctors | None:
    stmt = sa.select(Doctors).where(Doctors.id == id_doctor)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()
