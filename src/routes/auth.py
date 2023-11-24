from fastapi import APIRouter
from bd import Bd
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.token import Token, UserLogin

router = APIRouter()

SECRET_KEY = "b8ce4b0d2549e75cf2798e9aa649d25c5a2bff008e408036bd39e9552a8139628e3b9c9cbbd14a3f92159dfcad3a8475bf7fa4bafdce167de2cf6dfd0e3d0377fe49c3a80a6a2a3dc0e775cf28247f8a701496a6528919b464458b7f2314ce28a8a0dd447ca5f6920da6108ff3ea609a436d260927eae56cdd56c6089e34c1367bd165464ced8f83197a27e6d236aac898a2f48b7f5602a3846c61400b76ca2c"
ALGORITHM = "HS256"

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


@router.post('/token', response_model=Token)
async def login_for_acess_token(dados: UserLogin):
    user = authenticate_user(dados.usuario_id, dados.tipo_usuario, dados.senha)
    return user

def authenticate_user(id, tipo_usuario, senha):
    if tipo_usuario == 'gerente':
        print("Gerente")