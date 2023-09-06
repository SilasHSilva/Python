# Percorrer uma string

frase = "Hoje é quarta-feira"

tam = len(frase)

for i in range (tam):
    print(frase[i])

# inverter uma string (notacao slice)

palavra = "Fiap"

palavra_invertida = palavra[::-1]
print(palavra_invertida)