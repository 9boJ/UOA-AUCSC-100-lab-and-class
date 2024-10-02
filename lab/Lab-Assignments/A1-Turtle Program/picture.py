#picture.py
#by Jatin Bhagat, Sep/30/24

# Import all the objects of the turtle module
import turtle as t

# sets the background colour to orange
t.bgcolor("orange")

# sets the speed to fasts mode 
t.speed(0)

# A functions when called makes a square
def square(length):
    for i in range(4):
        t.pendown()
        t.forward(length)
        t.left(90)
        t.penup()

# repeated code for top sind
def move_left():
    t.forward(50)
    t.left(90)

# repeated code for left sind
def leftside():
    move_left()
    t.left(45)
    t.forward(50)
    t.penup()
    t.right(180)
    t.forward(50)
    t.pendown()
    t.left(45)
    t.forward(50)
    t.left(135)
    t.forward(50)
    t.penup()
    t.right(180)
    t.forward(50)
    t.pendown()
    t.left(45)
    t.forward(50)
    t.left(135)
    t.forward(50)
    t.left(45)
    t.forward(150)

# repeated code for right sind
def rightside():
    move_left()
    t.right(45)
    t.forward(50)
    t.penup()
    t.backward(50)
    t.right(45)
    t.pendown()

# repeated code for right sind in the function wheich if 
def leftside2():
    rightside()
    rightside()
    rightside()
    t.left(45)
    t.forward(50)
    t.left(135)
    t.forward(150)
    t.left(45)

# a fuction for building the sides 
def box(side):
    t.setheading(0)
    t.pendown()
    if side == "top":
        t.color("black","yellow")
        t.begin_fill()
        t.setheading(0)
        t.left(45)
        move_left()
        move_left()
        t.forward(50)
        t.right(180)
        move_left()
        move_left()
        t.forward(50)
        t.right(180)
        move_left()
        move_left()
        move_left()
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.left(90)
        move_left()
        t.forward(50)
        t.right(180)
        move_left()
        move_left()
        move_left()
        t.left(90)
        move_left()
        move_left()
        t.forward(50)
        t.left(90)
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.left(90)
        move_left()
        t.forward(50)
        t.right(180)
        move_left()
        move_left()
        move_left()
        t.left(90)
        move_left()
        move_left()
        t.forward(50)
        t.left(90)
        t.forward(150)
        t.end_fill()
        t.right(90)
        t.forward(100)
        t.setheading(0)
    elif side == left:
        t.color("black","blue")
        t.begin_fill()
        t.right(90)
        t.forward(50)
        t.left(45)
        leftside()
        t.penup()
        t.left(135)
        t.forward(100)
        t.left(45)
        t.pendown()
        leftside()
        t.left(135)
        t.forward(100)
        t.left(45)
        leftside()
        t.left(135)
        t.forward(50)
        t.end_fill()
        t.penup()
        t.right(180)
        t.forward(150)
        t.right(135)
        t.forward(150)
        t.setheading(0)
        t.color("black")
    elif side == "right":
        t.color("black","red")
        t.begin_fill()
        t.left(45)
        leftside2()
        t.forward(100)
        t.left(135)
        leftside2()
        t.forward(100)
        t.left(135)
        leftside2()
        t.forward(50)
        t.end_fill()

# variables for the sides 
left = "left"        
top = "top"
right = "right"

# the box for white background
t.color("black","white")
t.penup()
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(50)
t.begin_fill()
square(500)
t.end_fill()
t.penup()
t.left(90)
t.forward(250)
t.right(90)
t.forward(250)
t.setheading(0)
#########################################

#Rubik's cube
t.pensize(5)
t.right(90)
t.pendown()
t.forward(150)

t.left(180)
t.penup()
t.forward(150)

t.pendown()
t.left(45)
t.forward(150)

t.penup()
t.right(180)
t.forward(150)

t.pendown()
t.left(90)
t.forward(150)

t.left(90)
t.forward(150)

t.left(90)
t.forward(150)

t.setheading(0)
t.penup()
t.right(45)
t.forward(150)
t.left(90)

box(top)

t.right(90)
t.forward(150)

t.setheading(0)
t.left(45)
t.forward(150)

t.left(45)
t.forward(150)
t.penup()


t.left(135)
t.forward(150)

t.left(45)
t.forward(150)

t.right(135)
t.pendown()

t.forward(150)

t.right(45)
t.forward(150)

t.penup()

box(left)

t.right(90)
t.forward(50)
t.left(135)

t.pendown()

box(right)

# This pause the code until the user closes the Python Turtle Graphics window
t.done()