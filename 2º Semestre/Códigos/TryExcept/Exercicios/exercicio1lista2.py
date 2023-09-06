lista_alunos = []
resp = 1

while (resp != 0):
    print("1-Inserção de um aluno")
    print("2-Alteração de um aluno")
    print("3-Exclusão de um aluno")
    print("4-Exibição de todos aluno")
    opc = int(input("Digite a opção desejada (1-4): "))
    if (opc == 1):
        try:
            cod = int(input("Digite o código do aluno: "))
            nome = input("Digite o nome do aluno: ")
            curso = input("Digite o curso do aluno: ")
            disc = input("Digite a disciplina do aluno: ")
            nro_faltas = int(input("Digite a quantidade de faltas do aluno: "))
            lista_chk = []
            for i in range(3):
                lista_chk.append(float(input("Digite a nota do checkpoint: ")))
        except ValueError:
            print("Digite valores numéricos")
        else:
            aluno = {'Codigo': cod,'Nome': nome,'Curso': curso,'Disciplina':disc,
                    'Numero de faltas': nro_faltas,'Checkpoints':lista_chk}
            lista_alunos.append(aluno)
        finally:
            print("operação finalizada")
    elif(opc == 2):
        cod = int(input("Digite o codigo do aluno a ser alterado: "))
        pos = -1
        for i in range(len(lista_alunos)):
            if(cod == lista_alunos[i]['Codigo']):
                pos=i
        if(pos != -1): #encontrou o código do aluno no dicionário da lista
            try:
                print(f"Nome do aluno: {lista_alunos[pos]['Nome']} ")
                nome = input("Digite o nome do aluno: ")
                print(f"Curso do aluno: {lista_alunos[pos]['Curso']} ")
                curso = input(f"Digite o curso do aluno: ")
                print(f"Disciplina do aluno: {lista_alunos[pos]['Disciplina']} ")
                disc = input("Digite a disciplina do aluno: ")
                print(f"Numero de faltas do aluno: {lista_alunos[pos]['Numero de faltas']} ")
                nro_faltas = int(input("Digite a quantidade de faltas do aluno: "))
                print(f"Checkpoints do aluno: {lista_alunos[pos]['Checkpoints']} ")
                lista_chk = []
                for i in range(3):
                    lista_chk.append(float(input("Digite a nota do checkpoint: ")))
            except ValueError:
                print("Digite valores numericos")
            else:
                lista_alunos[pos]['Nome'] = nome
                lista_alunos[pos]['Curso'] = curso
                lista_alunos[pos]['Disciplina'] = disc
                lista_alunos[pos]['Numero de faltas'] = nro_faltas
                lista_alunos[pos]['Checkpoints'] = lista_chk
            finally:
                print("Alteração realizada com sucesso")
        else:
            print("Codigo não encontrado")

    elif(opc == 3):
        cod = int(input("Digite o codigo do aluno a ser alterado: "))
        pos = -1
        for i in range(len(lista_alunos)):
            if(cod == lista_alunos[i]['Codigo']):
                pos=i
        
        if(pos != -1):
            lista_alunos.pop(pos)
            print("Aluno excluido com sucesso")
        else:
            print("Codigo não encontrado")
        
    elif(opc == 4):
        print(lista_alunos)
    
    resp = int(input("Deseja continuar 1 - Sim / 0 - Não"))

        
