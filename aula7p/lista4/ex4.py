# 4. Média de números positivos
# • Leia números até que o usuário digite um número negativo.
# • Calcule e mostre a média dos números positivos digitados.

numero = []

while True:
    digite = int(input("Digite numeros: "))
    if digite >= 0:
        numero.append(digite)
    else:
         soma = 0
         for i in numero:
             soma += i
         media = soma / len(numero)
         break
print(f"A media é {media:.2f}")

     

