import uuid
from fastapi import APIRouter
import bd
from models.dependenteModel import DependenteModelDelete, DependenteModelPost, DependenteModelPut
from datetime import datetime
from enum import Enum

dependenteRouter = APIRouter()


@dependenteRouter.get("/")
async def list_Dependente():
    banco = bd.Bd()
    slq = f'SELECT * FROM Dependente'
    banco.cursor.execute(slq)
    return banco.cursor.fetchall()


@dependenteRouter.get("/{id}")
async def ler_dependente(id: str):
    banco = bd.Bd()
    slq = """SELECT * FROM `nullbank`.`Dependente`
    WHERE
        `idDependente` = %(id_dependente)s;"""
    banco.cursor.execute(slq, {"id_dependente": id})
    return banco.cursor.fetchall()


@dependenteRouter.post("/")
async def createDependente(dependente: DependenteModelPost):
    dependente.data_nascimento = datetime.strptime(
        dependente.data_nascimento, "%Y-%m-%d %H:%M:%S")
    banco = bd.Bd()
    slq = f"""INSERT INTO `nullbank`.`Dependente` (
  `idDependente`,
  `nome_completo`,
  `data_nascimento_dependente`,
  `parentesco`,
  `Funcionario_idFuncionario`
) VALUES (
   {int(uuid.uuid4().int%10**7)},
  %(nome)s,
  %(data_nascimento)s,       
  %(parentesco)s,       
  %(id_funcionario)s                   
);
"""
    banco.cursor.execute(
        slq, {"nome": dependente.nome, "data_nascimento": dependente.data_nascimento, "parentesco": dependente.parentesco.value, "id_funcionario": dependente.id_funcionario})
    banco.conexao.commit()
    return banco.cursor.fetchall()


@dependenteRouter.put("/")
async def modificarDependente(dependente: DependenteModelPut):
    banco = bd.Bd()
    slq = f"""UPDATE `nullbank`.`Dependente`
        SET `nome_completo` = %(nome)s
        WHERE `idDependente` = %(id_dependente)s ;
        """
    banco.cursor.execute(
        slq, {"nome": dependente.nome, "id_dependente": dependente.id})
    banco.conexao.commit()
    return banco.cursor.fetchall()


@dependenteRouter.delete("/")
async def deletarFuncionario(dependente: DependenteModelDelete):
    banco = bd.Bd()
    slq = f"""DELETE FROM `nullbank`.`Dependente`
            WHERE
             `idDependente` = %(id_dependente)s; 
            """
    banco.cursor.execute(slq, {"id_dependente": dependente.id})
    banco.conexao.commit()
    return banco.cursor.fetchall()
