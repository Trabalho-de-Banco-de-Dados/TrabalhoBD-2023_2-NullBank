from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, HTTPException
import bd
from models.contaModel import ContaModelPost, ContaModelPut
from datetime import datetime
from enum import Enum
from passlib.context import CryptContext
from routes.auth import pegar_dados_usuarios

contaRouter = APIRouter()
login_dependency = Annotated[dict, Depends(pegar_dados_usuarios)]


@contaRouter.get("/")
async def list_conta():
    banco = bd.Bd()
    slq = f"""SELECT numero_conta, saldo, tipo_conta, Cliente_cpf, Gerente_idFuncionario, Agencia_idAgencia FROM ContaBancaria"""
    banco.cursor.execute(slq)
    return banco.cursor.fetchall()


@contaRouter.get("/{numero_conta}")
async def ler_conta(numero_conta: str, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'CLIENTE' and usuario['usuario_id'] == numero_conta or usuario['tipo_usuario'] in ['DBA', 'ATENDENTE']:
        banco = bd.Bd()
        slq = """SELECT numero_conta, saldo, tipo_conta, Cliente_cpf, Gerente_idFuncionario, Agencia_idAgencia FROM `nullbank`.`ContaBancaria`
        WHERE
            `numero_conta` = %(numero_conta)s;"""
        banco.cursor.execute(slq, {"numero_conta": numero_conta})
        return banco.cursor.fetchall()
    elif usuario['tipo_usuario'] == 'GERENTE':
        banco = bd.Bd()
        slq = """SELECT f.matricula
            FROM `nullbank`.`Funcionario` f
            JOIN ContaBancaria c ON f.idFuncionario = c.Gerente_idFuncionario
            WHERE c.numero_conta = %(numero_conta)s"""
        banco.cursor.execute(slq, {"numero_conta": numero_conta})
        if str(banco.cursor.fetchall()[0][0]) == usuario['usuario_id']:
            slq = """SELECT numero_conta, saldo, tipo_conta, Cliente_cpf, Gerente_idFuncionario, Agencia_idAgencia FROM `nullbank`.`ContaBancaria`
            WHERE
                `numero_conta` = %(numero_conta)s;"""
            banco.cursor.execute(slq, {"numero_conta": numero_conta})
            result = banco.cursor.fetchall()
            return result
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")


@contaRouter.post("/")
async def createConta(conta: ContaModelPost, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        numero_conta = int(uuid.uuid4().int % 10**7)
        banco = bd.Bd()
        bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        slq = f"""INSERT INTO ContaBancaria (numero_conta, saldo, senha, tipo_conta, Cliente_cpf, Gerente_idFuncionario, Agencia_idAgencia)
        VALUES (
            {numero_conta}, 
            %(saldo)s, 
            %(senha)s, 
            %(tipo_conta)s, 
            %(Cliente_cpf)s, 
            %(Gerente_idFuncionario)s, 
            %(Agencia_idAgencia)s
        );
        """
        banco.cursor.execute(
            slq, {"saldo": conta.saldo, "senha": bcrypt_context.hash(conta.senha), "tipo_conta": conta.tipo_conta.value, "Cliente_cpf": conta.cliente_cpf, "Gerente_idFuncionario": conta.id_gerente, "Agencia_idAgencia": conta.id_agencia})
        if conta.tipo_conta.value == 'CONTA_ESPECIAL':
            slq = f"""INSERT INTO ContaEspecial (ContaBancaria_numero_conta, limite_credito)
            VALUES (
            {numero_conta}, 
            %(limite_credito)s
            );
            """
            banco.cursor.execute(
                slq, {"limite_credito": conta.limite_de_credito})
        elif conta.tipo_conta.value == 'CONTA_POUPANCA':
            slq = f"""INSERT INTO ContaPoupanca (ContaBancaria_numero_conta, taxa_juros)
            VALUES (
                %(ContaBancaria_numero_conta)s, 
                %(taxa_juros)s
                );
            """
            banco.cursor.execute(
                slq, {"ContaBancaria_numero_conta": numero_conta, "taxa_juros": conta.taxa_de_juros})
            banco.conexao.commit()
        else:
            slq = f"""INSERT INTO contaCorrente (ContaBancaria_numero_conta, aniversario_contrato)
            VALUES (
                %(ContaBancaria_numero_conta)s, 
                %(aniversario_contrato)s
                );
            """
            banco.cursor.execute(
                slq, {"ContaBancaria_numero_conta": numero_conta, "aniversario_contrato": conta.aniversario_contrato})
            banco.conexao.commit()
        banco.conexao.commit()
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")


@contaRouter.put("/")
async def modificarConta(conta: ContaModelPut, usuario: login_dependency):
    if usuario['tipo_usuario'] == 'DBA':
        banco = bd.Bd()
        slq = f"""UPDATE ContaBancaria
        SET 
            saldo = %(saldo)s,
            senha = %(senha)s,
            Gerente_idFuncionario = %(Gerente_idFuncionario)s,
            Agencia_idAgencia = %(Agencia_idAgencia)s
        WHERE numero_conta = %(numero_conta)s;
            """
        banco.cursor.execute(slq, {"saldo": conta.saldo, "senha": conta.senha, "numero_conta": conta.numero_conta,
                                   "Gerente_idFuncionario": conta.id_gerente, "Agencia_idAgencia": conta.id_agencia})
        banco.conexao.commit()
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")
