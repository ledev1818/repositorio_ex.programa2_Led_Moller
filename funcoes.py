import random

def rolar_dados(n):
    listaDados = []
    for i in range(n):
        listaDados.append(random.randint(1, 6))
    return listaDados

def guardar_dado(dadosRolados, dadosEstoque, dadoGuardar):
    novosRolados = []
    novoEstoque = []
    for i in dadosEstoque:
        novoEstoque.append(i)
    novoEstoque.append(dadosRolados[dadoGuardar])
    # cria a nova lista de estoque, adicionando os antigos e o novo dado

    for i in range(len(dadosRolados)):
        if i != dadoGuardar:
            novosRolados.append(dadosRolados[i])
    # cria a nova lista de dados rolados, pulando o dado a ser guardado

    return [novosRolados, novoEstoque]

