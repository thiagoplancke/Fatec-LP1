# 22. Leia duas listas de inteiros e mostre os elementos comuns (interseção)

A = [2,5,8,9,7,4,6]
B = [1,3,8,5,6,12,7]

B = set(B)
A = set(A)

print(A.intersection(B))