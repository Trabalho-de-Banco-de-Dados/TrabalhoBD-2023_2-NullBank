from pydantic import BaseModel
from enum import Enum


class tipo_conta(Enum):
    CONTA_ESPECIAL = 'CONTA_ESPECIAL'
    CONTA_POUPANCA = 'CONTA_POUPANCA'
    CONTA_CORRENTE = 'CONTA_CORRENTE'


class ContaModelPost(BaseModel):
    saldo: float
    senha: str
    tipo_conta: tipo_conta
    cliente_cpf: str
    id_gerente: int
    id_agencia: int
    aniversario_contrato: str
    taxa_de_juros: float
    limite_de_credito: int


class ContaModelPut(BaseModel):
    numero_conta: int
    saldo: float
    senha: str
    id_gerente: int
    id_agencia: int
