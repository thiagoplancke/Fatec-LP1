# 5. Invertendo string
# • Peça ao usuário que digite uma palavra.
# • Mostre a palavra invertida (sem usar funções prontas como [::-1])

palavra = input("Digite uma palavra: ")
lista = []
for i in palavra:
    lista.append(i)

invert = ""

for x in range(len(lista)-1, -1, -1):
    c = lista[x]
    invert = invert + c
print(invert)



    



