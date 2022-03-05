x=0

while x<10:
    if x==3:
        x=x+1
        continue #se x é igual a 3, pula o código. tem que por um x=x+1 dentro do if senão o valor vai ficar 3 pra sempre, criando um laço iinfinito
    print(x)
    x=x+1

print("Saiu do laço!")