from pydantic import BaseModel


class AgenciaModelPost(BaseModel):
    nome: str
    cidade: str


class AgenciaModelPut(BaseModel):
    id: int
    nome: str
    cidade: str


class AgenciaModelDelete(BaseModel):
    id: int
