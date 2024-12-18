from turtle import forward, right, left, exitonclick, speed, penup, pendown
from ngon import draw_n_gon

def draw_ngons_in_range(a,b,c=1):
    """
    Function draw a number of n-gons, which is equal to 'b' minus 'a' (considering c=1).\n
    'a' is a number of sides of the first n-gon.\n
    'b' equals to number of sides of the last n-gon.\n
    'c' is a step between types of n-gons, default c=1.\n
    Unhashtaging the 'speed(0)' lower will speed up the drawing.\n
    Modul's 'ngon' function draw_n_gon() needs to be imported.
    """
    for i in range(a,b+1,c):
        #speed(0)
        draw_n_gon(i)
        penup()
        forward(73)
        pendown()
        i += 1
    exitonclick()


draw_ngons_in_range(5, 8)
