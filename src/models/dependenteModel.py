from pydantic import BaseModel
from enum import Enum

class Parentesco(Enum):
    FILHO = 'FILHO'
    GENITOR = 'GENITOR'
    CONJUGE = 'CONJUGE'

class DependenteModelPost(BaseModel):
    nome: str
    parentesco: Parentesco
    data_nascimento: str
    id_funcionario: int

class DependenteModelPut(BaseModel):
    id: int
    nome: str


class DependenteModelDelete(BaseModel):
    id: int