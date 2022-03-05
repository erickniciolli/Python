nome="Erick"
altura=1.65
peso=80
idade=28
imc=peso/altura**2

print(nome, "tem", idade, "anos e seu IMC é de", imc)
print(f"{nome} tem {idade} anos e seu imc é de {imc:.2f}")  #duas casas decimais
print("{} tem {} anos e seu imc é de {:.2f}". format(nome, idade, imc))
print("{0} tem {1} anos e seu imc é de {2:.2f}. {0} é gordão ". format(nome, idade, imc))