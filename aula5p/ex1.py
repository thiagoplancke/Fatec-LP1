#1. Média de notas com quantidade variável
# • Solicite ao usuário quantas notas deseja informar.
# • Leia todas as notas e calcule a média.
# • Informe se o aluno foi aprovado (média ≥ 7) ou reprovado.

notas  = int(input("Digite quantas notas deseja colocar: "))
x = 0
soma = 0
while x < notas:
    ntd = float(input(f"Digite a nota {x+1}: "))
    soma += ntd
    x += 1
media = soma/notas
print(f"A media é {media:.2f}")