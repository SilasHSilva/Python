# Função SEM recurso Lambda

def retorna_maior (a,b):
    if (a > b):
        return (a)
    else:
        return (b)
    
print (f"O maior valor é {retorna_maior(8,4)}")

# função COM o recurso Lambda

retorna_maior_lambda = lambda a,b : a if (a > b) else b

print (f"O maior valor é {retorna_maior_lambda(3,15)}")
