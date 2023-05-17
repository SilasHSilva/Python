listas_numeros = []

for i in range(10):
    lista_numeros.append(int(input("Digite um numero: ")))

maior = lista_numeros[0]
pos_maior = 0 
for i in range(10):
    if (lista_numeros[i] > maior):
        maior = listas_numeros[i]
        pos_maior = i

print(f"O maior elemento da lista eh {maior}, que esta na posicao {pos_maior}")