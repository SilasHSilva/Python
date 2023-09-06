lista_precos = [150.30,99.10,70.50,300.30,450.20]

lista_precos_desc = list(map(lambda preco : preco - (preco * 0.20) if (preco > 100) else preco - (preco * 0.10), lista_precos))

print(lista_precos_desc)