# Leitura de valores numéricos SEM tratamento de erros

#num1 = int(input("Digite o primeiro número: "))
#num2 = int(input("Digite o segundo número: "))

#divisao = num1 / num2

#print(f"A divisão dos números é {divisao:.2f}")

# Leitura de valores numéricos COM tratamento de erros

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
except ValueError:
    print("Digite valores numéricos para a divisão")
else:
    divisao = num1 / num2
    print(f"A divisão dos números é {divisao:.2f}")
finally:
    print("Operação finalizada")

