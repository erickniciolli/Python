
a = lambda x, y: x*y

print(a(2, 2))


lista=[
    ["celta", 15],
    ["palio", 12],
    ["gol", 18]
]

print(lista)


lista.sort(key=lambda item: item[1], reverse=True)  #  reverse para inverter a ordem de ordem

print(lista)

print(sorted(lista, key=lambda item:item[1])) #  fazendo direto no print, não altera a lista original  