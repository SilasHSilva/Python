lista_palavras_ing = []
lista_palavras_port = []

resp = 1

while (resp != 0):
    lista_palavras_ing.append(input("Digite uma palavra em ingles: "))
    lista_palavras_port.append(input("Digite uma palavra em portugues: "))

    resp = int(input("Deseja continuar (1 - SIM / 0 - NAO)"))

palavra = input("Digite a palavra em ingles a ser traduzida: ")

if (palavra in lista_palavras_ing):
    pos_palavra = lista_palavras_ing.index(palavra)
    print(f"A palavra em portugues eh {lista_palavras_port[pos_palavra]}")