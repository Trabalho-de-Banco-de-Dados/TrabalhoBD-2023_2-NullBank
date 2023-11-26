from fastapi import APIRouter
import bd
from models.dbaModel import DbaModel

dbaRouter = APIRouter()


@dbaRouter.get("/")
async def list_agencias(dba: DbaModel):
    banco = bd.Bd()
    slq = dba.sql
    banco.cursor.execute(slq)
    return banco.cursor.fetchall()