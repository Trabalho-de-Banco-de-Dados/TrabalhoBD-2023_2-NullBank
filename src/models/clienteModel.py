from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class ClienteModelPost(BaseModel):
    id_endereco: int
    cpf: str
    nome: str
    rg: str
    orgao_emissor: str
    uf_rg: str
    data_nascimento: str
  

class ClienteEnderecoModelPost(BaseModel):
    endereco_tipo_logradouro: str
    endereco_nome_logradouro: str
    endereco_numero: int
    endereco_bairro: str
    endereco_cep: str
    endereco_cidade: str
    endereco_estado: str

class ClienteEmailModelPost(BaseModel):
    email: str
    tipo: str
    cpf: str

class ClienteTelefoneModelPost(BaseModel):
    telefone: str
    tipo: str
    cpf: str

class ClienteModelPut(BaseModel):
    cpf: str
    nome: str
    rg: str
    orgao_emissor: str
    uf_rg: str
    data_nascimento: str

    

class ClienteModelDelete(BaseModel):
    id: int