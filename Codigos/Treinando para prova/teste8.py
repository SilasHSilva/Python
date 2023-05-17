'''
Construa um programa em Python para preencher uma matriz, de 6 linhas por 6 colunas, com 
elementos do tipo int. Em seguida, o programa deve apresentar, na tela, todos 
os elementos pares contidos na matriz, bem como a posição em que eles se encontram.
'''

matriz = []

for lin in range(3):
    linha = []
    for col in range (3):
        element = int(input("Digite um elemento da matriz: "))
        linha.append(element)
    matriz.append(linha)

for lin in range(3):
    print(matriz[lin])

for lin in range(3):
    for col in range (3):
        if matriz[lin][col] % 2 == 0: #acessando elemento da matriz e verificando se ele é par
            print(f"Esse numero par: {matriz[lin][col]} se encontra na linha {[lin]} coluna {[col]}")
            
        

    