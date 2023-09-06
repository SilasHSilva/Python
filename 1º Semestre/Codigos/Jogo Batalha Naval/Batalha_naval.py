matriz = []
n_linhas = 0
n_colunas = 0

for lin in range(2):
    linha = []
    for col in range(2):
        linha.append(int(input(f"Digite: {lin} {col}")))
    matriz.append(linha)

for lin in range(2):
    print(matriz[lin])

print("Diga onde está o numero 1")

lin = input("Digite a linha")
col = input("Digite a coluna")

jogada = (matriz[lin][col])

if jogada == 1:
    print("Sim")
else:
    print("não")

