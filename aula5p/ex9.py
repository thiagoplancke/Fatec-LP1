# 9. Triângulo invertido
# • Solicite um número n.
# • Exiba linhas em formato invertido:
# 12345
# 1234
# 123
# 12
# 1

numero = int(input("Digite um numero: "))

for i in range( numero, 0, -1):
    for j in range(1,i + 1):
        print(j, end="")
    print()