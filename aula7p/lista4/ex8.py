# 8. Verificação de palíndromo
# • Leia uma palavra.
# • Informe se ela é um palíndromo (igual quando lida de trás para frente).


palavra = input("Digite uma palavra: ")
lista = []
for i in palavra:
    lista.append(i)

invert = ""

for x in range(len(lista)-1, -1, -1):
    c = lista[x]
    invert = invert + c
print(invert)

if invert == palavra:
    print("é um palindromo")
else:
    print("Não é um palindromo")