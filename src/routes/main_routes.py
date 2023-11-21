from fastapi import APIRouter
from routes.agencia import agenciaRouter
from routes.funcionario import funcionarioRouter
from routes.dependente import dependenteRouter
mainRoutes = APIRouter()

mainRoutes.include_router(agenciaRouter, prefix="/agencia", tags=["agencia"])
mainRoutes.include_router(funcionarioRouter, prefix="/funcionario", tags=["funcionario"])
mainRoutes.include_router(dependenteRouter, prefix="/dependente", tags=["dependente"])