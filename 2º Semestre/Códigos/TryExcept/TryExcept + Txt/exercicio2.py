def main():

    lista_produtos = []
    resp = 1

    while (resp != 0):
        print("1-Inserção de um produto")
        print("2-Alteração de um produto")
        print("3-Exclusão de um produto")
        print("4-Exibição de todos os produtos")
        print("5-Ordenação dos produtos por nome")
        print("6-Busca Binária por nome")
        print("7-Produtos cujo valor esteja entre R$150,00 e R$500,00, ordenados pelo valor")
        print("8-Produtos com quantidade superior a 100 unidades, ordenados pela quantidade")
        print("9-Gravação dos dados de todos os produtos em arquivo texto")
        print("10-Gravação do relatório da opção 7 em arquivo texto")
        print("11-Gravação do relatório da opção 8 em arquivo texto")
        opc = int(input("Digite a opção desejada (1-11): "))
        if (opc == 1):
            insere_funcionario(lista_produtos)
        elif (opc == 2):
            cod = int(input("Digite o código do produto a ser alterado: "))
            altera_funcionario(lista_produtos, cod)
        elif (opc == 3):
            cod = int(input("Digite o código do produto a ser excluído: "))
            exclui_funcionario(lista_produtos, cod)
        elif (opc == 4):
            bubbleSort(lista_produtos, "Codigo")
            print(lista_produtos)
        elif (opc == 5):
            bubbleSort(lista_produtos,"Descricao")
            print("Ordenação concluída com sucesso!")
        elif (opc == 6):
            bubbleSort(lista_produtos,"Descricao")
            nome = input("Digite um nome a ser procurado: ")
            pos = buscaBin (lista_produtos,nome)
            if (pos != -1):
                print("O nome está na lista")
                print(lista_produtos[pos])
            else:
                print("O nome não está na lista")
        elif (opc == 7):
            if (len(lista_produtos) > 0):
                relatorio_1(lista_produtos)
        elif (opc == 8):
            if (len(lista_produtos) > 0):
                relatorio_2(lista_produtos)
        elif (opc == 9):
            if (len(lista_produtos) > 0):
                grava_arqtexto_todos(lista_produtos)
                print("Gravação concluída com sucesso!")
        elif (opc == 10):
            if (len(lista_produtos) > 0):
                grava_arqtexto_relatorio_1(lista_produtos)
                print("Gravação concluída com sucesso!")
        elif (opc == 11):
            if (len(lista_produtos) > 0):
                grava_arqtexto_relatorio_2(lista_produtos)
                print("Gravação concluída com sucesso!")
        else:
            print("Opção inválida")
        resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

def insere_funcionario (lista_produtos):
    try:
        cod = int(input("Digite o código do produto: "))
        descr = input("Digite a descrição do produto: ")
        qtde = int(input("Digite a quantidade do produto: "))
        valor = float(input("Digite o valor do produto: "))

    except ValueError:
        print("Digite valores numéricos")
    else:
        funcionario = {'Codigo': cod, 'Descricao': descr, 'Quantidade': qtde,
                   'Valor': valor}
        lista_produtos.append(funcionario)
    finally:
        print("Operação finalizada")

def busca_funcionario (lista_produtos,cod):
    pos = -1
    for i in range(len(lista_produtos)):
        if (cod == lista_produtos[i]['Codigo']):
            pos = i
    return (pos)

def altera_funcionario (lista_produtos,cod):
    pos = busca_funcionario(lista_produtos, cod)

    if (pos != -1):  # encontrou o cÃƒÂ³digo do produto no dicionÃƒÂ¡rio da lista
        try:
            print(f"Descrição do produto: {lista_produtos[pos]['Descricao']}")
            descr = input("Digite a descrição do produto: ")
            print(f"Quantidade do produto: {lista_produtos[pos]['Quantidade']}")
            qtde = int(input("Digite a quantidade do produto: "))
            print(f"Valor do produto: {lista_produtos[pos]['Valor']}")
            valor = float(input("Digite o valor do produto: "))

        except ValueError:
            print("Digite valores numéricos")
        else:
            lista_produtos[pos]['Descricao'] = descr
            lista_produtos[pos]['Quantidade'] = qtde
            lista_produtos[pos]['Valor'] = valor
        finally:
            print("Operação finalizada")
    else:
        print("Código não encontrado!")

def exclui_funcionario (lista_produtos, cod):
    pos = busca_funcionario(lista_produtos, cod)
    if (pos != -1):
        lista_produtos.pop(pos)
        print("produto excluído com sucesso!")
    else:
        print("Código não encontrado!")

def bubbleSort (lista_produtos,chave):
    tam= len(lista_produtos)
    for i in range(tam-1,0,-1):
        for j in range(i):
            if lista_produtos[j][chave] > lista_produtos[j+1][chave]:
                temp = lista_produtos[j]
                lista_produtos[j] = lista_produtos[j+1]
                lista_produtos[j+1] = temp

def buscaBin (lista_produtos,elem):
    ini = 0
    fim = len(lista_produtos) - 1

    while (ini <= fim):
        meio = int((ini+fim)/2)
        if (lista_produtos[meio]['Descricao'] == elem):
            return (meio)
        else:
            if (elem < lista_produtos[meio]['Descricao']):
                fim = meio - 1
            else:
                ini = meio + 1
    return(-1)

def relatorio_1 (lista_produtos):
    bubbleSort(lista_produtos, "Valor")

    for i in range(len(lista_produtos)):
        if (lista_produtos[i]['Valor'] >= 150 and lista_produtos[i]['Valor'] <= 500):
            print(lista_produtos[i])

def relatorio_2 (lista_produtos):
    bubbleSort(lista_produtos, "Quantidade")

    for i in range(len(lista_produtos)):
        if (lista_produtos[i]['Quantidade'] > 100 ):
            print(lista_produtos[i])

def grava_arqtexto_todos(lista_produtos):

    for i in range(len(lista_produtos)):
        texto = str(lista_produtos[i]['Codigo'])+" "+lista_produtos[i]['Descricao']+" "+str(lista_produtos[i]['Quantidade'])+" "+str(lista_produtos[i]['Valor'])+"\n"
        with open("dados_todos_prod.txt","a",encoding="UTF8") as arq:
            arq.write(texto)
            arq.close()

def grava_arqtexto_relatorio_1 (lista_produtos):
    bubbleSort(lista_produtos, "Valor")

    for i in range(len(lista_produtos)):
        if (lista_produtos[i]['Valor'] >= 150 and lista_produtos[i]['Valor'] <= 500):
            texto = str(lista_produtos[i]['Codigo'])+" "+lista_produtos[i]['Descricao']+" "+str(lista_produtos[i]['Quantidade'])+" "+str(lista_produtos[i]['Valor'])+"\n"
            with open("dados_relat1_produtos.txt", "a", encoding="UTF8") as arq:
                arq.write(texto)
                arq.close()

def grava_arqtexto_relatorio_2 (lista_produtos):
    bubbleSort(lista_produtos, "Quantidade")

    for i in range(len(lista_produtos)):
        if (lista_produtos[i]['Quantidade'] > 100):
            texto = str(lista_produtos[i]['Codigo'])+" "+lista_produtos[i]['Descricao']+" "+str(lista_produtos[i]['Quantidade'])+" "+str(lista_produtos[i]['Valor'])+"\n"
            with open("dados_relat2_produtos.txt", "a", encoding="UTF8") as arq:
                arq.write(texto)
                arq.close()

if (__name__ == "__main__"):
    main()
