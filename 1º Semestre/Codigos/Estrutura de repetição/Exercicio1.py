# Jogo do PIM

num =  int(input("Qual o valor da tabuada que voce quer saber?"))
print("tabuada", num)
for i in range(0,11):
    tabuada = num * i
    print(num, "x", i , "=", tabuada)