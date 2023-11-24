import uuid
from fastapi import APIRouter
import bd
from models.clienteModel import ClienteModelDelete, ClienteModelPost, ClienteModelPut, ClienteEnderecoModelPost, ClienteEmailModelPost, ClienteTelefoneModelPost, ClienteEnderecoModelPut, ClienteEmailModelPut, ClienteTelefoneModelPut, ClienteEmailModelDelete, ClienteEnderecoModelDelete, ClienteTelefoneModelDelete
clienteRouter = APIRouter()
from datetime import datetime

@clienteRouter.get("/")
async def list_cliente():
    banco = bd.Bd()
    slq = f"""SELECT * FROM Cliente AS C 
    INNER JOIN Endereco AS E ON C.Endereco_idEndereco = E.idEndereco 
    LEFT JOIN Email as M on C.cpf = M.Cliente_cpf 
    LEFT JOIN Telefone as T on C.cpf = T.Cliente_cpf"""
    banco.cursor.execute(slq)
    return banco.cursor.fetchall()

@clienteRouter.get("/{cpf}")
async def ler_cliente(cpf:str):
    banco = bd.Bd()
    slq = """SELECT * FROM Cliente AS C 
    INNER JOIN Endereco AS E ON C.Endereco_idEndereco = E.idEndereco 
    LEFT JOIN Email as M on C.cpf = M.Cliente_cpf 
    LEFT JOIN Telefone as T on C.cpf = T.Cliente_cpf
    WHERE
        `cpf` = %(cpf)s;"""
    banco.cursor.execute(slq, {"cpf": cpf})
    return banco.cursor.fetchall()

@clienteRouter.post("/telefone")
async def createClienteTelefone(cliente: ClienteTelefoneModelPost):
    banco = bd.Bd()
    slq = f"""INSERT INTO `nullbank`.`Telefone` (
        `idTelefone`, 
        `telefone`, 
        `tipo`, 
        `Cliente_cpf`)
        VALUES (
         {int(uuid.uuid4().int%10**7)}, 
        %(telefone)s, 
        %(tipo)s, 
        %(Cliente_cpf)s);
    """
    banco.cursor.execute(
        slq, {"telefone": cliente.telefone, "tipo": cliente.tipo, "Cliente_cpf": cliente.cpf})
    banco.conexao.commit()
    return banco.cursor.fetchall()

@clienteRouter.put("/telefone")
async def modificarClienteTelefone(cliente: ClienteTelefoneModelPut):
    banco = bd.Bd()
    slq = f"""UPDATE `nullbank`.`Telefone`
    SET
    `telefone` = %(telefone)s,
    `tipo` = %(tipo)s
    WHERE `idTelefone` = %(id_telefone)s;

    """
    banco.cursor.execute(
        slq, {"telefone": cliente.telefone, "tipo": cliente.tipo, "id_telefone": cliente.id_telefone})
    banco.conexao.commit()
    return banco.cursor.fetchall()

@clienteRouter.post("/email")
async def createClienteEmail(cliente: ClienteEmailModelPost):
    banco = bd.Bd()
    slq = f"""INSERT INTO `nullbank`.`Email` (
        `idEmail`, 
        `email`, 
        `tipo`, 
        `Cliente_cpf`)
    VALUES (
        {int(uuid.uuid4().int%10**7)}, 
        %(email)s, 
        %(tipo)s, 
        %(Cliente_cpf)s);
    """
    banco.cursor.execute(
        slq, {"email": cliente.email, "tipo": cliente.tipo, "Cliente_cpf": cliente.cpf})
    banco.conexao.commit()
    return banco.cursor.fetchall()

@clienteRouter.put("/email")
async def ModificarClienteEmail(cliente: ClienteEmailModelPut):
    banco = bd.Bd()
    slq = f"""UPDATE `nullbank`.`Email`
    SET
    `email` = %(email)s,
    `tipo` = %(tipo)s
    WHERE `idEmail` = %(idEmail)s;
    """
    banco.cursor.execute(
        slq, {"email": cliente.email, "tipo": cliente.tipo, "idEmail": cliente.id_email})
    banco.conexao.commit()
    return banco.cursor.fetchall()


@clienteRouter.post("/endereco")
async def createClienteEndereco(cliente: ClienteEnderecoModelPost):
    banco = bd.Bd()
    slq = f"""INSERT INTO `nullbank`.`Endereco` (
        `idEndereco`, 
        `tipo_logradouro`, 
        `nome_logradouro`, 
        `numero`, 
        `bairro`, 
        `cep`, 
        `cidade`, 
        `estado`)
        VALUES (
        {int(uuid.uuid4().int%10**7)}, 
        %(tipo_logradouro)s, 
        %(nome_logradouro)s, 
        %(numero)s, 
        %(bairro)s, 
        %(cep)s, 
        %(cidade)s, 
        %(estado)s);

    """
    banco.cursor.execute(
        slq, {"tipo_logradouro": cliente.endereco_tipo_logradouro, "nome_logradouro": cliente.endereco_nome_logradouro, "numero": cliente.endereco_numero, "bairro": cliente.endereco_bairro, "cep": cliente.endereco_cep, "cidade": cliente.endereco_cidade, "estado": cliente.endereco_estado})
    banco.conexao.commit()
    return banco.cursor.fetchall()

@clienteRouter.put("/endereco")
async def modificarEndereco(cliente: ClienteEnderecoModelPut):
    banco = bd.Bd()
    slq = f"""UPDATE `nullbank`.`Endereco`
SET
  `tipo_logradouro` = %(tipo_logradouro)s,
  `nome_logradouro` = %(nome_logradouro)s,
  `numero` =  %(numero)s,
  `bairro` = %(bairro)s,
  `cep` = %(cep)s,
  `cidade` = %(cidade)s,
  `estado` = %(estado)s
WHERE `idEndereco` = %(id_endereco)s;

"""
    banco.cursor.execute(
        slq, {"tipo_logradouro": cliente.endereco_tipo_logradouro, "nome_logradouro": cliente.endereco_nome_logradouro, "numero": cliente.endereco_numero, "bairro": cliente.endereco_bairro, "cep": cliente.endereco_cep, "cidade": cliente.endereco_cidade, "estado": cliente.endereco_estado, "id_endereco": cliente.id_endereco})
    banco.conexao.commit()
    return banco.cursor.fetchall()

@clienteRouter.post("/")
async def createCliente(cliente: ClienteModelPost):
    cliente.data_nascimento = datetime.strptime(cliente.data_nascimento, "%Y-%m-%d %H:%M:%S")
    banco = bd.Bd()
    slq = f"""INSERT INTO `nullbank`.`Cliente` (
    `cpf`, 
    `nome_completo`, 
    `rg`, 
    `orgao_emissor`, 
    `uf_rg`, 
    `data_nascimento_cliente`, 
    `Endereco_idEndereco`)
    VALUES (
    %(cpf)s, 
    %(nome)s, 
    %(rg)s, 
    %(orgao_emissor)s, 
    %(uf_rg)s, 
    %(data_de_nascimento)s, 
    %(id_endereco)s
    );
    """
    banco.cursor.execute(
        slq, {"cpf": cliente.cpf, "nome": cliente.nome, "rg": cliente.rg, "orgao_emissor": cliente.orgao_emissor, "uf_rg": cliente.uf_rg, "data_de_nascimento": cliente.data_nascimento, "id_endereco": cliente.id_endereco})
    banco.conexao.commit()
    return banco.cursor.fetchall()


@clienteRouter.put("/")
async def modificarCliente(cliente: ClienteModelPut):
    banco = bd.Bd()
    slq = f"""UPDATE `nullbank`.`Cliente`
SET
  `nome_completo` = %(nome)s,
  `rg` = %(rg)s,
  `orgao_emissor` = %(orgao_emissor)s,
  `uf_rg` = %(uf_rg)s
WHERE `cpf` = %(cpf)s;
"""
    banco.cursor.execute(slq, {"nome": cliente.nome, "rg": cliente.rg,"orgao_emissor": cliente.orgao_emissor,"uf_rg": cliente.uf_rg,"cpf": cliente.cpf})
    banco.conexao.commit()
    return banco.cursor.fetchall()

@clienteRouter.delete("/")
async def deletarCliente(cliente: ClienteModelDelete):
    banco = bd.Bd()
    slq = f"""DELETE FROM `nullbank`.`Cliente`
    WHERE
        `cpf` = %(cpf)s;"""
    banco.cursor.execute(slq, {"cpf": cliente.cpf})
    banco.conexao.commit()
    return banco.cursor.fetchall()

@clienteRouter.delete("/endereco")
async def deletarEndereco(cliente: ClienteEnderecoModelDelete):
    banco = bd.Bd()
    slq = f"""DELETE FROM `nullbank`.`Endereco`
    WHERE
        `idEndereco` = %(id)s;"""
    banco.cursor.execute(slq, {"id": cliente.id})
    banco.conexao.commit()
    return banco.cursor.fetchall()

@clienteRouter.delete("/telefone")
async def deletarTelefone(cliente: ClienteTelefoneModelDelete):
    banco = bd.Bd()
    slq = f"""DELETE FROM `nullbank`.`Telefone`
    WHERE
        `idTelefone` = %(id)s;"""
    banco.cursor.execute(slq, {"id": cliente.id})
    banco.conexao.commit()
    return banco.cursor.fetchall()

@clienteRouter.delete("/email")
async def deletarEmail(cliente: ClienteEmailModelDelete):
    banco = bd.Bd()
    slq = f"""DELETE FROM `nullbank`.`Email`
    WHERE
        `idEmail` = %(id)s;"""
    banco.cursor.execute(slq, {"id": cliente.id})
    banco.conexao.commit()
    return banco.cursor.fetchall()

