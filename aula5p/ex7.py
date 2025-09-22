# 7. Retângulo de asteriscos
# • Solicite a altura e a largura.
# • Desenhe um retângulo de * usando laços aninhados.
altura = int(input("Digite a altura: "))
largura = int(input("Digite a largura: "))

for i in range(altura):        
    for j in range(largura):
        print("*", end="")  
    print() 
