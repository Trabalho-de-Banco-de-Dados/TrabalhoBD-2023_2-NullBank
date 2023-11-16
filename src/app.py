import mysql.connector
from fastapi import FastAPI
import uvicorn

def conexao():
    conexao = mysql.connector.connect(
        host = 'db4free.net',
        user = 'nullbank',
        password = 'RootRoot',
        database = 'nullbank',
        port = 3306
    )
    return conexao

def fechar_conexao(cursor, conexao):
    cursor.close()
    conexao.close()

app = FastAPI()

@app.get('/')
async def index():
    return 'hello word'

@app.get('/agencia/list')
async def agencia_list():
    conexao = conexao()
    cursor = conexao.cursor()
    slq = f'SELECT * FROM Agencia'
    cursor.execute(slq)
    fechar_conexao(cursor, conexao)
    return cursor.fetchall()
    
if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
