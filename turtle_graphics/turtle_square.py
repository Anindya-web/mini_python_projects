import turtle

wn = turtle.Screen()
user_bgcolor = input("Please enter your desired bgcolor name: ")
wn.bgcolor(user_bgcolor)

tess = turtle.Turtle()
user_pcolor = input("Please enter your desired pencolor name: ")
tess.color(user_pcolor)
user_psize = int(input("Please enter your desired pensize: "))
tess.pensize(user_psize)


tess.forward(150)
tess.left(90)
tess.forward(150)
tess.left(90)
tess.forward(150)
tess.left(90)
tess.forward(150)

wn.exitonclick()