palavra = input("Digite uma palavra: ")

palavra_contra = palavra[::-1]

if (palavra == palavra_contra):
    print("Essa palavra é um palíndromo!")
else:
    print("Essa palavra nao eh um palíndromo")



