from turtle import forward, right, left
from math import sqrt

# house:
def draw_house(a):
    x = a * sqrt(2)
    left(135)
    forward(x)
    right(90)
    forward(x/2)
    right(90)
    forward(x/2)
    right(90)
    forward(x)
    right(135)
    for i in range(4):
        forward(a)
        right(90)


