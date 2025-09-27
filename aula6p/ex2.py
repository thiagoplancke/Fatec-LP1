# Faça um programa que mostre a data no formato por extenso. O programa deve receber
# três números, representando dia, mês e ano, respectivamente.
# Entrada de três números Saída experada
# 01
# 04
# 2015
# 01 de abril de 2015
# 05
# 06
# 2025
# 05 de junho de 2025

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

meses = ["Janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

print(f"{dia} de {meses[mes - 1]} de {ano}")