# escrita em um arquivo texto
# criar o arquivo texto e disponibiliza-lo para escrita
texto = "Sexta-feira é feriado"
with open ("exemplo_texto.txt","w",encoding = "UTF8") as arq:
    arq.write(texto)

# abrir o arquivo texto e acrescentar uma linha linha
texto_novo = "\nDomingo comemora-se a Páscoa"
with open ("exemplo_texto.txt","a",encoding = "UTF8") as arq:
    arq.write(texto_novo)

