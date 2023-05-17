senha_valida = 12345
senha_usr = int(input("Digite a senha: "))

while (senha_usr != senha_valida):
    senha_usr = int(input("Senha incoreta! Digite-a novamente: "))

print("Senha correta!")