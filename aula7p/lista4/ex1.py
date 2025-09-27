# 1. Contagem de pares e ímpares
# • Leia 10 números inteiros.
# • Armazene-os em uma lista.
# • Ao final, mostre quantos são pares e quantos são ímpares.

lista = []

for i in range(1,11):
    lista.append(i)

par = []
impar = []
for x in lista:
    if x % 2 == 0:
        par.append(x)
        
    else:
        impar.append(x)
        
print(f"Existem {len(impar)} impares na lista")
print(f"Existem {len(par)} pares na lista")