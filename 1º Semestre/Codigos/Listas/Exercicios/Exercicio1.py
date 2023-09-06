lista_numeros = []

for i in range(10):
    num = int(input("Digite um numero: "))
    lista_numeros.append(num)

maior = lista_numeros[0]
pos_maior = 0 
for i in range(10):
    if (lista_numeros[i] > maior):
        maior = lista_numeros[i]
        pos_maior = i

print(lista_numeros)
print(f"O maior elemento da lista eh {maior}, que esta na posicao {pos_maior}")