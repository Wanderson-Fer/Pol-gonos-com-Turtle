import math
from turtle import Turtle, mainloop


def square(t: Turtle):
    """
    Desenha um quadrado

    Args:
        t: objeto Turtle

    """
    for i in range(4):
        t.fd(100)
        t.lt(90)


def polygon(t: Turtle, n: int, length: float):
    """
    Desenha um poligono com n lados de comprimento length

    Args:
        t: objeto Turtle
        n: número de lados
        length: comprimento de cada lado
    """
    angle = 360 / n
    polyline(t, n, length, angle)


def circle(t: Turtle, r: float):
    """
    Desenha um círculo a partir de um raio

    Args:
        t: objeto Turtle
        r: raio
    """
    arc(t, r, 360)


def arc(t: Turtle, r: float, angle: float):
    """
    Desenha um arco a partir de um raio e um ângulo

    Args:
        t: objeto Turtle
        r: raio do arco
        angle: ângulo do arco em graus

    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 8) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def polyline(t: Turtle, n: int, length: float, angle: float):
    """
    Desenha n segmentos

    Args:
        t: objeto Turtle
        n: número de segmentos
        length: comprimento de segmentos
        angle: graus entre os segmentos

    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def petal(t: Turtle, r: float, angle: float):
    """
    Desenha uma pétala com dois arcos

    Args:
        t: objeto Turtle
        r: raio do arco
        angle: ângulo (graus) que descreve o arco
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t: Turtle, n: int, r: float, angle: float):
    """
    Desenha uma flor com n pétalas

    Args:
        t: objeto Turtle
        n: número de pétalas
        r: raio do arco
        angle: ângulo (graus) que descreve o arco
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)


if __name__ == '__main__':
    my_turtle = Turtle()

    # Desenha um quadrado
    # square(my_turtle)
    # polygon(my_turtle, 12, 50)
    # circle(my_turtle, 200)

    # Escreva um conjunto de funções adequadamente geral que possa desenhar flores como as
    # da Figura 4.1.

    # polygon(my_turtle, 200, 5)
    flower(my_turtle, 12, 200, 45)

    mainloop()
