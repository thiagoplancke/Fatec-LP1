# 1. Leia 10 números inteiros em uma lista e exiba os números que aparecem mais de uma vez.

lista = [1,4,6,8,1,4,9,3,5,2]
repetidos = []
for i in lista:
    if lista.count(i) >= 2:
        repetidos.append(i)
        repetidos = set(repetidos)
        repetidos = list(repetidos)
print(f"Os numero repetidos são {repetidos}")