# 9. Dada uma lista de preços, calcule o valor total com 10% de desconto aplicado a cada item.

lista = [35,67,95,128,145]
lista_desconto = []
for i in lista:
    desconto = i * 0.90
    lista_desconto.append(desconto)

print(lista_desconto)