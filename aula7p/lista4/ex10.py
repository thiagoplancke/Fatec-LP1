# 10. Soma até zero
# • O usuário vai digitando números.
# • Quando digitar zero, o programa encerra.
# • Mostre a soma dos números digitados (exceto o zero).

lista_numeros = []
while True:
    numero = int(input("Digite numeros (0 para encerrar): "))
    if numero != 0:
        lista_numeros.append(numero)
    else:
        print(len(lista_numeros))
        break

