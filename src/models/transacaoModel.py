from pydantic import BaseModel
from enum import Enum

class tipo_transacao(Enum):
    SAQUE = 'SAQUE'
    DEPOSITO = 'DEPOSITO'
    ESTORNO = 'ESTORNO'
    TRANSFERENCIA = 'TRANSFERENCIA'

class TransferenciaModelPost(BaseModel):
    tipo_transacao: tipo_transacao
    valor: float
    entrada: int
    saida: int

