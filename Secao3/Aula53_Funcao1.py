def saudacao (msg="Olá", nome="Erick"): #  aqui mostra que OLÁ e Erick são as mensagens padrão
    nome=nome.replace("e", "3") #  mudar e para 3
    return f'{msg} {nome}'

print(saudacao())
print(saudacao("Fala", "Péricles"))
print(saudacao("Oi", "Jão"))