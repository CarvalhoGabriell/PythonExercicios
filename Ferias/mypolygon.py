import turtle
from Python.Ferias.funcoes_tartaruga import *

comment = """
    O metood fd( param ) move o turtle pra FRENTE de q acordo com o valor dos pixels que vc colocar.
    O metodo lt( param) move o turtle para a ESQUERDA, pórem seus valores correspoem em valores em graus , ou seja, a direção que o cursor ira percorrer
    O metodo rt( param ) move o turtle para a DIREITA, pórem seus valores correspoem em valores em graus , ou seja, a direção que o cursor ira percorrer
    O metodo bk( param ) move o turtle pra TRÁS
    Jás os metodos pu() e pd(), significam respectivamente "caneta pra cima (não desenha a rota)" , "caneta para baixo (desenha a rota)".
"""
print(comment)
bob = turtle.Turtle()

square(bob, 29)
retangulo(bob, 100, 140)
polygon(bob, 50, 8)
circle(bob, 360)
turtle.mainloop()

