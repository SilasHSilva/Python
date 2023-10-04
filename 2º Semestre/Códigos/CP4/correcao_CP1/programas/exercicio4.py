'''
Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter dados de
funcionários para o setor de RH de uma determinada empresa de desenvolvimento de software. Os dados a serem
armazenados devem ser os seguintes: nome, CPF, data de nascimento ([dia, mês, ano]: lista), cargo, salário
bruto, desconto INSS (15%), desconto IR (18,95%) e salário líquido (deve ser calculado). Faça o tratamento
de erros no processo de inserção e alteração. As operações deverão ser executadas até que o usuário digite
uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). OBS: o programa deve ter, obrigatoriamente, a função
“main” e as operações devem ser definidas em funções (modularização).
'''

def main():

    lista_funcionarios = []
    resp = 1

    while (resp != 0):
        print("1-InserÃ§Ã£o de um funcionÃ¡rio")
        print("2-AlteraÃ§Ã£o de um funcionÃ¡rio")
        print("3-ExclusÃ£o de um funcionÃ¡rio")
        print("4-ExibiÃ§Ã£o de todos os funcionÃ¡rios")

        opc = int(input("Digite a opÃ§Ã£o desejada (1-4): "))
        if (opc == 1):
            insere_funcionario(lista_funcionarios)
        elif (opc == 2):
            cod = input("Digite o cÃ³digo do funcionÃ¡rio a ser alterado: ")
            altera_funcionario(lista_funcionarios, cod)
        elif (opc == 3):
            cod = input("Digite o cÃ³digo do funcionÃ¡rio a ser excluÃ­do: ")
            exclui_funcionario(lista_funcionarios, cod)
        elif (opc == 4):
            print(lista_funcionarios)


        resp = int(input("Deseja continuar (1-SIM / 0-NÃƒO)? "))

def insere_funcionario (lista_funcionarios):
    try:

        nome = input("Digite o nome do funcionÃ¡rio: ")
        cpf = input("Digite o cpf do funcionario: ")
        lista_datanasc = []
        lista_datanasc.append(int(input("Dia de nasc: ")))
        lista_datanasc.append(int(input("Mês de nasc: ")))
        lista_datanasc.append(int(input("Ano de nasc: ")))
        cargo = input("Digite o cargo do funcionario: ")
        sal_bruto = float(input("Digite o salário bruto do funcionário: "))
        desc_INSS = sal_bruto * 0.15
        desc_IR = sal_bruto * 0.1895
        sal_liquido = sal_bruto - desc_INSS - desc_IR

    except ValueError:
        print("Digite valores numÃ©ricos")
    else:
        funcionario = {'Nome': nome, 'Cpf': cpf,'Data_Nasc':lista_datanasc, 'Cargo':cargo,
                       'Salario_bruto':sal_bruto,'Desc_INSS':desc_INSS,'Desc_IR':desc_IR,'Salario_liq':sal_liquido}
        lista_funcionarios.append(funcionario)
    finally:
        print("OperaÃ§Ã£o finalizada")

def busca_funcionario (lista_funcionarios,cpf):
    pos = -1
    for i in range(len(lista_funcionarios)):
        if (cpf == lista_funcionarios[i]['Cpf']):
            pos = i
    return (pos)

def altera_funcionario (lista_funcionarios,cpf):
    pos = busca_funcionario(lista_funcionarios, cpf)

    if (pos != -1):  # encontrou o cÃƒÆ’Ã‚Â³digo do funcionÃ¡rio no dicionÃƒÆ’Ã‚Â¡rio da lista
        try:
            print(f"Nome do funcionÃ¡rio: {lista_funcionarios[pos]['Nome']}")
            nome = input("Digite o nome do funcionÃ¡rio: ")
            print(f"Data de Nascimento: {lista_funcionarios[pos]['Data_Nasc']}")
            lista_datanasc = []
            lista_datanasc.append(int(input("Dia de nasc: ")))
            lista_datanasc.append(int(input("Mês de nasc: ")))
            lista_datanasc.append(int(input("Ano de nasc: ")))
            print(f"Cargo do funcionÃ¡rio: {lista_funcionarios[pos]['Cargo']}")
            cargo = input("Digite o cargo do funcionÃ¡rio: ")
            print(f"Salário bruto do funcionÃ¡rio: {lista_funcionarios[pos]['Salario_bruto']:.2f}")
            sal_bruto = float(input("Digite o salário bruto do funcionÃ¡rio: "))
            desc_INSS = sal_bruto * 0.15
            desc_IR = sal_bruto * 0.1895
            sal_liquido = sal_bruto - desc_INSS - desc_IR

        except ValueError:
            print("Digite valores numÃ©ricos")
        else:
            lista_funcionarios[pos]['Nome'] = nome
            lista_funcionarios[pos]['Data_Nasc'] = lista_datanasc
            lista_funcionarios[pos]['Cargo'] = cargo
            lista_funcionarios[pos]['Salario_bruto'] = sal_bruto
            lista_funcionarios[pos]['Desc_INSS'] = desc_INSS
            lista_funcionarios[pos]['Desc_IR'] = desc_IR
            lista_funcionarios[pos]['Salario_liq'] = sal_liquido
        finally:
            print("OperaÃ§Ã£o finalizada")
    else:
        print("CÃ³digo nÃ£o encontrado!")

def exclui_funcionario (lista_funcionarios, cpf):
    pos = busca_funcionario(lista_funcionarios, cpf)
    if (pos != -1):
        lista_funcionarios.pop(pos)
        print("FuncionÃ¡rio excluÃ­do com sucesso!")
    else:
        print("CÃ³digo nÃ£o encontrado!")



if (__name__ == "__main__"):
    main()

