# 9. Tabuada personalizada
# • Peça um número ao usuário.
# • Mostre a tabuada desse número de 1 a 10.

numero = int(input("Digite um numero: "))

for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")

