import turtle

screen = turtle.Screen()
screen.setup(width=500, height=500)

t = turtle.Turtle()

color = input("enter your color: ")
side_length = int(input("enter height: "))
t.color(color)

for i in range(4):
    t.forward(side_length)
    t.right(90)

turtle.done()