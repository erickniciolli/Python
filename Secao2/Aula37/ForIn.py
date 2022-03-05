texto="era uma vez"
novaString=""

for letra in texto:
    if letra=="e" or letra=="u":
        novaString+=letra.upper()
    else:
        novaString+=letra
    print(novaString)


for numeros in range(0, 10, 2):
    print(numeros)


