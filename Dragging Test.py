from turtle import Screen, Turtle

def drag(x, y):
    default.ondrag(None)  # disable handler inside handler

    default.goto(x, y)

    if default.distance(scar) < 40:
        default.shape('turtle')
    elif default.shape() == 'turtle':
        default.shape('circle')

    default.ondrag(drag)

wn = Screen()
wn.setup(500, 500)

scar = Turtle('square', visible=False)
scar.shapesize(4)
scar.color('pink')
scar.penup()
scar.left(90)
scar.forward(50)
scar.showturtle()

default = Turtle('circle', visible=False)
default.shapesize(2)
default.speed('fastest')
default.penup()
default.left(90)
default.backward(50)
default.showturtle()

default.ondrag(drag)

wn.mainloop()