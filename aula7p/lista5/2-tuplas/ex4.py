# 14. Leia uma frase e armazene em uma tupla todas as vogais que aparecem nela (sem repetição).

frase = "A vida é uma jornada, não um destino".lower()

voagais = ["a","e","i","o","u"]

voagais_frase = tuple(i for i in frase if i in voagais)
voagais_frase = set(voagais_frase)
voagais_frase = tuple(voagais_frase)
print(voagais_frase)