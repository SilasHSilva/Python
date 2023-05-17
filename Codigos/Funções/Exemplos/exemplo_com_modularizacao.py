def main():
    resp = 1

    while (resp != 0):
        print("1-Somar")
        print("2-Subtrair")
        print("3-Multiplicar")
        print("4-Dividir")

        opc = int(input("Digite a opcao (1-4): "))

        if (opc == 1):
            num1,num2 = leitura()
            soma = calcula_soma(num1, num2)
            exibe_resultado(soma)
        elif (opc == 2):
            num1,num2 = leitura()
            sub = calcula_subtracao(num1, num2)
            exibe_resultado(sub)
        elif (opc == 3):
            num1,num2 = leitura()
            mult = calcula_multiplicacao(num1, num2)
            exibe_resultado(mult)
        elif (opc == 4):
            num1,num2 = leitura()
            divisao = calcula_divisao(num1, num2)
            exibe_resultado(divisao)
        else:
            print("Opcao invalida")

        resp = int(input("Deseja continuar (1-SIM / 0-NAO)? "))


def leitura():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    return(num1,num2)

def calcula_soma (num1,num2):
    soma = num1 + num2
    return(soma)

def calcula_subtracao (num1,num2):
    sub = num1 - num2
    return(sub)

def calcula_multiplicacao (num1,num2):
    mult = num1 * num2
    return(mult)

def calcula_divisao (num1,num2):
    div = num1 / num2
    return(div)

def exibe_resultado (res):
    print(f"Resultado: {res:.2f}")

if (__name__ == "__main__"):
    main()

