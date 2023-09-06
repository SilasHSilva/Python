resp = 1
lista_usuarios = []

while (resp != 0):
    print("1-Inserir usuário")
    print("2-Alterar usuário")
    print("3-Remover usuário")
    print("4-Exibir usuários")
    opc = int(input("Digite a opção desejada (1-4): "))

    if (opc == 1):
        try:
            cod = int(input("Digite o código do usuário: "))
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))
            senha = input("Digite a senha do usuário: ")
        except ValueError:
            print("Digite um valor numérico")
        else:
            usuario = {'Codigo':cod, 'Nome':nome, 'Idade':idade, 'Senha':senha}
            lista_usuarios.append(usuario)
        finally:
            print("Operação finalizada")
    elif (opc == 2):
        cod = int(input("Digite um código que deseja alterar: "))
        pos = -1
        # busca do código dentro do dicionário da lista
        for i in range (len(lista_usuarios)):
            if (lista_usuarios[i]['Codigo'] == cod):
                pos = i
        if (pos != -1): # o código foi encontrado
             try:
                nome = input("Digite o nome do usuário: ")
                idade = int(input("Digite a idade do usuário: "))
                senha = input("Digite a senha do usuário: ")
             except ValueError:
                print("Digite um valor numérico")
             else:
                lista_usuarios[pos]['Nome'] = nome
                lista_usuarios[pos]['Idade'] = idade
                lista_usuarios[pos]['Senha'] = senha
             finally:
                print("Operação finalizada")
        else:
            print("Usuário não encontrado")
    elif (opc == 3):
        cod = int(input("Digite um código que deseja excluir: "))
        pos = -1
        # busca do código dentro do dicionário da lista
        for i in range (len(lista_usuarios)):
            if (lista_usuarios[i]['Codigo'] == cod):
                pos = i
        if (pos != -1):
            lista_usuarios.pop(pos)
        else:
            print("Usuário não encontrado")
    elif (opc == 4):
        print(lista_usuarios)

    resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

