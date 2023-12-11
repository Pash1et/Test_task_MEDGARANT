from typing import Annotated

from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_async_session
from app.services.doctors import db_handlers as db_hand
from app.services.doctors import schemas as sh
from app.services.doctors import utils as ut


async def get_all_doctors(
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    doctors = await db_hand.get_all_doctors(session)
    return doctors


async def get_free_time(
    id_doctor: int,
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    doctor = await db_hand.get_doctor_by_id(session, id_doctor)
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Доктор не найден."
        )
    free_time: list = await ut.get_free_time(busy_time=doctor.busy_time)
    data = {"id_doctor": doctor.id, "free_time": free_time}
    try:
        validate_data = sh.SFreeTime.model_validate(data)
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Внутреняя ошибка сервиса.",
        ) from e
    return validate_data
