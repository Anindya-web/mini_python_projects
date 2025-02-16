import turtle
wn = turtle.Screen()

u1 = turtle.Turtle()

distance = 50
angle = 90

for _ in range(15):
    u1.forward(distance)
    u1.right(angle)
    distance = distance + 4
    angle = angle - 4

wn.exitonclick()
