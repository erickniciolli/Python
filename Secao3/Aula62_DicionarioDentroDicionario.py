clientes={ # DICIONARIO CLIENTES
    "cliente1":{"nome: ":"Erick", "sobrenome: ":"Santos"}, # dicionario cliente1
    "cliente2":{"nome: ":"Valdir", "sobrenome: ": "Niciolli"}  #dicionario cliente2
}

for clientesK, clientesV in clientes.items():
    print(clientesK)
    for nome, sobrenome in clientesV.items():
        print(f"\t{nome} {sobrenome}")

# para juntar dois dicionarios d1 e d2, usar d1.update(d2)