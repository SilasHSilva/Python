soma_salarios = 0

nome_empresa = input("Digite o nome da empresa: ")

for cont in range (5):
    nome = input("Digite o nome do funcionario "+str(cont+1)+" :")
    salario = float(input("Digite o salario do funcionario "+str(cont+1)+" :"))
    soma_salarios+=salario
    if (cont == 0):
        maior_salario = salario
        menor_salario = salario
        nome_maior_salario = nome
        nome_menor_salario = nome
    else:
        if (salario > maior_salario):
            maior_salario = salario
            nome_maior_salario = nome
        if (salario < menor_salario):
            menor_salario = salario
            nome_menor_salario = nome

media = soma_salarios / 5

print(f"A media salarial dos funcionarios da empresa {nome_empresa} eh {media:.2f}")
print(f"{nome_menor_salario} recebe o menor salario que corresponde a {menor_salario:.2f}")
print(f"{nome_maior_salario} recebe o maior salario que corresponde a {maior_salario:.2f}")
