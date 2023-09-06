lista_clientes = []
resp = 1

while (resp != 0):
    print("1-Inserção de um cliente")
    print("2-Alteração de um cliente")
    print("3-Exclusão de um cliente")
    print("4-Exibição de todos os clientes")
    opc = int(input("Digite a opção desejada (1-4): "))
    if (opc == 1):
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
            cliente = {'Codigo':cod,'Nome':nome,'Cpf':cpf,'Idade':idade,
                     'Endereco':endereco,'Limite_credito':limite_credito}
            lista_clientes.append(cliente)
        finally:
            print("Operação finalizada")
    elif (opc == 2):
        cod = int(input("Digite o código do cliente a ser alterado: "))
        pos = -1
        for i in range(len(lista_clientes)):
            if (cod == lista_clientes[i]['Codigo']):
                pos = i
        if (pos != -1): #encontrou o código do cliente no dicionário da lista
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
    elif (opc == 3):
        cod = int(input("Digite o código do cliente a ser excluído: "))
        pos = -1
        for i in range(len(lista_clientes)):
            if (cod == lista_clientes[i]['Codigo']):
                pos = i
        if (pos != -1):
            lista_clientes.pop(pos)
            print("cliente excluído com sucesso!")
        else:
            print("Código não encontrado!")
    elif (opc == 4):
        print(lista_clientes)

    resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))
