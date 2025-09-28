# 10. Dada uma lista de listas (matriz 3x3), calcule a soma dos elementos da diagonal principal

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

soma = 0

for i in range(3):
    soma += matriz[i][i]

print(soma)