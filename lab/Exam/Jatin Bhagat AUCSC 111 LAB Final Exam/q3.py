# Imports all of tkinter 
from tkinter import *

root = Tk() # Sets a tkinter window to "root"

for i in range(0,10):
    """ Makes a multiplication table"""
    root.columnconfigure(i,weight=1) # Setup the 10 columns with a weight of 1 
    root.rowconfigure(i,weight=1) # Setup the 10 rows with a weight of 1 
    for z in range(0,10):
        """ Add the number to the boxs """
        num = Label(text=i*z) # Add the number as a text to it places, 
        num.grid(column=z,row = i) # Sets the text "num" to it columns and row  

root.title("Multiplication Table") # Stes the title of the window to "Multiplication Table"
root.geometry("500x500") # sets the window size to 500pxx500px

root.mainloop() # Keeps the window open at the end 