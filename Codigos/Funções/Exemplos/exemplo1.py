# Funcao que exibe uma mensagem na tela

def exibe_mensagem():
    print("Minha primeira funcao")

#chamada da funcao
exibe_mensagem()

exibe_mensagem()

# Funcao que exiba uma mensagem customizada

def exibe_mensagem_custom (mensagem):
    print(mensagem)

# Chamada da funcao com parametro
msg = "Minha mensagem"
exibe_mensagem_custom (msg)

msg2 = "Outra mensagem"
exibe_mensagem_custom (msg2)

# Funcao para somar 2 numeros inteiros

def calcula_soma (num1,num2):
    soma = num1 + num2
    return(soma)

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

# Uma forma de chamada da funcao com "return"
s = calcula_soma (num1,num2)
print(f"Soma: {s}")

# Outra forma de chamada da funcao com "return"

print(f"Soma: {calcula_soma (num1,num2)}")

# Funcao que calcula a soma e a media dos numeros de inicio ate fim

def calcula_soma_media (ini,fim):
    soma = 0
    cont_numeros = 0
    for i in range (ini, fim+1):
        soma+=i
        cont_numeros+=1
    media = soma / cont_numeros
    return (soma,media)

# Chamada da funcao
inicio = int (input("Digite o inicio: "))
fim = int(input("Digite o fim: "))

s,m = calcula_soma_media (inicio,fim)

print(f"Soma: {s}")
print(f"Media: {m:.2f}")




