import turtle as t

t.speed(0)
t.setup(800,600)
t.speed(9)
t.up()

def my_goto(x, y):
    t.pencolor("orange")
    t.penup()
    t.goto(x, y)
    t.pendown()

def round_rectangle(centre_x,centre_y,width,height,cornersize):
    t.up()
    t.goto(centre_x-width/2+cornersize,centre_y-height/2)
    t.down()
    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        t.fd(width-2*cornersize)
        t.circle(cornersize,90)
        t.fd(height-2*cornersize)
        t.circle(cornersize,90)
        t.end_fill()

def round_rectangle(centre_x,centre_y,width,height,cornersize):
    t.up()
    t.goto(centre_x-width/2+cornersize,centre_y-height/2)
    t.down()
    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        t.fd(width-2*cornersize)
        t.circle(cornersize,90)
        t.fd(height-2*cornersize)
        t.circle(cornersize,90)
        t.end_fill()
round_rectangle(0,0,200,300,80)
t.fillcolor('black')
t.begin_fill()

t.goto(-35, 40)
t.fillcolor('white')
t.begin_fill()
t.forward(80)
t.left(90)
t.forward(10)
t.left(90)
t.forward(80)
t.left(90)
t.forward(10)
t.left(90)

t.goto(-35, 60)
t.forward(80)
t.left(90)
t.forward(10)
t.left(90)
t.forward(80)
t.left(90)
t.forward(10)
t.left(90)
t.pendown()
t.end_fill()
t.fillcolor('red')
t.begin_fill()
t.goto(5,50)
t.penup()
t.circle(15)
t.pendown()
t.end_fill()

t.goto(-150, -175)
t.begin_fill()
t.pencolor("black")
t.fillcolor("black")
round_rectangle(90,-125,600,100,50)
t.begin_fill()
t.goto(-70,-175)
t.setheading(110)
t.circle(80,-100)
t.goto(140,-280)
t.setheading(350)
t.circle(80,-100)
t.end_fill()
t.done()










