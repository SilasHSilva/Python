'''
Uma função que retorne uma nova lista de palavras convertidas para minúsculo baseada em uma lista de palavras.
'''

def main():

    lista_palavras = ["FIAP","TDS","Cazuza","ManGa"]
    lista_minusculas = list(map(converte_minusculo,lista_palavras))

    print(lista_minusculas)

def converte_minusculo(palavra):
    return(palavra.lower())

if (__name__ == "__main__"):
    main()