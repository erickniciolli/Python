loggedUser=True

msg="Usuário logado" if loggedUser else "Precisa logar"
print(msg)
#mensagem será usuário logado se loggedUser é true, senão, precisa logar

idade=input("Qual sua idade")

if not idade.isnumeric():
    print("Digite apenas números")
else:
    idade = int(idade)
    if idade>=18:
        print("Tudo liberado")
    else:
        print("Acesso negado")

#OOOU COM TERNÁRIO

idade=input("Qual sua idade")
if not idade.isnumeric():
    print("Digite apenas números")
else:
    idade=int(idade)
    msg2="Tudo liberado" if idade>=18 else "Negado"
    print(msg2)