'''
1) Escreva um programa em Python que faça um 
CRUD em uma lista de dicionários, os quais devem conter os seguintes dados:
a. Código
b. Nome do funcionário
c. Idade do funcionário
d. Salário do funcionário
Faça o tratamento de erros no processo de inserção e alteração. 
As operações deverão ser executadas até que o usuário 
digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).
'''

lista_funcionarios = []
resp = 1

while (resp != 0):
    print("1-Inserção do funcionário")
    print("2-Alteração do funcionário")
    print("3-Exclusão do funcionário")
    print("4-Exibição dos funcionários")
    opc = int(input("Digite a opção desejada (1-4): "))

    if (opc == 1):
        try:
            cod = int(input("Digite o código: "))
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            salario = float(input("Digite o salário: "))
        except ValueError:
            print("Digite um valor numérico")
        else:
            func = {'Codigo':cod,'Nome':nome,'Idade':idade,'Salario':salario}
            lista_funcionarios.append(func)
        finally:
            print("Operação finalizada")
    elif (opc == 2):
        cod = int(input("Digite o código do funcionário que deseja alterar: "))
        pos = -1
        for i in range(len(lista_funcionarios)):
            if (cod == lista_funcionarios[i]['Codigo']):
                pos = i
        if (pos != -1): # encontrou o código a ser alterado
            try:
                print(f"Nome: {lista_funcionarios[pos]['Nome']}")
                nome = input("Digite o nome: ")
                print(f"Idade: {lista_funcionarios[pos]['Idade']}")
                idade = int(input("Digite a idade: "))
                print(f"Salário: {lista_funcionarios[pos]['Salario']}")
                salario = float(input("Digite o salário: "))
            except ValueError:
                print("Digite um valor numérico")
            else:
                lista_funcionarios[pos]['Nome'] = nome
                lista_funcionarios[pos]['Idade'] = idade
                lista_funcionarios[pos]['Salario'] = salario
            finally:
                print("Operação finalizada")
        else:
            print("Código não encontrado!")
    elif (opc == 3):
        cod = int(input("Digite o código do funcionário que deseja excluir: "))
        pos = -1
        for i in range(len(lista_funcionarios)):
            if (cod == lista_funcionarios[i]['Codigo']):
                pos = i
        if (pos != -1):  # encontrou o código a ser excluído
            lista_funcionarios.pop(pos)
            print("Exclusão realizada com sucesso!")
        else:
            print("Código não encontrado!")
    elif (opc == 4):
        print(lista_funcionarios)

    resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))




