contatos = {}

for i in range (3):
    nome = input("Digite um nome: ")
    tel = input("Digite um telefone: ")
    email = input("Digite um e-mail: ")
    contatos[nome] = {'nome': nome, 'telefone': tel, 'email': email}

for chave, subdic in contatos.items():
    texto = subdic['nome']+" "+subdic['telefone']+" "+subdic['email']+"\n"
    with open ("contatos.txt","a",encoding="UTF8") as arq:
        arq.write(texto)