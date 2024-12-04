# imports Turtle as tl
import turtle as tl

# imports Random as rm
import random as rm

def draw_square(turtle, side_length, color):
    """Draw a square with given side lenght and color"""
    turtle.pendown() # Puts the tutle pen down 
    turtle.pencolor(color) # Canges the color
    for i in range(4): # draw the square
        turtle.forward(side_length) 
        turtle.left(90)

def draw_spiral(num_squares, size_increment):
    """draws square going in a spiral"""
    global tur
    tur.speed(0) # sets the turtle speed fast as posibel 
    defaultSize = 20 # default size of the  square
    colorBank = ["red","blue","green","hotpink","magenta"] # color that the turtle can use 
    for i in range(num_squares): #draws square going in a spiral
        defaultSize = size_increment + defaultSize # change the size of the square by increment of "size_increment"
        color = colorBank[rm.randrange(0,4)] # picks a random color 
        draw_square(tur, defaultSize, color) # calls "draw_square()" to draw square
        tur.right(20) #turn the turtle right by 20

tur = tl.Turtle()
draw_spiral(20,10)
tur.screen.mainloop() # keeps the screen open at the end 

