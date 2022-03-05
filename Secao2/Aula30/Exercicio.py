num1=input("digite um número inteiro: ")

if num1.isnumeric():
    num1=int(num1)
    if (num1%2)==0:
        print("É PAR")
    else:
        print("É IMPAR")
else:
    print("Esse número não é inteiro não!!!")