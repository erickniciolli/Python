hora=int(input("Que hora é essa? "))

if hora>0 and hora<12:
    print("Bom dia!")
elif hora>=12 and hora<17:
    print("Batarde")
elif hora<24:
    print("Banoite")
else:
    print("hora inexistente")