import turtle


def draw_flower(a=50, angle=20):
    # initializing turtle
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.tracer(0)

    # setting starting position
    t.left(90)
    t.forward(200)
    t.right(90)

    # drawing blossom
    for j in range(18):
        for i in range(4):
            t.forward(a)
            t.left(90)
        t.left(angle)

    # drawing stem
    t.right(90)
    t.forward(380)
    t.right(180)

    # positioning for drawing leaf 1
    t.forward(25)
    t.left(90)

    # draw leaf 1
    for j in range(2):
        for i in range(200):
            t.forward(1)
            t.right(0.2)
        t.right(140)

    # positioning for leaf 2
    t.right(90)
    t.forward(25)
    t.right(90)

    # draw leaf 2
    for j in range(2):
        for i in range(200):
            t.forward(1)
            t.left(0.2)
        t.left(140)

    # screen setting
    screen.update()
    turtle.done()


draw_flower()