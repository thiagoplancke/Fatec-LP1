# 8. Triângulo numérico
# • Solicite um número n.
# • Exiba linhas em formato triangular:

numero = int(input("Digite um numero: "))
lista = []
for i in range(1, numero + 1):
    lista.append(i)
    
    for j in lista:
        print(j, end= "")
    print()   

