from fastapi import APIRouter, Depends, HTTPException
import bd
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.token import Token, UserLogin
from passlib.context import CryptContext
from datetime import timedelta
from jose import jwt, JWTError
import datetime
from typing import Annotated

router = APIRouter()

SECRET_KEY = "b8ce4b0d2549e75cf2798e9aa649d25c5a2bff008e408036bd39e9552a8139628e3b9c9cbbd14a3f92159dfcad3a8475bf7fa4bafdce167de2cf6dfd0e3d0377fe49c3a80a6a2a3dc0e775cf28247f8a701496a6528919b464458b7f2314ce28a8a0dd447ca5f6920da6108ff3ea609a436d260927eae56cdd56c6089e34c1367bd165464ced8f83197a27e6d236aac898a2f48b7f5602a3846c61400b76ca2c"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


@router.post('/token', response_model=Token)
async def login_for_acess_token(dados: UserLogin):
    user = authenticate_user(dados.usuario_id, dados.tipo_usuario, dados.senha)
    user = bool(user)
    if not user:
        raise HTTPException(status_code=500, detail="Usuário ou senha incorretos")
    token = create_access_token(dados.usuario_id, dados.tipo_usuario, timedelta(days=30))
    return {"access_token": str(token), "token_type": "1"}

def authenticate_user(id, tipo_usuario, senha):
    banco = bd.Bd()
    if tipo_usuario in ['GERENTE', 'ATENDENTE', 'CAIXA']:
        slq = """SELECT * FROM `nullbank`.`Funcionario`
        WHERE
            `matricula` = %(matricula)s AND `cargo` = %(cargo)s;"""
        banco.cursor.execute(slq, {"matricula": id, "cargo": tipo_usuario})
        result = banco.cursor.fetchall()
        if len(list(result))==0:
            return False
        if not bcrypt_context.verify(senha, result[0][3]):
            return False
        return True        
    elif tipo_usuario == 'DBA':
        if id == "ADMIN" and senha == "ROOT":
            return True
        
def create_access_token(usuario_id, tipo_usuario, time_delta):
    encode = {"usuario_id": usuario_id, "tipo_usuario":  tipo_usuario}
    experies = datetime.datetime.utcnow() + time_delta
    encode.update({"exp": experies})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def pegar_dados_usuarios(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id = payload.get("usuario_id")
        tipo_usuario = payload.get("tipo_usuario")
        if usuario_id is None or tipo_usuario is None:
           raise HTTPException(status_code=401, detail='Não foi possível valisar o usuário')
        return {"usuario_id": usuario_id, "tipo_usuario": tipo_usuario} 
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=401, detail='Não foi possível valisar o usuário')