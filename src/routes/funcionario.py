from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, HTTPException
import bd
from models.funcionarioModel import FuncionarioModelPost, FuncionarioModelPut, FuncionarioModelDelete
from datetime import datetime
from enum import Enum
from passlib.context import CryptContext
from routes.auth import pegar_dados_usuarios


funcionarioRouter = APIRouter()
login_dependency = Annotated[dict, Depends(pegar_dados_usuarios)]


@funcionarioRouter.get("/")
async def list_funcionario(usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        print(usuario)  # VEM DO JWT
        banco = bd.Bd()
        slq = f'SELECT idFuncionario, matricula, nome_completo, endereco, cidade, cargo, sexo, data_nascimento_funcionario, salario, Agencia_idAgencia, num_dependentes FROM Funcionario'
        banco.cursor.execute(slq)
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")



@funcionarioRouter.get("/{id}")
async def ler_funcionario(id: str, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        banco = bd.Bd()
        slq = """SELECT * FROM `nullbank`.`Funcionario`
        WHERE
            `idFuncionario` = %(id_funcionario)s;"""
        banco.cursor.execute(slq, {"id_funcionario": id})
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")


@funcionarioRouter.post("/")
async def createFuncionario(funcionario: FuncionarioModelPost, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        funcionario.data_nascimento = datetime.strptime(
            funcionario.data_nascimento, "%Y-%m-%d %H:%M:%S")
        banco = bd.Bd()
        bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        slq = f"""INSERT INTO `nullbank`.`Funcionario` (
    `idFuncionario`,
    `matricula`,
    `nome_completo`,
    `senha`,
    `endereco`,
    `cidade`,
    `cargo`,
    `sexo`,
    `data_nascimento_funcionario`,
    `salario`,
    `Agencia_idAgencia`,
    `num_dependentes`
    ) VALUES (
    {int(uuid.uuid4().int%10**7)},
    %(matricula)s,
    %(nome)s,
    %(senha)s,
    %(endereco)s,
    %(cidade)s,
    %(cargo)s,  
    %(sexo)s,  
    %(data_nascimento)s,  
    %(salario)s, 
    %(agencia)s,  
    %(num_dependentes)s 
    );
    """
        banco.cursor.execute(
            slq, {"matricula": funcionario.matricula, "nome": funcionario.nome,
                "senha": bcrypt_context.hash(funcionario.senha),
                "endereco": funcionario.endereco, "cidade": funcionario.cidade, "cargo": funcionario.cargo.value, "sexo": funcionario.sexo.value, "data_nascimento": funcionario.data_nascimento, "salario": funcionario.salario, "agencia": funcionario.Agencia, "num_dependentes": funcionario.num_dependentes})
        banco.conexao.commit()
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")



@funcionarioRouter.put("/")
async def modificarFuncionario(funcionario: FuncionarioModelPut, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        banco = bd.Bd()
        slq = f"""UPDATE `nullbank`.`Funcionario`
                SET
                    `nome_completo` = %(nome)s,
                    `endereco` = %(endereco)s,
                    `cidade` = %(cidade)s,
                    `cargo` = %(cargo)s, 
                    `salario` = %(salario)s,  
                    `num_dependentes` =  %(num_dependentes)s
                WHERE
                    `idFuncionario` =  %(id_funcionario)s; 
                """
        banco.cursor.execute(slq, {"id_funcionario": funcionario.id, "nome": funcionario.nome, "endereco": funcionario.endereco, "cidade": funcionario.cidade,
                            "cargo": funcionario.cargo.value, "salario": funcionario.salario, "num_dependentes": funcionario.num_dependentes})
        banco.conexao.commit()
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")



@funcionarioRouter.delete("/")
async def deletarFuncionario(funcionario: FuncionarioModelDelete, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        banco = bd.Bd()
        slq = f"""DELETE FROM `nullbank`.`Funcionario`
                WHERE
                `idFuncionario` = %(id_funcionario)s; 
                """
        banco.cursor.execute(slq, {"id_funcionario": funcionario.id})
        banco.conexao.commit()
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")
