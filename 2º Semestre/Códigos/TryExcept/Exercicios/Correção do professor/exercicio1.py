def main():

    lista_funcionarios = []
    resp = 1

    while (resp != 0):
        print("1-Inserção de um funcionário")
        print("2-Alteração de um funcionário")
        print("3-Exclusão de um funcionário")
        print("4-Exibição de todos os funcionários")
        print("5-Ordenação dos funcionários por nome")
        print("6-Busca Binária por nome")
        print("7-Funcionários com idade superior a 25 anos, ordenados por idade")
        print("8-Funcionários com idade entre 22 e 35 anos, ordenados por salário, cujo salário seja maior do que R$3700,00")
        opc = int(input("Digite a opção desejada (1-8): "))
        if (opc == 1):
            insere_funcionario(lista_funcionarios)
        elif (opc == 2):
            cod = int(input("Digite o código do funcionário a ser alterado: "))
            altera_funcionario(lista_funcionarios, cod)
        elif (opc == 3):
            cod = int(input("Digite o código do funcionário a ser excluído: "))
            exclui_funcionario(lista_funcionarios, cod)
        elif (opc == 4):
            bubbleSort(lista_funcionarios, "Codigo")
            print(lista_funcionarios)
        elif (opc == 5):
            bubbleSort(lista_funcionarios,"Nome")
            print("Ordenação concluída com sucesso!")
        elif (opc == 6):
            bubbleSort(lista_funcionarios,"Nome")
            nome = input("Digite um nome a ser procurado: ")
            pos = buscaBin (lista_funcionarios,nome)
            if (pos != -1):
                print("O nome está na lista")
                print(lista_funcionarios[pos])
            else:
                print("O nome não está na lista")
        elif (opc == 7):
            if (len(lista_funcionarios) > 0):
                relatorio_1(lista_funcionarios)
        elif (opc == 8):
            if (len(lista_funcionarios) > 0):
                relatorio_2(lista_funcionarios)

        resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

def insere_funcionario (lista_funcionarios):
    try:
        cod = int(input("Digite o código do funcionário: "))
        nome = input("Digite o nome do funcionário: ")
        idade = int(input("Digite a idade do funcionário: "))
        salario = float(input("Digite o salário do funcionário: "))

    except ValueError:
        print("Digite valores numéricos")
    else:
        funcionario = {'Codigo': cod, 'Nome': nome, 'Idade': idade,
                   'Salario': salario}
        lista_funcionarios.append(funcionario)
    finally:
        print("Operação finalizada")

def busca_funcionario (lista_funcionarios,cod):
    pos = -1
    for i in range(len(lista_funcionarios)):
        if (cod == lista_funcionarios[i]['Codigo']):
            pos = i
    return (pos)

def altera_funcionario (lista_funcionarios,cod):
    pos = busca_funcionario(lista_funcionarios, cod)

    if (pos != -1):  # encontrou o cÃƒÂ³digo do funcionário no dicionÃƒÂ¡rio da lista
        try:
            print(f"Nome do funcionário: {lista_funcionarios[pos]['Nome']}")
            nome = input("Digite o nome do funcionário: ")
            print(f"Idade do funcionário: {lista_funcionarios[pos]['Idade']}")
            idade = int(input("Digite a idade do funcionário: "))
            print(f"Salário do funcionário: {lista_funcionarios[pos]['Salario']}")
            salario = float(input("Digite o salário do funcionário: "))

        except ValueError:
            print("Digite valores numéricos")
        else:
            lista_funcionarios[pos]['Nome'] = nome
            lista_funcionarios[pos]['Idade'] = idade
            lista_funcionarios[pos]['Salario'] = salario
        finally:
            print("Operação finalizada")
    else:
        print("Código não encontrado!")

def exclui_funcionario (lista_funcionarios, cod):
    pos = busca_funcionario(lista_funcionarios, cod)
    if (pos != -1):
        lista_funcionarios.pop(pos)
        print("Funcionário excluído com sucesso!")
    else:
        print("Código não encontrado!")

def bubbleSort (lista_funcionarios,chave):
    tam= len(lista_funcionarios)
    for i in range(tam-1,0,-1):
        for j in range(i):
            if lista_funcionarios[j][chave] > lista_funcionarios[j+1][chave]:
                temp = lista_funcionarios[j]
                lista_funcionarios[j] = lista_funcionarios[j+1]
                lista_funcionarios[j+1] = temp

def buscaBin (lista_funcionarios,elem):
    ini = 0
    fim = len(lista_funcionarios) - 1

    while (ini <= fim):
        meio = int((ini+fim)/2)
        if (lista_funcionarios[meio]['Nome'] == elem):
            return (meio)
        else:
            if (elem < lista_funcionarios[meio]['Nome']):
                fim = meio - 1
            else:
                ini = meio + 1
    return(-1)

def relatorio_1 (lista_funcionarios):
    bubbleSort(lista_funcionarios, "Idade")

    for i in range(len(lista_funcionarios)):
        if (lista_funcionarios[i]['Idade'] > 25):
            print(lista_funcionarios[i])

def relatorio_2 (lista_funcionarios):
    bubbleSort(lista_funcionarios, "Salario")

    for i in range(len(lista_funcionarios)):
        if (lista_funcionarios[i]['Idade'] >= 22 and lista_funcionarios[i]['Idade'] <= 35 and lista_funcionarios[i]['Salario'] > 3700):
            print(lista_funcionarios[i])

if (__name__ == "__main__"):
    main()
