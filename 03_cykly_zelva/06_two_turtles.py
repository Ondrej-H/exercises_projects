import turtle

def draw_maze(side=10, count_turns=19, angle=90):
    t = turtle.Turtle()     # now just type t.<function> and we can use functions of our new turtle "t"
    t.speed(0)
    t.pensize(2)
    t.left(90)
    for i in range(count_turns):
        t.forward(side)
        t.left(angle)
        side += 5
    
    tz = turtle.Turtle()
    tz.speed(0)
    tz.pencolor("green")
    tz.pensize(4)
    tz.left(90)
    for i in range(count_turns):
        tz.forward(side)
        tz.left(angle)
        side += 5
    # hide cursor of turtle "t"
    #t.hideturtle()
    # window stay opened (like with turtle.exitonclick())
    turtle.done()


draw_maze()