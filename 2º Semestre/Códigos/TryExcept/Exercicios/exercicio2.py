'''
2) Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os
quais devem conter os seguintes dados:
a. Código
b. Descrição do produto
c. Quantidade em estoque
d. Valor do produto
Faça o tratamento de erros no processo de inserção e alteração. 
As operações deverão ser executadas até que o usuário digite 
uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).
'''

lista_produtos = []
resp = 1

while (resp != 0):
    print("1-Inserção do produto")
    print("2-Alteração do produto")
    print("3-Exclusão do produto")
    print("4-Exibição dos produtos")
    opc = int(input("Digite a opção desejada (1-4): "))

    if (opc == 1):
        try:
            cod = int(input("Digite o código: "))
            descr = input("Digite a descrição: ")
            qtde = int(input("Digite a quantidade: "))
            valor = float(input("Digite o valor: "))
        except ValueError:
            print("Digite um valor numérico")
        else:
            produto = {'Codigo':cod,'Descricao':descr,'Quantidade':qtde,'Valor':valor}
            lista_produtos.append(produto)
        finally:
            print("Operação finalizada")
    elif (opc == 2):
        cod = int(input("Digite o código do produto que deseja alterar: "))
        pos = -1
        for i in range(len(lista_produtos)):
            if (cod == lista_produtos[i]['Codigo']):
                pos = i
        if (pos != -1): # encontrou o código a ser alterado
            try:
                print(f"Descrição: {lista_produtos[pos]['Descricao']}")
                descr = input("Digite a descrição: ")
                print(f"Quantidade: {lista_produtos[pos]['Quantidade']}")
                qtde = int(input("Digite a quantidade: "))
                print(f"Valor: {lista_produtos[pos]['Valor']}")
                valor = float(input("Digite o valor: "))
            except ValueError:
                print("Digite um valor numérico")
            else:
                lista_produtos[pos]['Descricao'] = descr
                lista_produtos[pos]['Quantidade'] = qtde
                lista_produtos[pos]['Valor'] = valor
            finally:
                print("Operação finalizada")
        else:
            print("Código não encontrado!")
    elif (opc == 3):
        cod = int(input("Digite o código do produto que deseja excluir: "))
        pos = -1
        for i in range(len(lista_produtos)):
            if (cod == lista_produtos[i]['Codigo']):
                pos = i
        if (pos != -1):  # encontrou o código a ser excluído
            lista_produtos.pop(pos)
            print("Exclusão realizada com sucesso!")
        else:
            print("Código não encontrado!")
    elif (opc == 4):
        print(lista_produtos)

    resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))