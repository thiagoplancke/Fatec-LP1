# 5. Soma até limite
# • Solicite um número limite positivo.
# • Vá somando números naturais em sequência (1, 2, 3, …).
# • Pare quando a soma ultrapassar o limite e exiba o resultado.

limite = int(input("Digite um numero limite: "))
soma = 0
x = 1
while True:
    soma += (limite - (limite - x))
    x += 1
    if soma > limite:
        print(soma)
        break
        
