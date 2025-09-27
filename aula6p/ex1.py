# Exercício 1
# A nota final de um estudante é calculada a partir de três notas atribuídas respectivamente a
# um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três
# notas mencionadas anteriormente obedece aos pesos a seguir:

#        Nota               Peso

# Trabalho de Laboratório    2

# Avaliação Semestral        3

# Exame Final                5


notas_tipos = ["Trabalho de Laboratório", "Avaliação Semestral", "Exame Final"]

notas = []

pesos = [2,3,5]

soma = 0
for i in range(3):
    nt = float(input(f"Digite a nota do(a) {notas_tipos[i]}: "))
    notas.append(nt)
    soma += notas[i]*pesos[i]

media = soma/sum(pesos)

print(f"A media final foi de {media:.2f}")