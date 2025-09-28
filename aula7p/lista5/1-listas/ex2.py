# 2. Leia uma lista de nomes e mostre apenas os que começam com vogal.

lista_nome = ["andré","pedro","orlando","thiago","antonio","sergio"]

vogais = ["a","e","i","o","u"]

for i in vogais:
    for j in lista_nome:
        if j.startswith(i):
            print(j)
  