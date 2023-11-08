

def salvar_lista(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for item in lista:
            arquivo.write(item + '\n')

# Para carregar a lista a partir do arquivo de texto
def carregar_lista(nome_arquivo):
    lista = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                lista.append(linha.strip())
    except FileNotFoundError:
        lista = []  # Se o arquivo não existir, retorna uma lista vazia
    return lista

# Exemplo de uso
clientes = []

while True:
    cliente = input('Insira um nome (ou digite "sair" para encerrar): ')
    if cliente == 'sair':
        break
    clientes.append(cliente)

# Salvando a lista em um arquivo
    salvar_lista(clientes, 'lista_clientes.pkl')

# Carregando a lista a partir do arquivo
    lista_carregada = carregar_lista('lista_clientes.pkl')

# Imprimindo a lista carregada
    print('Lista carregada:', lista_carregada)

# Iterando pela lista carregada
    for i, cliente in enumerate(lista_carregada):
        tamanho_lista = len(lista_carregada)
        if tamanho_lista == 1:
            id_venda = 0
        else:
            id_venda = i
    print(f'{cliente} - id_venda: {id_venda}')