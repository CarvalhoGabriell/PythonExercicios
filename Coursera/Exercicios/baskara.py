from typing import Match


import math


a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

delta = b ** 2 - 4 * a * c

if (delta == 0) :
    raiz1 =( -b + math.sqrt(delta)) / (2*a )
    print("A raiz é unica: ",raiz1)
elif (delta < 0):
    print("O delta não pode ser negativo")
else:
    raiz1 =( - b + math.sqrt(delta)) / (2*a )
    raiz2 = ( - b - math.sqrt(delta)) / (2*a )
    print("As raizes são - Raiz 1:", raiz1, "Raiz 2:",raiz2)