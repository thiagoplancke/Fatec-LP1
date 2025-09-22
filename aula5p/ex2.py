# 2. Número secreto
# • O programa sorteia um número entre 1 e 50.
# • O usuário deve tentar adivinhar.
# • O programa deve dar dicas (“maior” ou “menor”) até acertar.
import random

numero_secreto = random.randint(1,50)
print(numero_secreto)

while True:
    usuario = int(input("Digite um numero de 1 a 50: "))
    if usuario < numero_secreto:
        print("Digite um numero maior")
    elif usuario > numero_secreto:
        print("Digite um numero menor")
    else:
        print("Parabéns você acertou!")
        break