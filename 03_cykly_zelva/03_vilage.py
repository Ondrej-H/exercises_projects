from turtle import forward, right, left, exitonclick, speed
from house import draw_house
# house:
def draw_vilage(a=80, count_houses=19):
    """
    Function draw siple schematic houses.\n
    'a' is a base of the house.\n
    'count_houses' is a number of houses.\n
    Modul's 'house' function draw_house() needs to be imported.
    """
    speed(0)
    left(180)
    forward(12 * a)
    right(180)
    for count in range(count_houses):
        draw_house(a)
        right(90)
        forward(2*a + a/5)


draw_vilage()
exitonclick()