from fastapi import FastAPI

from app.config import settings
from app.services.doctors.routes import doctors_router

app = FastAPI(
    docs_url=settings.DOCS_URL,
)

app.include_router(doctors_router)
