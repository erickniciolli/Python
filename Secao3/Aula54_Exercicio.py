#1 está na aula anterior

# 2 função que peça 3 números e a soma entre eles

def soma(n1, n2, n3):
    return n1+n2+n3

print(soma(1,1,1))

def aumento(numero, porcentagem):
    return numero*(1+porcentagem/100)

print(aumento(1, 10))

def fizzbuzz(numero):
    if numero%5==0 and numero%3==0:
        return "FizzBuzz"
    elif numero%2==0:
        return "Fizz"
    elif numero%3==0:
        return "Buzz"
    return numero

print(fizzbuzz(15))
print(fizzbuzz(2))
print(fizzbuzz(3))
print(fizzbuzz(7))