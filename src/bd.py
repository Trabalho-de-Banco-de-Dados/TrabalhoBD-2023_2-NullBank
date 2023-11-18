import mysql.connector

class Bdmeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

def conectar():
    print("TESTE")
    conexao = mysql.connector.connect(
        host = 'db4free.net',
        user = 'nullbank',
        password = 'RootRoot',
        database = 'nullbank',
        port = 3306
    )
    return conexao

class Bd(metaclass=Bdmeta):
    def __init__(self):
        self.conecxao = conectar()
        self.cursor = self.conecxao.cursor()