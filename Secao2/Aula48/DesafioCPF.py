CPF="84541377853"
nCPF=CPF[:-2]

soma=0
a=10

for v1 in nCPF:
        soma=soma+int(v1)*a
        print(v1, a, soma)
        a -= 1
        if a<2:
            break
if (11-soma%11)>9:
    digito1=0
else:
    digito1=11-soma%11

print(f'O digito 1 é {digito1}')

soma2=0
b=11
for v1 in nCPF:
        soma2=soma2+int(v1)*b
        print(v1, b, soma2)
        b -= 1
        if b<2:
            break
digito2=11-(soma2+digito1*2)%11

print(f"O digito 2 é {digito2}")

nCPF+=str(digito1)
nCPF+=str(digito2)

if CPF==nCPF:
    print("É VALIDO")
else:
    print("INVÁLIDO")