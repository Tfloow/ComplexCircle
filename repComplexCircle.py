import turtle
from turtle import *
import time
import cmath
import math

turtle.bgpic()

speed(0)
forward(500)
left(90)
forward(200)
left(90)
forward(500)
left(90)
forward(100)
left(90)
forward(500)
goto(0,100)
home()
goto(100,0)
left(90)
forward(200)
right(90)
forward(100)
right(90)
forward(300)
right(90)
forward(200)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
penup()
home()
pendown()

poiPolar = []
poiComplex = []
coordinatex = float(textinput("x", "what is your real value"))
poiComplex.append(coordinatex)
coordinatey = float(textinput("y", "what is your complex value"))
poiComplex.append(coordinatey)
complexNumber = coordinatex + coordinatey*1j
degree = cmath.phase(complexNumber)
print(degree)
print(complexNumber)
polarNumber = cmath.polar(complexNumber)
poiPolar.append(polarNumber[0])
poiPolar.append(polarNumber[1])
print(poiPolar)

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
goto(math.ceil(poiComplex[0]) * 100+100, math.ceil(poiComplex[1]) * 100)
print(pos())
dot(10, "red")
pendown()
color("red")
goto(100,0)
goto(125, 0)
left(90)
degree = math.degrees(degree)
print(degree)
circle(25, degree)
penup()
write("Angle =", True, align="right")
write(degree, True)
print(cmath.polar(1))

aSqrt = textinput("Get square root? ", "Do you want to know the square root of" + str(complexNumber) + " ?")
if aSqrt == "yes" or "ok":
    print("ok")
    print(poiPolar[0])
    sqrtR = math.sqrt(poiPolar[0])
    sqrtC_1 = poiPolar[1]/2
    sqrtC_2 = poiPolar[1]+2*math.pi/2
    print(sqrtC_2)
    goto(100 + sqrtR*100,0)
    setheading(90)
    circle(sqrtR*100, math.degrees(sqrtC_1))
    dot(10, "blue")
    pendown()
    color("blue")
    goto(100,0)
    penup()
    goto(100 + sqrtR*100,0)
    setheading(90)
    circle(sqrtR*100, math.degrees(sqrtC_2))
    pendown()
    print(math.degrees(sqrtC_2))
    dot(10, "green")
    pendown()
    color("green")
    goto(100, 0)
    penup()

exitonclick()
