import mysql.connector


class Bdmeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


def conectar():
    print("Iniciando conexão")
    conexao = mysql.connector.connect(
        host='db4free.net',
        user='nullbank',
        password='RootRoot',
        database='nullbank',
        port=3306
    )
    print("Conexão feita com o banco")
    return conexao


class Bd(metaclass=Bdmeta):
    def __init__(self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()
