# 12. Frequência de números
# • Leia 8 números e armazene em uma lista.
# • Pergunte um número ao usuário.
# • Mostre quantas vezes ele aparece na lista.

numero = []

for i in range(8):
    x = int(input(f"Digite o {i+1}º numero: "))
    numero.append(x)
print(f"numeros: {numero}")

escolha = int(input("escolha um numero da lista: "))

print(f"O numero {escolha} aparece {numero.count(escolha)} vezes.")