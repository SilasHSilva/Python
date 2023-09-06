# Função SEM recurso Lambda

def soma_numeros (x,y):
    soma = x+y
    return (soma)

print(f"A soma é {soma_numeros(6,9)}")

# Função COM recurso Lambda

soma_numeros_lambda = lambda x,y : x + y 

print(f"A soma é {soma_numeros_lambda (12,5)}")

