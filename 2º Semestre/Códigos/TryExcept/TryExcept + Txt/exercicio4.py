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
        print("7-Clientes com limite de crédito inferior a R$5000,00, ordenados pelo Limite de crédito")
        print("8-Clientes cuja idade esteja entre 25 e 45 anos, com limite de crédito superior a R$2000, ordenados pela idade")
        print("9-Gravação dos dados de todos os cliente em arquivo texto")
        print("10-Gravação do relatório da opção 7 em arquivo texto")
        print("11-Gravação do relatório da opção 8 em arquivo texto")
        opc = int(input("Digite a opção desejada (1-11): "))
        if (opc == 1):
            insere_cliente(lista_clientes)
        elif (opc == 2):
            cod = int(input("Digite o código do cliente a ser alterado: "))
            altera_cliente(lista_clientes, cod)
        elif (opc == 3):
            cod = int(input("Digite o código do cliente a ser excluído: "))
            exclui_cliente(lista_clientes, cod)
        elif (opc == 4):
            bubbleSort(lista_clientes,"Codigo")
            print(lista_clientes)
        elif (opc == 5):
            bubbleSort(lista_clientes,"Nome")
            print("Ordenação concluída com sucesso!")
        elif (opc == 6):
            bubbleSort(lista_clientes,"Nome")
            nome = input("Digite um nome a ser procurado: ")
            pos = buscaBin (lista_clientes,nome)
            if (pos != -1):
                print("O nome está na lista")
                print(lista_clientes[pos])
            else:
                print("O nome não está na lista")
        elif (opc == 7):
            if (len(lista_clientes) > 0):
                relatorio_1(lista_clientes)
        elif (opc == 8):
            if (len(lista_clientes) > 0):
                relatorio_2(lista_clientes)
        elif (opc == 9):
            if (len(lista_clientes) > 0):
                grava_arqtexto_todos(lista_clientes)
                print("Gravação concluída com sucesso!")
        elif (opc == 10):
            if (len(lista_clientes) > 0):
                grava_arqtexto_relatorio_1(lista_clientes)
                print("Gravação concluída com sucesso!")
        elif (opc == 11):
            if (len(lista_clientes) > 0):
                grava_arqtexto_relatorio_2(lista_clientes)
                print("Gravação concluída com sucesso!")
        else:
            print("Opção inválida")

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

    if (pos != -1):  # encontrou o cÃƒÂ³digo do cliente no dicionÃƒÂ¡rio da lista
        try:
            print(f"Nome do cliente: {lista_clientes[pos]['Nome']}")
            nome = input("Digite o nome do cliente: ")
            print(f"Cpf do cliente: {lista_clientes[pos]['Cpf']}")
            cpf = input("Digite o cpf do cliente: ")
            print(f"Idade do cliente: {lista_clientes[pos]['Idade']}")
            idade = int(input("Digite a idade do cliente: "))
            print(f"Endereço do cliente: {lista_clientes[pos]['Endereco']}")
            endereco = input("Digite o endereçoo do cliente: ")
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

def bubbleSort (lista_clientes,chave):
    tam= len(lista_clientes)
    for i in range(tam-1,0,-1):
        for j in range(i):
            if lista_clientes[j][chave] > lista_clientes[j+1][chave]:
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



def relatorio_1 (lista_clientes):
    bubbleSort(lista_clientes, "Limite_credito")

    for i in range(len(lista_clientes)):
        if (lista_clientes[i]['Limite_credito'] < 5000):
            print(lista_clientes[i])

def relatorio_2 (lista_clientes):
    bubbleSort(lista_clientes, "Idade")

    for i in range(len(lista_clientes)):
        if (lista_clientes[i]['Limite_credito'] > 2000 and lista_clientes[i]['Idade'] >= 25 and lista_clientes[i]['Idade'] <= 45):
            print(lista_clientes[i])

def grava_arqtexto_todos(lista_clientes):

    for i in range(len(lista_clientes)):
        texto = str(lista_clientes[i]['Codigo']) + " " + lista_clientes[i]['Nome'] + " " + lista_clientes[i]['Cpf'] + " " + str(lista_clientes[i]['Idade']) + " " + lista_clientes[i]['Endereco'] + " " + str(lista_clientes[i]['Limite_credito']) + "\n"
        with open("dados_todos_clientes.txt", "a", encoding="UTF8") as arq:
            arq.write(texto)
            arq.close()

def grava_arqtexto_relatorio_1(lista_clientes):
    bubbleSort(lista_clientes, "Limite_credito")

    for i in range(len(lista_clientes)):
        if (lista_clientes[i]['Limite_credito'] < 5000):
            texto = str(lista_clientes[i]['Codigo']) + " " + lista_clientes[i]['Nome'] + " " + lista_clientes[i]['Cpf'] + " " + str(lista_clientes[i]['Idade']) + " " + lista_clientes[i]['Endereco'] + " " + str(lista_clientes[i]['Limite_credito']) + "\n"
            with open("dados_relat1_clientes.txt", "a", encoding="UTF8") as arq:
                arq.write(texto)
                arq.close()

def grava_arqtexto_relatorio_2(lista_clientes):
    bubbleSort(lista_clientes, "Idade")

    for i in range(len(lista_clientes)):
        if (lista_clientes[i]['Limite_credito'] > 2000 and lista_clientes[i]['Idade'] >= 25 and lista_clientes[i]['Idade'] <= 45):
                texto = str(lista_clientes[i]['Codigo']) + " " + lista_clientes[i]['Nome'] + " " + lista_clientes[i]['Cpf'] + " " + str(lista_clientes[i]['Idade']) + " " + lista_clientes[i]['Endereco'] + " " + str(lista_clientes[i]['Limite_credito']) + "\n"
                with open("dados_relat2_clientes.txt", "a", encoding="UTF8") as arq:
                    arq.write(texto)
                    arq.close()

if (__name__ == "__main__"):
    main()
