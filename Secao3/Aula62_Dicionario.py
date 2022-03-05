d1={"chave1":"Essa é a chave 1", "chave3":"Essa é a chave 3"}
d1["chave2"]="Essa é a chave 2" #  adicionando algo novo no dicionario d1

print(d1)
print(d1["chave1"]) # aqui ve o valor da chave1

d2=dict(chave3="Essa é a chave 3", chave4="Essa é a chave 4")

print(d2)

# para deletar utilizamos del d1["nome da chave"]

print("Essa é a chave 3" in d1.values())

for k in d1:
    print(k)

for v in d1.values():
    print(v)

for i in d1.items():  # aqui mostra a chave e o valor, como uma tupla
    print(i)

for k, v in d1.items():  # aqui retorna ambos também, mas sem ser tupla
    print(k,v)