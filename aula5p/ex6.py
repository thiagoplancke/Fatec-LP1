# 6. Tabuadas completas
# • Exiba as tabuadas de multiplicação de 1 até 10.

x = 1
j = 1

while True:
    print(f"{x} x {j} = {x*j}")
    j += 1
    if j > 10:
        j = 1
        x += 1
        if x > 10:
            break