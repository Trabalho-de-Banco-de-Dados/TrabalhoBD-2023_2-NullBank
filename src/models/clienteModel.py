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


class ClienteEnderecoModelPut(BaseModel):
    endereco_tipo_logradouro: str
    endereco_nome_logradouro: str
    endereco_numero: int
    endereco_bairro: str
    endereco_cep: str
    endereco_cidade: str
    endereco_estado: str
    id_endereco: int


class ClienteEmailModelPost(BaseModel):
    email: str
    tipo: str
    cpf: str


class ClienteEmailModelPut(BaseModel):
    email: str
    tipo: str
    id_email: int


class ClienteTelefoneModelPost(BaseModel):
    telefone: str
    tipo: str
    cpf: str


class ClienteTelefoneModelPut(BaseModel):
    telefone: str
    tipo: str
    id_telefone: int


class ClienteModelPut(BaseModel):
    cpf: str
    nome: str
    rg: str
    orgao_emissor: str
    uf_rg: str


class ClienteModelDelete(BaseModel):
    cpf: int


class ClienteEnderecoModelDelete(BaseModel):
    id: int


class ClienteEmailModelDelete(BaseModel):
    id: int


class ClienteTelefoneModelDelete(BaseModel):
    id: int
