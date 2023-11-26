from fastapi import APIRouter
from routes.agencia import agenciaRouter
from routes.funcionario import funcionarioRouter
from routes.dependente import dependenteRouter
from routes.cliente import clienteRouter
from routes.auth import router as authRouter
from routes.conta import contaRouter
from routes.transacao import transacaoRouter
from routes.dba import dbaRouter
mainRoutes = APIRouter()

mainRoutes.include_router(agenciaRouter, prefix="/agencia", tags=["agencia"])
mainRoutes.include_router(
    funcionarioRouter, prefix="/funcionario", tags=["funcionario"])
mainRoutes.include_router(
    dependenteRouter, prefix="/dependente", tags=["dependente"])
mainRoutes.include_router(clienteRouter, prefix="/cliente", tags=["cliente"])
mainRoutes.include_router(authRouter, prefix="/auth", tags=["auth"])
mainRoutes.include_router(contaRouter, prefix="/conta", tags=["conta"])
mainRoutes.include_router(
    transacaoRouter, prefix="/transacao", tags=["transacao"])
mainRoutes.include_router(dbaRouter, prefix="/dba", tags=["DBA"])
