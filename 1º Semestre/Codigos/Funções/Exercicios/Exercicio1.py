def main():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    # chamada da função atribuindo o retorno de uma variavel
    maior = retorna_maior(a,b)
    print(f"O maior valor eh {maior}")

    # chamada da função diretamente em um "print"
    print(f"O maior valor eh {retorna_maior(a,b)}")

def retorna_maior(a,b):
    if (a > b):
        return (a)
    else:
        return(b)
    
if (__name__ == "__main__"):
    main()