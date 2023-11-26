from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class Cargo(Enum):
    GERENTE = 'GERENTE'
    ATENDENTE = 'ATENDENTE'
    CAIXA = 'CAIXA'


class Sexo(Enum):
    FEMININO = 'MASCULINO'
    MASCULINO = 'FEMININO'


class FuncionarioModelPost(BaseModel):
    matricula: int
    nome: str
    senha: str
    endereco: str
    cidade: str
    cargo: Cargo
    sexo: Sexo
    data_nascimento: str
    salario: float
    Agencia: int
    num_dependentes: int


class FuncionarioModelPut(BaseModel):
    id: int
    nome: str
    endereco: str
    cidade: str
    cargo: Cargo
    salario: float
    num_dependentes: int


class FuncionarioModelDelete(BaseModel):
    id: int
