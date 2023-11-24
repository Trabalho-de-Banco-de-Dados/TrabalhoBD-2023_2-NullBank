from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserLogin(BaseModel):
    usuario_id: int
    tipo_usuario: str
    senha: str