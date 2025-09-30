# 23. Dado um conjunto de nomes, verifique se um nome digitado está presente.

nomes = {"thiago","pedro","orlando","jessica","joelma"}

ver = input("Digite um nome: ")

if ver in nomes:
    print(f"{ver} esta na lista")
else:
    print("Não esta na lista")