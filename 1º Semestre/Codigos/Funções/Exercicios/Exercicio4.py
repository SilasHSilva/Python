def main():
    b = int(input("Digite o valor de b: "))

    print(f"O quadrado de {b} eh {calcula_quadrado(b)}")

def calcula_quadrado(b):
    quadrado = b**2 #quadrado = b * b 
    return(quadrado)

if (__name__ == "__main__"):
    main()