from fastapi import APIRouter
import bd
from models.agenciaModel import AgenciaModelPost
agenciaRouter = APIRouter()
import uuid

@agenciaRouter.get("/")
async def list_agencias():
    banco = bd.Bd()
    slq = f'SELECT * FROM Agencia'
    banco.cursor.execute(slq)
    return banco.cursor.fetchall()

@agenciaRouter.post("/")
async def createAgencia(agencia:AgenciaModelPost):
    banco = bd.Bd()
    slq = f"""INSERT INTO 
    `nullbank`.`Agencia` (`idAgencia`,`nome`, `salario_montante_total`, `cidade`) VALUES (
        {int(uuid.uuid4().int%10**7)},
        %(agencia)s,
        0.00,
        %(cidade)s);"""
    banco.cursor.execute(slq, {"agencia": agencia.nome, "cidade": agencia.cidade})
    banco.conexao.commit()
    return banco.cursor.fetchall()
    
