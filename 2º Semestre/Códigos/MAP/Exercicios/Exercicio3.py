'''
Uma função que calcule uma nova lista baseada em uma lista de acordo com a seguinte regra: 
quando o elemento da lista for par, adicione 5 a este número e, caso contrário, subtraia 2. 
OBS: estes elementos modificados deverão fazer parte da nova lista.
'''

def main():

    lista = [4,7,2,5,5,8,1]
    nova_lista = list(map(altera_lista,lista))
    print(nova_lista)

def altera_lista(valor):
    if (valor % 2 == 0 ):
        return(valor + 5)
    else:
        return(valor - 2)
    
if (__name__ == "__main__"):
    main()