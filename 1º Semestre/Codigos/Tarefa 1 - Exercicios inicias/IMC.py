# Calculo de indice de massa corporea

Peso = int(input("Digite seu peso:"))
Altura = float(input("Digite sua altura (em metro):"))

IMC = Peso/(Altura*Altura)

print(f"Seu indice de massa corporea eh: {IMC:.2f}")
