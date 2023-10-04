def main():

    lista_imoveis= []
    resp = 1

    while (resp != 0):
        print("1-Inserção de um imovel")
        print("2-Alteração de um imovel")
        print("3-Exclusão de um imovel")
        print("4-Exibição de todos os imoveis")
        opc = int(input("Digite a opção desejada (1-4): "))
        if (opc == 1):
            insere_imovel(lista_imoveis)
        elif (opc == 2):
            cod = int(input("Digite o código do imovel a ser alterado: "))
            altera_imovel(lista_imoveis, cod)
        elif (opc == 3):
            cod = int(input("Digite o código do imovel a ser excluído: "))
            exclui_imovel(lista_imoveis, cod)
        elif (opc == 4):
            print(lista_imoveis)

        resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

def insere_imovel (lista_imoveis):
    try:
        cod = int(input("Digite o código do imovel: "))
        tipo = input("Digite o tipo do imovel: ")
        local = input("Digite a localização do imovel: ")
        bairro = input("Digite o bairro do imovel: ")
        metragem = float(input("Digite a metragem do imovel: "))
        valor = float(input("Digite o valor do imovel: "))

    except ValueError:
        print("Digite valores numéricos")
    else:
        imovel = {'Codigo': cod, 'Tipo': tipo, 'Localizacao': local,
                   'Bairro': bairro, 'Metragem':metragem, 'Valor':valor}
        lista_imoveis.append(imovel)
    finally:
        print("Operação finalizada")

def busca_imovel (lista_imoveis,cod):
    pos = -1
    for i in range(len(lista_imoveis)):
        if (cod == lista_imoveis[i]['Codigo']):
            pos = i
    return (pos)

def altera_imovel (lista_imoveis,cod):
    pos = busca_imovel(lista_imoveis, cod)

    if (pos != -1):  # encontrou o cÃƒÂ³digo do imovel no dicionÃƒÂ¡rio da lista
        try:

            print(f"Tipo do imovel: {lista_imoveis[pos]['Tipo']}")
            tipo = input("Digite o tipo do imovel: ")
            print(f"Localização do imovel: {lista_imoveis[pos]['Localizacao']}")
            local = input("Digite a localização do imovel: ")
            print(f"Bairro do imovel: {lista_imoveis[pos]['Bairro']}")
            bairro = input("Digite o bairro do imovel: ")
            print(f"Metragem do imovel: {lista_imoveis[pos]['Metragem']}")
            metr = float(input("Digite a metragem do imovel: "))
            print(f"Valor do imovel: {lista_imoveis[pos]['Valor']}")
            valor = float(input("Digite o valor do imovel: "))

        except ValueError:
            print("Digite valores numéricos")
        else:

            lista_imoveis[pos]['Tipo'] = tipo
            lista_imoveis[pos]['Localizacao'] = local
            lista_imoveis[pos]['Bairro'] = bairro
            lista_imoveis[pos]['Metragem'] = metr
            lista_imoveis[pos]['Valor'] = valor
        finally:
            print("Operação finalizada")
    else:
        print("Código não encontrado!")

def exclui_imovel (lista_imoveis, cod):
    pos = busca_imovel(lista_imoveis, cod)
    if (pos != -1):
        lista_imoveis.pop(pos)
        print("imovel excluído com sucesso!")
    else:
        print("Código não encontrado!")

if (__name__ == "__main__"):
    main()
