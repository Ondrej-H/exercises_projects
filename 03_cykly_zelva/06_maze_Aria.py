import turtle

# Vytvoření objektu želvy
t = turtle.Turtle()

# Nastavení rychlosti želvy (0 = nejrychlejší)
t.speed(0)

# Nastavení barvy pera
t.pencolor("blue")

# Nastavení tloušťky pera
t.pensize(2)

# Nastavení počáteční pozice želvy
t.penup()
t.goto(-100, 0)
t.pendown()

# Definice proměnných pro spirálu
strana = 10
úhel = 90
počet_otáček = 10

# Nakreslení spirály
for i in range(počet_otáček * 4):
    t.forward(strana)
    t.left(úhel)
    strana += 5

# Skrytí kurzoru želvy
t.hideturtle()

# Udržování okna otevřeného
turtle.done()