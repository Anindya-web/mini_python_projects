import turtle

wn = turtle.Screen()
wn.bgcolor("white")

u1 = turtle.Turtle()
u1.color("black")
u1.shape("turtle")
u1.penup()

for _ in range(10):
    u1.forward(50)
    u1.stamp()
    u1.forward(-50)
    u1.right(36)
    
wn.exitonclick()
