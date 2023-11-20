from pydantic import BaseModel
from enum import Enum

class Parentesco(Enum):
    FILHO = 'FILHO'
    GENITOR = 'GENITOR'
    CONJUGE = 'CONJUGE'

class FuncionarioModelPost(BaseModel):
    nome: str
    senha: str
    endereco: str
    cidade: str
    parentesco: Parentesco
    data_nascimento: str
    salario: float
    Agencia: int
    num_dependentes: int

class FuncionarioModelPut(BaseModel):
    id: int
    nome: str
    endereco: str
    cidade: str
    parentesco: Parentesco
    salario: float
    num_dependentes: int


class FuncionarioModelDelete(BaseModel):
    id: int