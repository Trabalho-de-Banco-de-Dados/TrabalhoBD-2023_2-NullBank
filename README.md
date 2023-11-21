# NullBank - Sistema de Controle Bancário

## Descrição

Este projeto é uma implementação de um sistema de controle bancário chamado "NullBank". O sistema é desenvolvido usando Python, com MySQL ver. 5.7 como o banco de dados e MySQL Workbench para modelagem. O sistema é compatível com o sistema operacional Windows 10+.

## Modelo de Negócios

O sistema dá suporte ao cadastro e à manutenção (remoção / alteração) dos dados de todas as entidades participantes do sistema bancário do NullBank. Ele gerencia agências, funcionários, clientes, contas bancárias e transações.

## Funcionalidades

1. **Administração de Agências**: O sistema permite o gerenciamento de agências, incluindo a criação, remoção e atualização de agências.

2. **Administração de Funcionários**: O sistema permite o gerenciamento de funcionários, incluindo a criação, remoção e atualização de funcionários.

3. **Administração de Clientes**: O sistema permite o gerenciamento de clientes, incluindo a criação, remoção e atualização de clientes.

4. **Administração de Contas Bancárias**: O sistema permite o gerenciamento de contas bancárias, incluindo a criação, remoção e atualização de contas.

5. **Administração de Transações**: O sistema permite o gerenciamento de transações, incluindo a criação, remoção e atualização de transações.

## Como Usar

1. Clone este repositório para o seu computador local.
2. Instale as dependências necessárias.
3. Configure o banco de dados MySQL usando o arquivo de configuração fornecido.
4. Execute o sistema.

## Equipe responsável pelo projeto

INÁCIO LIMA DE SOUZA FILHO - 509153

GABRIEL ARAUJO TEIXEIRA - 511476

FRANCISCO WENDEL ALVES RIBEIRO - 510424

## Professor resposável

FERNANDO RODRIGUES DE ALMEIDA JÚNIOR

## Disciplina / Instituição

Banco de Dados 2023.2 / UNIVERSIDADE FEDERAL DO CEARÁ

## Como rodar backEnd
Com o python intalado o primeiro passo é criar um ambiente virtual

```python -m venv venv```

Ativar o ambiente

```.\venv\Scripts\activate```

Instalar as dependências

```pip install -r requirements.txt```

E rodar o código

```python src/app.py```
## Requisitos Back-End
- [X] CRUD de Agências
- [X] CRUD de Funcionários
- [X] CRUD de Dependentes
- [ ] CRUD de  Contas
- [ ] CRUD de  Clientes
- [ ] Adicionar Transações
- [ ] Adicionar login para DBA
- [ ] Adicionar login para funcionários
- [ ] Adicionar login para clientes
##