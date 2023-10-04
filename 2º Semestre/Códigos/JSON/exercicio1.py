import json

with open("log.json","r",encoding="utf8") as arq:
    dados_leitura = arq.read()
    conteudo_json = json.loads(dados_leitura)

for i in range(len(conteudo_json)):
    try:
        print(f"Operation Name: {conteudo_json[i]['operationName']}")
    except:
        print(None)
    try:
        print(f"Table Name: {conteudo_json[i]['tableName']}")
    except:
        print(None)
    try:
        print(f"Fields: {conteudo_json[i]['fields']}")
    except:
        print(None)