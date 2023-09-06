def main():

    lista_alunos = []
    resp = 1

    while (resp != 0):
        print("1-Inserção de um aluno")
        print("2-Alteração de um aluno")
        print("3-Exclusão de um aluno")
        print("4-Exibição de todos os alunos")
        print("5-Ordenação dos alunos pelo nome")
        print("6-Busca Binária pelo nome")
        opc = int(input("Digite a opção desejada (1-5): "))
        if (opc == 1):
            insere_aluno(lista_alunos)
        elif (opc == 2):
            cod = int(input("Digite o código do aluno a ser alterado: "))
            altera_aluno(lista_alunos, cod)
        elif (opc == 3):
            cod = int(input("Digite o código do aluno a ser excluído: "))
            exclui_aluno(lista_alunos, cod)
        elif (opc == 4):
            print(lista_alunos)
        elif (opc == 5):
            bubbleSort(lista_alunos)
            print("Ordenação concluída com sucesso!")
        elif (opc == 6):
            bubbleSort(lista_alunos)
            nome = input("Digite um nome a ser procurado: ")
            pos = buscaBin (lista_alunos,nome)
            if (pos != -1):
                print("O nome está na lista")
                print(lista_alunos[pos])
            else:
                print("O nome não está na lista")

        resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

def insere_aluno (lista_alunos):
    try:
        cod = int(input("Digite o código do aluno: "))
        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")
        disc = input("Digite a disciplina do aluno: ")
        nro_faltas = int(input("Digite a quantidade faltas do aluno: "))
        lista_chk = []
        for i in range(3):
            lista_chk.append(float(input("Digite a nota do checkpoint: ")))
    except ValueError:
        print("Digite valores numéricos")
    else:
        aluno = {'Codigo': cod, 'Nome': nome, 'Curso': curso, 'Disciplina': disc,
                 'Nro_faltas': nro_faltas, 'Checkpoints': lista_chk}
        lista_alunos.append(aluno)
    finally:
        print("Operação finalizada")

def busca_aluno (lista_alunos,cod):
    pos = -1
    for i in range(len(lista_alunos)):
        if (cod == lista_alunos[i]['Codigo']):
            pos = i
    return (pos)

def altera_aluno (lista_alunos,cod):
    pos = busca_aluno(lista_alunos,cod)
    if (pos != -1):  # encontrou o cÃ³digo do aluno no dicionÃ¡rio da lista
        try:
            print(f"Nome do aluno: {lista_alunos[pos]['Nome']}")
            nome = input("Digite o nome do aluno: ")
            print(f"Curso do aluno: {lista_alunos[pos]['Curso']}")
            curso = input("Digite o curso do aluno: ")
            print(f"Disciplina do aluno: {lista_alunos[pos]['Disciplina']}")
            disc = input("Digite a disciplina do aluno: ")
            print(f"Número de faltas do aluno: {lista_alunos[pos]['Nro_faltas']}")
            nro_faltas = int(input("Digite a quantidade faltas do aluno: "))
            print(f"Checkpoints do aluno: {lista_alunos[pos]['Checkpoints']}")
            lista_chk = []
            for i in range(3):
                lista_chk.append(float(input("Digite a nota do checkpoint: ")))
        except ValueError:
            print("Digite valores numéricos")
        else:
            lista_alunos[pos]['Nome'] = nome
            lista_alunos[pos]['Curso'] = curso
            lista_alunos[pos]['Disciplina'] = disc
            lista_alunos[pos]['Nro_faltas'] = nro_faltas
            lista_alunos[pos]['Checkpoints'] = lista_chk
        finally:
            print("Operação finalizada")
    else:
        print("Código não encontrado!")


def exclui_aluno(lista_alunos, cod):
    pos = busca_aluno(lista_alunos, cod)
    if (pos != -1):
        lista_alunos.pop(pos)
        print("Aluno excluído com sucesso!")
    else:
        print("Código não encontrado!")

def bubbleSort (lista_alunos):
    tam= len(lista_alunos)
    for i in range(tam-1,0,-1):
        for j in range(i):
            if lista_alunos[j]['Nome'] > lista_alunos[j+1]['Nome']:
                temp = lista_alunos[j]
                lista_alunos[j] = lista_alunos[j+1]
                lista_alunos[j+1] = temp

def buscaBin (lista_alunos,elem):
    ini = 0
    fim = len(lista_alunos) - 1

    while (ini <= fim):
        meio = int((ini+fim)/2)
        if (lista_alunos[meio]['Nome'] == elem):
            return (meio)
        else:
            if (elem < lista_alunos[meio]['Nome']):
                fim = meio - 1
            else:
                ini = meio + 1
    return(-1)

if (__name__ == "__main__"):
    main()
