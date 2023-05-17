resp = 1

while(resp!=0):
    print("1-Somar")
    print("2-Subtrair")
    print("3-Multiplicar")
    print("4-Dividir")

    opc = int(input("Digite a opcao (1-4): "))

    if (opc == 1):
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        soma = num1 + num2
        print(f"Resultado: {soma:.2f}")
    elif (opc == 2):
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        sub = num1 - num2
        print(f"Resultado: {sub:.2f}")
    elif (opc == 3):
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        mult = num1 * num2
        print(f"Resultado: {mult:.2f}")
    elif (opc == 4):
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        divisao = num1 / num2
        print(f"Resultado: {divisao:.2f}")
    else:
        print("Opcao invalida!")

    resp = int(input("Deseja continuar (1-SIM / 0-NAO)? "))

