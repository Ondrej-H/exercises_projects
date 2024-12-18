from turtle import forward, left, exitonclick
# triangle:
def draw_triangle(a=50):
    """
    Draw an equilateral triangle.
    'a' is base of the trianle.
    """
    for i in range(3):
        forward(a)
        left(120)       # the turtle turns by outer angle (not inner), that's why 120
    exitonclick()


draw_triangle(100)
