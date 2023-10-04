def main:

    lista_carros = []
    resp = 1

    while (resp != 0):
        print()





def insere_carro(lista_carros):
    try:
        ident = int(input("Digite o identificador(numerico) do carro: "))
        nome = input("Digite o nome do carro: ")
        marca = input("Digite a marca do carro: ")
        placa = input("Digite a placa do carro: ")
        ano = int(input("Digite o ano do carro"))
    except(ValueError):
        print("Digite um valor númerico!")
    else:
        carro = {"Nome":nome, "Marca": marca,"placa": placa, "Ano": ano,"Identificador": ident}
        lista_carros.append(carro)
    finally:
        print("Operação finalizada")

def busca_carro(lista_carros,ident):
    pos = -1
    for i in range(len(lista_carros)):
        if ident == lista_carros[i]["identificador"]:
            pos = i
    return pos

def altera_carro(lista_carros,ident):
    pos = busca_carro(lista_carros,ident)
    if(pos != -1):
        try:
             print(f"Nome do carro: {lista_carros[pos]['Nome']}")
             nome = input("Digite o nome do carro: ")
             print(f"Marca do carro: {lista_carros[pos]['Marca']}")
             marca = input("Digite a marca do carro: ")
             print(f"Placa do carro: {lista_carros[pos]['Placa']}")
             placa = input("Digite a placa do carro: ")
             print(f"Ano do carro: {lista_carros[pos]['Ano']}")
             ano = int(input("Digite o ano do carro"))
        except ValueError:
            print("Digite um valor númerico")
        else:
            lista_carros[pos]['Nome'] = nome
            lista_carros[pos]['Marca'] = marca
            lista_carros[pos]['Placa'] = placa
            lista_carros[pos]['Ano'] = ano
        finally:
            print("Operação finalizada")

def exlui_funcionario(lista_carros,identi):
    pos = busca_carro(lista_carros,identi)
    if (pos != -1):
        lista_carros.pop(pos)
        print("Carro excluído com sucesso!")
    else:
        print("Código não encontrado!")

def grava_txt (lista_carros):

    for i in range (len(lista_carros)):
        texto = str(lista_carros[i]['Identificador'] + " " +
                    str(lista_carros[i]['Nome'] + " " +
                        str(lista_carros[i]['Marca'] + " " +
                            str(lista_carros[i]['Placa'] + " " +
                                str(lista_carros[i]['Ano'])))))
        with open("Dados_carros.txt","a",encoding="utf8") as arq:
            arq.write(texto)
            arq.close()

if __name__ == '__main__':
    main()