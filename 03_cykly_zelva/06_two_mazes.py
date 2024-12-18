import turtle

def draw_mazes(side=10, count_turns=19, angle=90):
    t = turtle.Turtle()     # now just type t.<function> and we can use functions of our new turtle "t"
    t.speed(0)
    t.pensize(2)
    t.left(90)
    original_side = side
    for i in range(count_turns):
        t.forward(side)
        t.left(angle)
        side += 5
    t.penup()
    t.right(180)
    t.forward((count_turns+1) * 5)
    t.right(90)
    t.pendown()
    # zde chci nastvit 'side' opět na default (side=10) respektive na nastavení argumentu při volání funkce. Jak na to?
    side = original_side
    for i in range(count_turns):
        t.forward(side)
        t.left(angle)
        side += 5
    # hide cursor of turtle "t"
    #t.hideturtle()
    # window stay opened (like with turtle.exitonclick())
    turtle.done()


draw_mazes()