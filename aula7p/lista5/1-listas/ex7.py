# 7. Peça ao usuário uma frase e crie uma lista com todas as palavras distintas (sem repetição).

x = input("Digite uma frase: ")

palavras = x.split()

palavras = list(set(palavras))

print(palavras)
