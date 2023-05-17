def main():
    x = int(input("Digite o valor de x: "))

    print(f"O dobro de {x} eh {calcula_dobro(x)}")

def calcula_dobro(x):
    dobro = 2 * x
    return (dobro)

if (__name__ == "__main__"):
    main()