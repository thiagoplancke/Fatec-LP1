# 8. Leia uma lista de números e remova o maior e o menor valor. Exiba a lista resultante.
lista = list(range(1,11))
maximo = max(lista)
minimo = min(lista)

del lista[lista.index(maximo)]

del lista[lista.index(minimo)]

print(lista)