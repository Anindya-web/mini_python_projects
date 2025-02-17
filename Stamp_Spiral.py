import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
u1 = turtle.Turtle()
u1.color("blue")
u1.shape("turtle")
distance = 5
u1.up()

for _ in range(40):
    u1.stamp()
    u1.forward(distance)
    u1.right(24)
    distance = distance + 2

wn.exitonclick()
