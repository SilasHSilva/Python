soma_salarios = 0
qtde_habitantes = 0
soma_nrofilhos = 0
qtde_salariomenor1500 = 0

salario = float(input("Digite o salario do habitante: "))

while (salario >= 0):
    soma_salarios+=salario
    qtde_habitantes+=1
    nro_filhos = int(input("Digite o numero de filhos do habitante: "))
    soma_nrofilhos+=nro_filhos
    if (salario < 1500):
        qtde_salariomenor1500+=1
    if (qtde_habitantes==1):
        maior_salario = salario
    else:
        if (salario > maior_salario):
            maior_salario = salario

    salario = float(input("Digite o salario do habitante: "))

media_salario = soma_salarios / qtde_habitantes
media_nrofilhos = soma_nrofilhos / qtde_habitantes
percent_salariomenor1500 = (qtde_salariomenor1500 * 100) / qtde_habitantes

print(f"Media dos salarios: {media_salario:.2f}")
print(f"Media do nro de filhos: {media_nrofilhos:.2f}")
print(f"Maior salario: {maior_salario:.2f}")
print(f"Percentual de pessoas com salário menor que R$ 1500,00: {percent_salariomenor1500:.2f}")
