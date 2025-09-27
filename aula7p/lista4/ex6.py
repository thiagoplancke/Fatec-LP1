# 6. Nome mais longo
# • Leia uma lista com 5 nomes.
# • Exiba qual tem a maior quantidade de caracteres.

nomes = ["Thiago","Orlando","Matheus","Rafael","Guilherme"]
lista = []

for i in nomes:
    lista.append(len(i))

print(f"O maior nome é o {nomes[lista.index(max(lista))]}")
