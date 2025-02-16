import turtle
wn = turtle.Screen()

user_1 = turtle.Turtle()
user_1.pensize(10)
user_1.color("blue")
user_1.right(90)
user_1.forward(150)

user_1.left(90)
user_1.forward(75)

user_2 = turtle.Turtle()
user_2.pensize(10)
user_2.color("orange")
user_2.left(180)
user_2.forward(75)

wn.exitonclick()
