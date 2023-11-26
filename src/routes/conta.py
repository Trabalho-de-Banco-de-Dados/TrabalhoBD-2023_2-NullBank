import uuid
from fastapi import APIRouter
import bd
from models.contaModel import  ContaModelPost, ContaModelPut
from datetime import datetime
from enum import Enum

contaRouter = APIRouter()

@contaRouter.get("/")
async def list_conta():
    banco = bd.Bd()
    slq = f"""SELECT *FROM ContaBancaria
    """
    banco.cursor.execute(slq)
    return banco.cursor.fetchall()

@contaRouter.get("/{numero_conta}")
async def ler_conta(numero_conta:str):
    banco = bd.Bd()
    slq = """SELECT * FROM `nullbank`.`ContaBancaria`
    WHERE
        `numero_conta` = %(numero_conta)s;"""
    banco.cursor.execute(slq, {"numero_conta": numero_conta})
    return banco.cursor.fetchall()

@contaRouter.post("/")
async def createConta(conta: ContaModelPost):
    numero_conta = int(uuid.uuid4().int%10**7)
    banco = bd.Bd()
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
        slq, {"saldo": conta.saldo, "senha": conta.senha, "tipo_conta": conta.tipo_conta.value, "Cliente_cpf": conta.cliente_cpf, "Gerente_idFuncionario": conta.id_gerente, "Agencia_idAgencia": conta.id_agencia})
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


@contaRouter.put("/")
async def modificarConta(conta: ContaModelPut):
    banco = bd.Bd()
    slq = f"""UPDATE ContaBancaria
    SET 
        saldo = %(saldo)s,
        senha = %(senha)s,
        Gerente_idFuncionario = %(Gerente_idFuncionario)s,
        Agencia_idAgencia = %(Agencia_idAgencia)s
    WHERE numero_conta = %(numero_conta)s;
        """
    banco.cursor.execute(slq, {"saldo": conta.saldo, "senha": conta.senha, "numero_conta": conta.numero_conta, "Gerente_idFuncionario": conta.id_gerente, "Agencia_idAgencia": conta.id_agencia})
    banco.conexao.commit()
    return banco.cursor.fetchall()
