# 4. Contagem de pares e ímpares
# • Solicite 10 números.
# • Exiba quantos são pares, quantos são ímpares, e a soma dos pares.
par = []
impar = []
x = 0 
soma = 0
while x < 10:
    numero = int(input("Digite 10 numero: "))
    if numero % 2 == 0:
        soma += numero
        par.append(numero)
    else:
        impar.append(numero)
    x +=1 

print(f"Existem {len(par)} numeros pares e a soma deles da {soma}")
print(f"\nExistem {len(impar)} numeros impares")
