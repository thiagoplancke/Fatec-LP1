# 4. Leia uma lista de 10 números e crie duas listas: uma com os números pares e outra com os
# ímpares

numero = [1,2,3,4,5,6,7,8,9,10]
par = []
impar = []

for i in numero:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"Par: {par}")
print(f"impar: {impar}")