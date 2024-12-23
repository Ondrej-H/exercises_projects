import turtle


def draw_rotated_squares(a=50, angle=20):
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.tracer(0)
    for j in range(18):
        for i in range(4):
            t.forward(a)
            t.left(90)
        t.left(angle)
    screen.update()
    turtle.done()


draw_rotated_squares()