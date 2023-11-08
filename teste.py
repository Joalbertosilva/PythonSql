import pyodbc
from random import randint
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-CNOFHH8;"
    "Database=PythonSql;"
)
conexao = pyodbc.connect(dados_conexao)
print('Conexão realizada!')
print()

cursor = conexao.cursor()
lista_id = []
while True: 
    cliente = input('Insira seu nome: ')
    id_venda = randint(1, 1000)
    lista_id.append(id_venda)
    while id_venda == lista_id:
        id_venda = randint(1, 1000)
    lista_id.append(id_venda)
    produto = input('Insira o nome do produto comprado: ')
    data = input('Seguindo o modelo (xx/xx/xxxx), insira a data: ')
    preco = int(input('Insira o valor da compra: '))
    quantidade = int(input('Insira a quantidade: '))

    comando = (f"""INSERT INTO VENDAS (idVenda, cliente, produto, data_venda, preco, quantidade)
    VALUES ({id_venda}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})""")
    cursor.execute(comando)
    cursor.commit()

    escolha = input('Deseja continuar [S/N]? ')
    if escolha.lower() == 'n':
        print('Programa Encerrado!')
        break;