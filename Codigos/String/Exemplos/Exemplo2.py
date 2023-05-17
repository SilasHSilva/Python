# Funcoes em strings

# Retorna o tamanho (quant. de caracteres) de string

texto = "Aula de Python"

print(len(texto))

# Converter todos os caracteres para minusculo

palavra_minusc = texto.lower()
print(palavra_minusc)

# Converter todos os caracteres para maiusculo

palavra_maiusc = texto.upper()
print(palavra_maiusc)

# separar palavras de um texto

palavras = texto.split(" ")
print(palavras)

# substituir (trocar) palavras de um texto

nova_palavra = texto.replace ("Python" , "Java")
print(nova_palavra)