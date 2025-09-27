# 7. Contador de vogais
# • Peça que o usuário digite uma frase.
# • Conte quantas vogais existem nessa frase.

frase = input("Digite uma frase: ")

vogais = ["a","e","i","o","u"]

vogais_em_frase = []

for i in frase:
    if i in vogais:
        vogais_em_frase.append(i)

print(f"Existe {len(vogais_em_frase)} voagais na frase")

print("Quantidade de cada: ")

print(f"a: {vogais_em_frase.count("a")}")

print(f"e: {vogais_em_frase.count("e")}")

print(f"i: {vogais_em_frase.count("i")}")

print(f"o: {vogais_em_frase.count("o")}")

print(f"u: {vogais_em_frase.count("u")}")