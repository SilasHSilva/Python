'''
2) Transforme a função de descontos da Black Friday (20% de desconto ) em uma função 
lambda e aplique a sua coleção. Aperfeiçoe a aplicação escrevendo a 
função lambda diretamente dentro da chamada do MAP.
'''

lista_precos = [230.33,340.20,125.60,560.45,854.30]

lista_precos_desc = list(map(lambda preco : preco - (preco * 0.20), lista_precos))

print(lista_precos_desc)