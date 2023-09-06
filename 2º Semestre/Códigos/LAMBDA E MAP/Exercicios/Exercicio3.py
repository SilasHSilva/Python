'''
3) Dada as listas abaixo, transforme a função que calcule o preço 
final de cada item dado os descontos para cada um deles em uma função lambda. 
Aperfeiçoe a aplicação escrevendo a função lambda diretamente dentro da chamada do MAP.
# listaOriginal = [234, 64, 13467, 45.89, 23]
# listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]
'''

listaOriginal = [234, 64, 13467, 45.89, 23]
listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]

lista_precos_desc = list(map(lambda preco,desc : preco - (preco * desc),listaOriginal,listaDescontos))


for i in range(len(lista_precos_desc)):
    print(f"{lista_precos_desc[i]:.2f}")