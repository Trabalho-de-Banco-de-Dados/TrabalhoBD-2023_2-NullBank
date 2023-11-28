from fastapi import FastAPI
import uvicorn
from routes.main_routes import mainRoutes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Nullbank",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(mainRoutes)

if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
