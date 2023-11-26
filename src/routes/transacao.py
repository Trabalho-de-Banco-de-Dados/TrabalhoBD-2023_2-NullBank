from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, HTTPException
import bd
from models.transacaoModel import TransferenciaModelPost
from datetime import datetime
from routes.auth import pegar_dados_usuarios

transacaoRouter = APIRouter()
login_dependency = Annotated[dict, Depends(pegar_dados_usuarios)]


@transacaoRouter.get("/")
async def list_transacao(usuario: login_dependency):
    if usuario['tipo_usuario'] in ['CAIXA', 'DBA']:
        banco = bd.Bd()
        slq = f'SELECT * FROM Transacao'
        banco.cursor.execute(slq)
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")


@transacaoRouter.get("/{id}")
async def ler_transacao(id: str, usuario: login_dependency):
    if usuario['tipo_usuario'] in ['CAIXA', 'DBA']:
        banco = bd.Bd()
        slq = """SELECT * FROM `nullbank`.`Transacao`
        WHERE
            `idTransacao` = %(id_transacao)s;"""
        banco.cursor.execute(slq, {"id_transacao": id})
        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")


@transacaoRouter.post("/")
async def createTransacao(transacao: TransferenciaModelPost, usuario: login_dependency):
    if usuario['tipo_usuario'] in ['CAIXA', 'DBA']:
        banco = bd.Bd()
        data_e_hora = datetime.now()
        if transacao.tipo_transacao.value == 'TRANSFERENCIA':
            slq = f"""INSERT INTO Transacao (idTransacao, tipo_transacao, data_hora, valor, Entrada, Saida)
        VALUES (
            {int(uuid.uuid4().int%10**7)},
            %(tipo_transacao)s,
            '{data_e_hora}',
            %(valor)s,
            %(Entrada)s,
            %(Saida)s
            );
        """
            banco.cursor.execute(
                slq, {"tipo_transacao": transacao.tipo_transacao.value, "valor": transacao.valor, "Entrada": transacao.entrada, "Saida": transacao.saida})
        elif transacao.tipo_transacao.value == 'ESTORNO':
            slq = f"""INSERT INTO Transacao (idTransacao, tipo_transacao, data_hora, valor, Entrada, Saida)
        VALUES (
            {int(uuid.uuid4().int%10**7)},
            %(tipo_transacao)s,
            '{data_e_hora}',
            %(valor)s,
            %(Entrada)s,
            %(Saida)s
            );
        """
            banco.cursor.execute(
                slq, {"tipo_transacao": transacao.tipo_transacao.value, "valor": transacao.valor, "Entrada": transacao.entrada, "Saida": transacao.entrada})
        elif transacao.tipo_transacao.value == 'DEPOSITO':
            slq = f"""INSERT INTO Transacao (idTransacao, tipo_transacao, data_hora, valor, Entrada, Saida)
        VALUES (
            {int(uuid.uuid4().int%10**7)},
            %(tipo_transacao)s,
            '{data_e_hora}',
            %(valor)s,
            %(Entrada)s,
            NULL
            );
        """
            banco.cursor.execute(
                slq, {"tipo_transacao": transacao.tipo_transacao.value, "valor": transacao.valor, "Entrada": transacao.entrada})
        else:
            slq = f"""INSERT INTO Transacao (idTransacao, tipo_transacao, data_hora, valor, Entrada, Saida)
        VALUES (
            {int(uuid.uuid4().int%10**7)},
            %(tipo_transacao)s,
            '{data_e_hora}',
            %(valor)s,
            %(Entrada)s,
            %(Saida)s
            );
        """
            banco.cursor.execute(
                slq, {"tipo_transacao": transacao.tipo_transacao.value, "valor": transacao.valor, "Entrada": transacao.entrada, "Saida": transacao.entrada})
        banco.conexao.commit()

        return banco.cursor.fetchall()
    raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")
