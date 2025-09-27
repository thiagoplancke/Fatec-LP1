# 3. Procurando nome na lista
# • Crie uma lista com 5 nomes fixos.
# • Peça que o usuário digite um nome.
# • Informe se o nome está na lista ou não.

nomes = ["Thiago","Orlando","Matheus","Rafael","Guilherme"]

digite = input("Digite um nome: ")

if digite in nomes:
    print("Está na lista")

else:
    print("Não está na lista")