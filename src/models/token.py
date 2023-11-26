from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserLogin(BaseModel):
    usuario_id: str
    tipo_usuario: str
    senha: str
