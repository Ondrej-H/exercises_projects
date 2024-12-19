import turtle


def draw_spiral(n=100, side=0.01, count_turns=1000, side_rise=0.01, direction="left"):
    """
    Function draw spiral of n-gon shape.\n
    'n' is number of sides of the n-gon.\n
    'side' is length of the first stroke from the center of the spiral.\n
    'count_turns' is how many strokes will there be in total.\n
    'side_rise' - the higher, the bigger the gaps between strokes.\n
    'direction' of rotation of the spiral must be string "left" or "right"
    """
    angle = (180 - (180 * (1 - 2/n)))
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.tracer(0)
    # t.pensize(2)
    t.left(90)
    for i in range(count_turns+1):
        t.forward(side)
        if direction == "left":
            t.left(angle)       # for left-handed spiral
        else:
            t.right(angle)     # for right-handed spiral
        side += side_rise
    screen.update()
    turtle.done()


draw_spiral()
