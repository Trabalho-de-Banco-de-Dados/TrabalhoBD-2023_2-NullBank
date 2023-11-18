from fastapi import APIRouter
from routes.agencia import agenciaRouter

mainRoutes = APIRouter()

mainRoutes.include_router(agenciaRouter, prefix="/agencia", tags=["agencia"])
