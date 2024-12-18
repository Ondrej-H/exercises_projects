import turtle

def draw_n_spiral(n, side=4, count_turns=57, direction="left"):
    """
    Function draw spiral of n-gon shape.
    'n' is number of sides of the n-gon.
    'side' is lenght of the first stroke from the center of the spiral
    'count_turns' is how many strokes will there be in total
    """
    angle = (180 - (180 * (1 - 2/n)))
    t = turtle.Turtle()
    t.speed(10)
    t.pensize(2)
    t.left(90)
    for i in range(count_turns+1):
        t.forward(side)
        t.left(angle)       # for left-handed spiral
        #t.right(angle)     # for right-handed spiral
        side += 2
    turtle.done()


draw_n_spiral(8)