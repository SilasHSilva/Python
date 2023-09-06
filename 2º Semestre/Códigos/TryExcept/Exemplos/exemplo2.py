# Divisão dos números SEM tratamento de erros

#num1 = int(input("Digite o primeiro número: "))
#num2 = int(input("Digite o segundo número: "))

#divisao = num1 / num2

#print(f"A divisão dos números é {divisao:.2f}")

# Divisão dos números COM tratamento de erros

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    divisao = num1 / num2
except ValueError:
    print("Digite valores numéricos para a divisão")
except ZeroDivisionError:
    print("Digite um valor diferente de zero para dividir")
else:
    print(f"A divisão dos números é {divisao:.2f}")
finally:
    print("Operação finalizada")

