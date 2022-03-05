num1=input("Digite um número: ")
num2=input("Digite outro número: ")

if num1.isdigit() and num2.isdigit():
    num1=int(num1)
    num2=int(num2)

    print(num1+num2)
else:
    print("Não são números")


# para float, converter pra float.. porém não funciona no isdigit, isnumeric nem isdecimal

num3=input("Digite um número: ")
num4=input("Digite outro número: ")

#essa opção TRY é para não aparecer um erro. tenta, se não rolar, vai pro except
try:
    num3=float(num3)
    num4=float(num4)

    print(num4+num3)
except:
    print("ERRO")