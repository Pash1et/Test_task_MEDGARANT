from datetime import time

from pydantic import BaseModel


class SDoctor(BaseModel):
    id: int
    first_name: str
    last_name: str
    specialization: str
    busy_time: list[dict[str, time]]


class SFreeTime(BaseModel):
    id_doctor: int
    free_time: list[dict[str, time]]
