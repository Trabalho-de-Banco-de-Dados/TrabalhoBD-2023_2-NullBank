from fastapi import APIRouter
from routes.agencia import agenciaRouter
from routes.funcionario import funcionarioRouter

mainRoutes = APIRouter()

mainRoutes.include_router(agenciaRouter, prefix="/agencia", tags=["agencia"])
mainRoutes.include_router(funcionarioRouter, prefix="/funcionario", tags=["funcionario"])