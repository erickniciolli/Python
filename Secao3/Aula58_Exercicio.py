
def func1():
    nome="Erick"
    return nome

def func2(parametro):
    print(f'Oi {parametro}')

nome=func1()

print(func1)
func2(nome)

# exercicio2

def pai(nome, time):
    return f'{nome} torce para o {time}'

def eu(timemeu):
    return f"Eu torço para o {timemeu}"

def juncao(funcao1, funcao2):
    print(f'{funcao1} E O OUTRO {funcao2}')


juncao(pai("Meu pai", "Palmeiras"), eu("São Paulo"))