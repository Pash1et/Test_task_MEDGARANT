from fastapi import APIRouter

from app.services.doctors import schemas as sh
from app.services.doctors import views

doctors_router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"],
)

doctors_router.add_api_route(
    path="/",
    endpoint=views.get_all_doctors,
    response_model=list[sh.SDoctor],
    description="Получение всех врачей.",
)
doctors_router.add_api_route(
    path="/{id_doctor}/free_time",
    endpoint=views.get_free_time,
    response_model=sh.SFreeTime,
    description="Получение списка свободных окон.",
)
