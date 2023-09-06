precos_unitarios = [230.00,340.50,130.95,460.33,860.50]
qtde_vendidas = [3,2,5,1,2]
descontos = [0.20,0.15,0.04,0.50,0.25]

lista_precosfinais = list(map(lambda preco,qtde,desc : (qtde*preco) - ((qtde*preco)*(desc)),precos_unitarios,qtde_vendidas,descontos))

print(lista_precosfinais)