from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
import bd
from models.dbaModel import DbaModel
from routes.auth import pegar_dados_usuarios

dbaRouter = APIRouter()
login_dependency = Annotated[dict, Depends(pegar_dados_usuarios)]


@dbaRouter.post("/")
async def executar_sql(dba: DbaModel, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        banco = bd.Bd()
        slq = dba.sql
        banco.cursor.execute(slq)
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")
