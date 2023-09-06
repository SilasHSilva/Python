def main():
    n = int(input("Digite o valor de n: "))

    if (verifica_par_impar(n) == 1):
        print("O numero é par")
    else:
        print("O numero é impar")

def verifica_par_impar(n):
    if(n % 2 == 0):
        return(1)
    else:
        return(0)

if (__name__ == "__main__"):
    main()