# 11. Lista sem repetição
# • Leia 10 números.
# • Monte uma lista sem repetir valores.
# • Mostre a lista final

# 11. Lista sem repetição

numeros = []  

for i in range(10):
    n = int(input(f"Digite o {i+1}º número: "))
    if n not in numeros:
        numeros.append(n)
  


print("\nLista final sem repetições:")
print(numeros)
