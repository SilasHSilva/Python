def main():
    num1 = int(input("Digite o valor de num1: "))
    num2 = int(input("Digite o valor de num2: "))
    print(f"A soma dos numeros eh: {soma_numeros(num1,num2)}")

    n = int(input("Digite o valor de n: "))
    verificar_parimpar(n)

    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    print(f"O maior numero eh: {retorna_maior (x,y)}")

def soma_numeros(num1,num2):
    soma = num1 + num2
    return(soma)

def verificar_parimpar(n):
    if(n % 2 == 0):
        print("O numero eh par")
    else:
        print("O numero eh impar")

def retorna_maior(x,y):
    if(x > y):
        return(x)
    else:
        return(y)
    
if (__name__ == "__main__"):
    main()