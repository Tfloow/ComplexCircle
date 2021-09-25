from turtle import *
import time
import cmath
import math

point_of_interest=[]
cmath.polar(math.sqrt(5) + 2j)
coordinatex = int(textinput("x", "what is your real value"))
coordinatey = int(textinput("y", "what is your complex value"))
complexNumber = coordinatex + coordinatey*1j
print(complexNumber)
polarNumber = cmath.polar(complexNumber)
point_of_interest.append(polarNumber[0])
point_of_interest.append(polarNumber[1])
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
goto(math.ceil(point_of_interest[0])*100, math.ceil(point_of_interest[1])*100)
print(point_of_interest)
print(pos())
dot(10, "red")
pendown()
goto(100,0)
exitonclick()
