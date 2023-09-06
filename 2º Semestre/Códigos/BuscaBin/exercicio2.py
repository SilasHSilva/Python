def main():

    lista_clientes = []
    resp = 1

    while (resp != 0):
        print("1-Inserção de um cliente")
        print("2-Alteração de um cliente")
        print("3-Exclusão de um cliente")
        print("4-Exibição de todos os clientes")
        print("5-Ordenação dos clientes por nome")
        print("6-Busca Binária por nome")
        opc = int(input("Digite a opção desejada (1-5): "))
        if (opc == 1):
            insere_cliente(lista_clientes)
        elif (opc == 2):
            cod = int(input("Digite o código do cliente a ser alterado: "))
            altera_cliente(lista_clientes, cod)
        elif (opc == 3):
            cod = int(input("Digite o código do cliente a ser excluído: "))
            exclui_cliente(lista_clientes, cod)
        elif (opc == 4):
            print(lista_clientes)
        elif (opc == 5):
            bubbleSort(lista_clientes)
            print("Ordenação concluída com sucesso!")
        elif (opc == 6):
            bubbleSort(lista_clientes)
            nome = input("Digite um nome a ser procurado: ")
            pos = buscaBin (lista_clientes,nome)
            if (pos != -1):
                print("O nome está na lista")
                print(lista_clientes[pos])
            else:
                print("O nome não está na lista")

        resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

def insere_cliente (lista_clientes):
    try:
        cod = int(input("Digite o código do cliente: "))
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o cpf do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        endereco = input("Digite o endereço do cliente: ")
        limite_credito = float(input("Digite o limite de crédito do cliente: "))

    except ValueError:
        print("Digite valores numéricos")
    else:
        cliente = {'Codigo': cod, 'Nome': nome, 'Cpf': cpf, 'Idade': idade,
                   'Endereco': endereco, 'Limite_credito': limite_credito}
        lista_clientes.append(cliente)
    finally:
        print("Operação finalizada")

def busca_cliente (lista_clientes,cod):
    pos = -1
    for i in range(len(lista_clientes)):
        if (cod == lista_clientes[i]['Codigo']):
            pos = i
    return (pos)

def altera_cliente (lista_clientes,cod):
    pos = busca_cliente(lista_clientes, cod)

    if (pos != -1):  # encontrou o cÃ³digo do cliente no dicionÃ¡rio da lista
        try:
            print(f"Nome do cliente: {lista_clientes[pos]['Nome']}")
            nome = input("Digite o nome do cliente: ")
            print(f"Cpf do cliente: {lista_clientes[pos]['Cpf']}")
            cpf = input("Digite o cpf do cliente: ")
            print(f"Idade do cliente: {lista_clientes[pos]['Idade']}")
            idade = int(input("Digite a idade do cliente: "))
            print(f"Endereço do cliente: {lista_clientes[pos]['Endereco']}")
            endereco = input("Digite o endereço do cliente: ")
            print(f"Limite de crédito do cliente: {lista_clientes[pos]['Limite_credito']}")
            limite_credito = float(input("Digite o limite de crédito do cliente: "))

        except ValueError:
            print("Digite valores numéricos")
        else:
            lista_clientes[pos]['Nome'] = nome
            lista_clientes[pos]['Cpf'] = cpf
            lista_clientes[pos]['Idade'] = idade
            lista_clientes[pos]['Endereco'] = endereco
            lista_clientes[pos]['Limite_credito'] = limite_credito
        finally:
            print("Operação finalizada")
    else:
        print("Código não encontrado!")

def exclui_cliente (lista_clientes, cod):
    pos = busca_cliente(lista_clientes, cod)
    for i in range(len(lista_clientes)):
        if (cod == lista_clientes[i]['Codigo']):
            pos = i
    if (pos != -1):
        lista_clientes.pop(pos)
        print("cliente excluído com sucesso!")
    else:
        print("Código não encontrado!")

def bubbleSort (lista_clientes):
    tam= len(lista_clientes)
    for i in range(tam-1,0,-1):
        for j in range(i):
            if lista_clientes[j]['Nome'] > lista_clientes[j+1]['Nome']:
                temp = lista_clientes[j]
                lista_clientes[j] = lista_clientes[j+1]
                lista_clientes[j+1] = temp

def buscaBin (lista_clientes,elem):
    ini = 0
    fim = len(lista_clientes) - 1

    while (ini <= fim):
        meio = int((ini+fim)/2)
        if (lista_clientes[meio]['Nome'] == elem):
            return (meio)
        else:
            if (elem < lista_clientes[meio]['Nome']):
                fim = meio - 1
            else:
                ini = meio + 1
    return(-1)

if (__name__ == "__main__"):
    main()
