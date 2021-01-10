import math


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    print("\033[1;36m QUADRADO comppleto")

def polygon(t, length, lados):
    angulo = 360/lados
    for i in range(lados):
        t.fd(length)
        t.rt(angulo)
        t.fd(length)
    print("\033[1;31m POLIGONO COMPLETO")

def retangulo(t, side_menor, side_maior):
    for i in range(2):
        t.pd()
        t.fd(side_menor)
        t.rt(90)
        t.fd(side_maior)
        t.rt(90)
    print("\033[1;35m RETANGULO COMPLETO")

def circle (t, raio):
    circunference = 2 *math.pi * raio
    lados = int(circunference /3) +1
    length = circunference / lados
    polygon(t, length,lados)
