# 16. Leia duas tuplas de números e crie uma nova tupla que contenha a soma dos elementos posição
# a posição.

tupla1 = (1,2,3,4,5,6,7,8,9)
tupla2 = (4,8,2,1,3,6,3,9,6)
tupla3 = []
x = 0
for i in tupla1:
    tupla3.append(tupla1[x]+tupla2[x])
    x += 1
tupla3 = tuple(tupla3)
print(tupla3)