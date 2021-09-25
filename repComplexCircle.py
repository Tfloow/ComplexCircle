from turtle import *
import time

point_of_interest=[]
coordinatex = int(textinput("x", "Where do you want me to go on x?"))
point_of_interest.append(coordinatex)
coordinatey = int(textinput("y", "Where do you want me to go on y?"))
point_of_interest.append(coordinatey)
print(point_of_interest)

speed(0.4)
forward(100)
left(90)
forward(100)
right(90)
circle(-100,90)
right(90)
forward(100)
left(90)
forward(100)
left(90)
circle(100)

penup()
goto(point_of_interest[0], point_of_interest[1])
dot(10, "red")
exitonclick()
