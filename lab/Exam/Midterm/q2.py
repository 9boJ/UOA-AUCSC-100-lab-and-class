import tkinter as tk # import's tkinter as tk

lst = ['Zoe', 'Yannick', 'Xena', 'Wendy', 'Vince'] # list of names

def cilk():
    """changes the name ever time cilked """
    global lst, textnub, entry # look for the variables in mine 
    textnub = textnub + 1 # ever time cilked is called "textnub" go up by 1 
    if textnub >= len(lst): # if "textnub" goes over or is length  of list "lst" sets "textnub" to 0 
        textnub = 0
    entry.config(text = lst[textnub]) # updates the name from the list 
    entry.pack() # save the changes 

window = tk.Tk() # opens a window
textnub = 0 # sets "textnub" to 0 
entry = tk.Label(window, text= lst[textnub], background= "white", width=20, anchor="w", padx= 1, pady= 1,) # makes a widget "Label" and sets the text from list of name "lst"
entry.pack(side='left') # saves the wiget and move it to the left

next = tk.Button(window, text= "Next", command=cilk, padx= 1, pady= 1 )# makes a widget "Button" and sets the text "Next" so when cliked show the next name by calling "clik()"
next.pack(side = "right") # save the wight and move it to the right

window.mainloop() # kepp the screen open 