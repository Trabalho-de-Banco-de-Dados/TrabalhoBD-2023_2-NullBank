from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, HTTPException
import bd
from models.agenciaModel import AgenciaModelPost, AgenciaModelPut, AgenciaModelDelete
from routes.auth import pegar_dados_usuarios
agenciaRouter = APIRouter()
login_dependency = Annotated[dict, Depends(pegar_dados_usuarios)]


@agenciaRouter.get("/")
async def list_agencias():
    banco = bd.Bd()
    slq = f'SELECT * FROM Agencia'
    banco.cursor.execute(slq)
    return banco.cursor.fetchall()


@agenciaRouter.get("/{id}")
async def ler_agencia(id: str):
    banco = bd.Bd()
    slq = """SELECT * FROM `nullbank`.`Agencia`
    WHERE
        `idAgencia` = %(id_agencia)s;"""
    banco.cursor.execute(slq, {"id_agencia": id})
    return banco.cursor.fetchall()


@agenciaRouter.post("/")
async def createAgencia(agencia: AgenciaModelPost, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        banco = bd.Bd()
        slq = f"""INSERT INTO 
        `nullbank`.`Agencia` (`idAgencia`,`nome`, `salario_montante_total`, `cidade`) VALUES (
            {int(uuid.uuid4().int%10**7)},
            %(agencia)s,
            0.00,
            %(cidade)s);"""
        banco.cursor.execute(
            slq, {"agencia": agencia.nome, "cidade": agencia.cidade})
        banco.conexao.commit()
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")


@agenciaRouter.put("/")
async def modificarAgencia(agencia: AgenciaModelPut, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        banco = bd.Bd()
        slq = f"""UPDATE `nullbank`.`Agencia`
        SET
            `nome` = %(agencia)s,
            `cidade` = %(cidade)s
        WHERE
            `idAgencia` = %(id_agencia)s;"""
        banco.cursor.execute(slq, {"agencia": agencia.nome,
                                   "cidade": agencia.cidade,
                                   "id_agencia": agencia.id})
        banco.conexao.commit()
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")


@agenciaRouter.delete("/")
async def deletarAgencia(agencia: AgenciaModelDelete, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'CAIXA':
        banco = bd.Bd()
        slq = f"""DELETE FROM `nullbank`.`Agencia`
        WHERE
            `idAgencia` = %(id_agencia)s;"""
        banco.cursor.execute(slq, {"id_agencia": agencia.id})
        banco.conexao.commit()
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")
