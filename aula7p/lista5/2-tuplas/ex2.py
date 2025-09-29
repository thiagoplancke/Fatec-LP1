# 12. Leia 5 números inteiros e armazene-os em uma tupla. Informe quantos são pares.

lista = []
for i in range(5):
    numeros = int(input("Digite o 1. numero: "))
    lista.append(numeros)


lista = tuple(lista)

par  = []

impar = []

for j in lista:
    if j % 2 == 0:
        par.append(j)
    else:
        impar.append(j)