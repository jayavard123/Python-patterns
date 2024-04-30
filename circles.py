import turtle
import colorsys
t=turtle.Turtle()
turtle.Screen().bgcolor('black')
t.width(9)

def shit():
    h=0
    n=98
    for i in range(1234):
        c=colorsys.hsv_to_rgb(h,1,0.8)
        h+=1/n
        t.speed(56)
        t.pencolor(c)
        t.pensize(5)
        t.rt(329)
        t.lt(57)
        t.forward(28)
        t.circle(150)
        t.lt(181)
        t.backward(162)

shit()
turtle.done()

