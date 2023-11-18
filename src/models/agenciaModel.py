from pydantic import BaseModel

class AgenciaModelPost(BaseModel):
    nome: str
    cidade: str
    # description: str | None = None
    # price: float
    # tax: float | None = None