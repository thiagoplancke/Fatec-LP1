# 6. Dada uma lista de números, exiba a soma dos valores que estão em índices pares

lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for i in lista:
    if lista.index(i) % 2 == 0:
        soma += i
print(soma)