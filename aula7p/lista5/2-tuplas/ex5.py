# 15. Crie uma tupla com 10 números e mostre o maior, o menor e a média.

lista = []

for i in range(10):
    lista.append(i)

lista = tuple(lista)

print(max(lista))
print(min(lista))

soma = 0

for j in  lista:
    soma += j

media = soma/len(lista)
print(media)