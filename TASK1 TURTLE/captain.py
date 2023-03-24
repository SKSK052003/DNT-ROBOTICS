import turtle
import math

ca = turtle.Turtle()


def func_1(x, y):
    ca.penup()
    ca.goto(x, y)
    ca.pendown()
    ca.setheading(0)
    ca.pensize(2)
    ca.speed(10)


def circle(r, color):
    x_point = 0
    y_pont = -r
    func_1(x_point, y_pont)
    ca.pencolor(color)
    ca.fillcolor(color)
    ca.begin_fill()
    ca.circle(r)
    ca.end_fill()


def star(r, color):
    func_1(0, 0)
    ca.pencolor(color)
    ca.setheading(162)
    ca.forward(r)
    ca.setheading(0)
    ca.fillcolor(color)
    ca.begin_fill()
    for i in range(5):
        ca.forward(math.cos(math.radians(18)) * 2 * r)
        ca.right(144)
    ca.end_fill()
    ca.hideturtle()


if __name__ == '__main__':
    circle(300, 'crimson')
    circle(250, 'snow')
    circle(190, 'crimson')
    circle(120, 'blue')
    star(120, 'snow')
    turtle.done()