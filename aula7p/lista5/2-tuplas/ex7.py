# 17. Crie uma tupla com 5 palavras e exiba a quantidade de letras de cada uma

palvaras = ["amor","arroz","videogame","pizza","computador"]
x = 0
for i in palvaras:
    print(f" A palavra {palvaras[x]} tem {len(palvaras[x])} letras.")
    x += 1