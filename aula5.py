#exercicio de fixação


def maximo(a,b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
    return maximo

maximo(7,4)


def multiplo(a,b):
    if a % b == 0:
        print(True) 
    else:
        print(False) 

multiplo(6,5)

def quadrado(a):
    print(a * a)
    return a*a

quadrado(4)


def triangulo(a,b):
    area = (a*b)/2
    print(area)

triangulo(6,9)


