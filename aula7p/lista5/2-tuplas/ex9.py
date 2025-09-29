# 19. Crie uma tupla com pares ordenados representando coordenadas (x, y). Exiba apenas os pontos
# onde x = y

tupla = ((2,3),(4,6),(7,7),(0,0),(8,1),(3,3),(1,2),(3,2),(2,2))


for x,y in tupla:
    if x == y:
        print((x,y))