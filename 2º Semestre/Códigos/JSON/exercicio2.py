import json

with open("produtos_estoque.json", "r", encoding="utf8") as arq:
    dados_leitura = arq.read()
    conteudo_json = json.loads(dados_leitura)

print("Descrições dos produtos com quantidade em estoque superior a 100\n")
for i in range(len(conteudo_json)):
    if (conteudo_json[i]['quantidade'] > 100):
        print(conteudo_json[i]['produto'])

print("\nDescrições dos produtos que custam entre R$5.00 e R$20.00\n")
for i in range(len(conteudo_json)):
    if (conteudo_json[i]['valor'] >= 5.00 and conteudo_json[i]['valor'] <= 20.00):
        print(conteudo_json[i]['produto'])