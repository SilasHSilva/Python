def main():

    lista_medicamentos = []
    resp = 1

    while (resp != 0):
        print("1-Inserção de um medicamento")
        print("2-Alteração de um medicamento")
        print("3-Exclusão de um medicamento")
        print("4-Exibição de todos os medicamentos")
        opc = int(input("Digite a opção desejada (1-4): "))
        if (opc == 1):
            insere_medicamento(lista_medicamentos)
        elif (opc == 2):
            cod = int(input("Digite o código do medicamento a ser alterado: "))
            altera_medicamento(lista_medicamentos, cod)
        elif (opc == 3):
            cod = int(input("Digite o código do medicamento a ser excluído: "))
            exclui_medicamento(lista_medicamentos, cod)
        elif (opc == 4):
            print(lista_medicamentos)

        resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

def insere_medicamento (lista_medicamentos):
    try:
        cod = int(input("Digite o código do medicamento: "))
        nome = input("Digite o nome do medicamento: ")
        indic = input("Digite a indicação do medicamento: ")
        mes = int(input("Digite o mês de validade do medicamento: "))
        ano = int(input("Digite o ano de validade do medicamento: "))
        valor = float(input("Digite o valor do medicamento: "))

    except ValueError:
        print("Digite valores numéricos")
    else:
        medicamento = {'Codigo': cod, 'Nome': nome, 'Indicacao': indic,
                   'Mes_validade': mes, 'Ano_validade':ano, 'Valor':valor}
        lista_medicamentos.append(medicamento)
    finally:
        print("Operação finalizada")

def busca_medicamento (lista_medicamentos,cod):
    pos = -1
    for i in range(len(lista_medicamentos)):
        if (cod == lista_medicamentos[i]['Codigo']):
            pos = i
    return (pos)

def altera_medicamento (lista_medicamentos,cod):
    pos = busca_medicamento(lista_medicamentos, cod)

    if (pos != -1):  # encontrou o cÃƒÂ³digo do medicamento no dicionÃƒÂ¡rio da lista
        try:
            print(f"Nome do medicamento: {lista_medicamentos[pos]['Nome']}")
            nome = input("Digite o nome do medicamento: ")
            print(f"Indicação do medicamento: {lista_medicamentos[pos]['Indicacao']}")
            indic = input("Digite a indicação do medicamento: ")
            print(f"Mês de validade do medicamento: {lista_medicamentos[pos]['Mes_validade']}")
            mes = int(input("Digite o mês de validade do medicamento: "))
            print(f"Ano de validade do medicamento: {lista_medicamentos[pos]['Ano_validade']}")
            ano = int(input("Digite o ano de validade do medicamento: "))
            print(f"Valor do medicamento: {lista_medicamentos[pos]['Valor']}")
            valor = float(input("Digite o valor do medicamento: "))

        except ValueError:
            print("Digite valores numéricos")
        else:
            lista_medicamentos[pos]['Nome'] = nome
            lista_medicamentos[pos]['Indicacao'] = indic
            lista_medicamentos[pos]['Mes_validade'] = mes
            lista_medicamentos[pos]['Ano_validade'] = ano
            lista_medicamentos[pos]['Valor'] = valor
        finally:
            print("Operação finalizada")
    else:
        print("Código não encontrado!")

def exclui_medicamento (lista_medicamentos, cod):
    pos = busca_medicamento(lista_medicamentos, cod)
    if (pos != -1):
        lista_medicamentos.pop(pos)
        print("medicamento excluído com sucesso!")
    else:
        print("Código não encontrado!")

if (__name__ == "__main__"):
    main()
