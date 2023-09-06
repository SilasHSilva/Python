data = input("Digite uma data no formato dd/mm/aaaa: ")
lista_data = data.split("/")

if (lista_data[1] == "01'"):
    mes_extenso = "Janeiro"

elif (lista_data[1] == "02'"):
    mes_extenso = "Fevereiro"

elif (lista_data[1] == "03'"):
    mes_extenso = "Março"

elif (lista_data[1] == "04'"):
    mes_extenso = "Abril"

elif (lista_data[1] == "05'"):
    mes_extenso = "Maio"

elif (lista_data[1] == "06'"):
    mes_extenso = "Junho"

elif (lista_data[1] == "07'"):
    mes_extenso = "Julho"

elif (lista_data[1] == "08'"):
    mes_extenso = "Agosto"

elif (lista_data[1] == "09'"):
    mes_extenso = "Setembro"

elif (lista_data[1] == "10'"):
    mes_extenso = "Outubro"

elif (lista_data[1] == "11'"):
    mes_extenso = "Novembro" 

elif (lista_data[1] == "12'"):
    mes_extenso = "Dezembro"

data_extenso = lista_data[0] + "de" (mes_extenso) + lista_data[2]

print(data_extenso)


