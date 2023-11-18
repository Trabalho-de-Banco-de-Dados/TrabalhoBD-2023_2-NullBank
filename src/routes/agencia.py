import uuid
from fastapi import APIRouter
import bd
from models.agenciaModel import AgenciaModelPost, AgenciaModelPut, AgenciaModelDelete
agenciaRouter = APIRouter()


@agenciaRouter.get("/")
async def list_agencias():
    banco = bd.Bd()
    slq = f'SELECT * FROM Agencia'
    banco.cursor.execute(slq)
    return banco.cursor.fetchall()

@agenciaRouter.get("/{id}")
async def ler_agencia(id:str):
    banco = bd.Bd()
    slq = """SELECT * FROM `nullbank`.`Agencia`
    WHERE
        `idAgencia` = %(id_agencia)s;"""
    banco.cursor.execute(slq, {"id_agencia": id})
    return banco.cursor.fetchall()

@agenciaRouter.post("/")
async def createAgencia(agencia: AgenciaModelPost):
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


@agenciaRouter.put("/")
async def modificarAgencia(agencia: AgenciaModelPut):
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


@agenciaRouter.delete("/")
async def deletarAgencia(agencia: AgenciaModelDelete):
    banco = bd.Bd()
    slq = f"""DELETE FROM `nullbank`.`Agencia`
    WHERE
        `idAgencia` = %(id_agencia)s;"""
    banco.cursor.execute(slq, {"id_agencia": agencia.id})
    banco.conexao.commit()
    return banco.cursor.fetchall()
