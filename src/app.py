from fastapi import FastAPI
import uvicorn
import bd

app = FastAPI(
    title="Nullbank",
    version="1.0.0"
)

@app.get('/')
async def index():
    return 'hello word'

@app.get('/agencia/list')
async def agencia_list():
    banco = bd.Bd()
    slq = f'SELECT * FROM Agencia'
    banco.cursor.execute(slq)
    return banco.cursor.fetchall()
    
if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
