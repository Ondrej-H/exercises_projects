from turtle import forward, left, exitonclick, speed

def draw_n_gon(n):
    """
    Function draw n-gon, where n is number of sides of the n-gon.
    Unhashtaging the 'speed(0)' lower will speed up the drawing.
    """
    #speed(0)
    a = 200/n
    for side in range(n):
        forward(a)
        left(180 - (180 * (1 - 2/n)))
    exitonclick()


draw_n_gon(10000)
