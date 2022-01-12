###############
# CMPT 120 
# turtle_Art.py
# initial plan: Diana Cukierman
# Programmed by: Colton Blackwell
# Date: October 17th, 2021

# - This program uses random to randomize the digital art every time it has ran.
# - Title: RUBRIK UNIVERSE


import turtle
import random

wn = turtle.Screen()
wn.bgcolor("light steel blue")
colton = turtle.Turtle()
colton.speed(0)


def rubikCircle(x, y, z):
    def left():
        colton.fillcolor(x)
        colton.begin_fill()
        colton.right(90)
        colton.forward(50)
        colton.right(120)
        colton.forward(50)
        colton.right(60)
        colton.forward(52.5)
        colton.right(120)
        colton.forward(50)
        colton.end_fill()

    def right():
        colton.fillcolor(y)
        colton.begin_fill()
        colton.left(60)
        colton.forward(50)
        colton.right(120)
        colton.forward(52.5)
        colton.right(60)
        colton.forward(50)
        colton.right(120)
        colton.forward(52.5)
        colton.end_fill()

    def top():
        colton.fillcolor(z)
        colton.begin_fill()
        colton.left(60)
        colton.forward(50)
        colton.right(120)
        colton.forward(50)
        colton.right(60)
        colton.forward(50)
        colton.end_fill()

    left()
    right()
    top()


def square():
    def left():

        colton.fillcolor("firebrick")
        colton.begin_fill()
        colton.right(90)
        colton.forward(100)
        colton.right(120)
        colton.forward(100)
        colton.right(60)
        colton.forward(105)
        colton.right(120)
        colton.forward(100)
        colton.end_fill()

    def right():
        colton.fillcolor("dodger blue")
        colton.begin_fill()
        colton.left(60)
        colton.forward(100)
        colton.right(120)
        colton.forward(105)
        colton.right(60)
        colton.forward(100)
        colton.right(120)
        colton.forward(105)
        colton.end_fill()

    def top():
        colton.fillcolor("gold")
        colton.begin_fill()
        colton.left(60)
        colton.forward(100)
        colton.right(120)
        colton.forward(100)
        colton.right(60)
        colton.forward(100)
        colton.end_fill()

    def cross():
        colton.right(60)
        colton.forward(35)
        colton.right(60)
        colton.forward(100)
        colton.right(60)
        colton.forward(100)
        colton.left(120)
        colton.forward(35)
        colton.left(60)
        colton.forward(100)
        colton.left(60)
        colton.forward(100)
        colton.right(120)
        colton.forward(35)
        colton.right(60)
        colton.forward(33)
        colton.right(120)
        colton.forward(105)
        colton.left(60)
        colton.forward(100)
        colton.left(60)
        colton.forward(33)
        colton.left(120)
        colton.forward(100)
        colton.right(60)
        colton.forward(105)
        colton.right(60)
        colton.forward(35)
        colton.right(60)
        colton.forward(35)
        colton.right(60)
        colton.forward(105)
        colton.right(60)
        colton.forward(101)
        colton.left(120)
        colton.forward(33)
        colton.left(60)
        colton.forward(100)
        colton.left(60)
        colton.forward(105)

    left()
    right()
    top()
    cross()


def name(x, y, z):
    name = turtle.Turtle()
    name.penup()
    name.setpos(250, -300)
    name.pendown()
    name.pencolor(x)
    name.left(90)
    name.forward(20)
    name.right(90)
    name.forward(10)
    name.left(180)
    name.forward(10)
    name.left(90)
    name.forward(20)
    name.left(90)
    name.forward(10)
    name.penup()
    name.forward(5)
    name.pendown()
    name.pencolor(y)
    name.forward(10)
    name.left(90)
    name.forward(15)
    name.left(90)
    name.forward(10)
    name.right(90)
    name.forward(5)
    name.left(180)
    name.forward(20)
    name.right(180)
    name.forward(20)
    name.right(90)
    name.forward(5)
    name.right(90)
    name.forward(5)
    name.penup()
    name.left(90)
    name.forward(10)
    name.pendown()
    name.pencolor(z)
    name.right(90)
    name.forward(25)
    name.left(90)
    name.forward(10)
    name.left(90)
    name.forward(12.5)
    name.left(90)
    name.forward(10)
    name.right(90)
    name.forward(15)
    name.right(90)
    name.forward(10)
    name.right(90)
    name.forward(25)
    name.left(90)
    name.penup()
    name.forward(20)
    # name.stamp("turtle")


colours = ["firebrick", "dodger blue", "gold"]
newColours = []
for i in colours:
    randomColour = random.choice(colours)
    newColours.append(randomColour)
print(newColours[0])
rubikCircle(newColours[0], newColours[1], newColours[2])


def rubikSphere():

    for i in range(11):
        colton.forward(30)
        colton.pendown()
        rubikCircle(newColours[0], newColours[1], newColours[2])
        colton.penup()


rubikSphere()
colton.penup()
colton.setpos(-200, 300)
colton.pendown()
rubikSphere()
colton.penup()
colton.setpos(100, 200)
colton.pendown()
rubikSphere()
randomNum = random.randint(2, 3)
ranAngle = random.randint(0, 150)
ranDirection = random.randint(150, 200)
ranWay = random.randint(1, 2)
direction = 0
for i in range(randomNum):
    colton.pendown()
    square()
    if ranWay == 1:
        colton.right(ranAngle)
    else:
        colton.left(ranAngle)
    colton.penup()
    if direction == 0:
        colton.forward(ranDirection)
    else:
        direction = ranDirection
        colton.forward(direction)

colours = ["red", "blue", "yellow"]
newColour = []
for colour in colours:
    ranColour = random.choice(colours)
    newColour.append(ranColour)
name(newColour[0], newColour[1], newColour[2])