# 14. Separando positivos e negativos
# • Leia 10 números.
# • Coloque os positivos em uma lista e os negativos em outra.
# • Exiba as duas listas.

positivos = []
negativos = []

for i in range(10):
    x = int(input(f"Digite o {i+1} numero: "))
    if x > 0:
        positivos.append(x)
    else:
        negativos.append(x)

print(negativos)
print(positivos)