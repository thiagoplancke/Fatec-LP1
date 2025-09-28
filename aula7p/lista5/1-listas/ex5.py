# 5. Leia uma lista de palavras e exiba todas ordenadas por tamanho.

lista_palavras = ["comida","garrafa","céu","computador","oi","celular"]
tamanho = []
ordem = []

for i in lista_palavras:
    tamanho.append(len(i))
    tamanho.sort()

for j in tamanho:
    for t in lista_palavras:
        if len(t) == j:
            ordem.append(t)
            ordem = set(ordem)
            ordem = list(ordem)
print(ordem)



