lista1=[1, 2, 3]
lista2=[4, 5, 6]

lista2.append(7)  #adiciona algo no fim
lista2.insert(0, "inicio")  #aqui no insert, prineiro colocar o índice onde queremos adicionar, depois o que queremos adicionar

print(lista1)
print(lista2)
print(lista1+lista2)
# lista1.extend(lista2) ou seja, extende com a lista2, também podemos adicionar uma string ou qualquer valor

#comando .pop deleta o último elemento

#já o comando del, precisamos indicar qual o índice... del(lista1[0])

#max(lista1) OOOU min(lista1)


lista3=["String", True, 10, 20.4]

for tipo in lista3:
    print(f"O tipo do elemento {tipo} é {type(tipo)}")

