#calculator.py
#Jatin Bhagat
#oct/23/2024

#import tkinter as tk

# root = tk.Tk()
# root.title("Basic Calculator")
# root.mainloop()




# root = tk.Tk()
# root.title("Basic Calculator")


# screen_var = tk.StringVar()

# screen_var.set("")

# screen = tk.Entry(root, textvariable = screen_var, font = "Arial 20 bold", 
#                   borderwidth = 4, relief = "ridge")

# screen.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)
# root.mainloop()






# root = tk.Tk()
# root.title("Basic Calculator")


# screen_var = tk.StringVar()

# screen_var.set("")

# screen = tk.Entry(root, textvariable = screen_var, font = "Arial 20 bold", 
#                   borderwidth = 4, relief = "ridge")

# screen.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# buttons = [ 
#     "7", "8", "9", "/", 
#     "4", "5", "6", "*", 
#     "1", "2", "3", "-", 
#     "C", "0", "=", "+" 
# ]

# row_val = 1
# col_val = 0 

# for button_text in buttons:
#     button = tk.Button(root, text=button_text, font="Arial 18", padx=20, 
#                        pady=20) 
#     button.grid(row=row_val, column=col_val, padx=5, pady=5)
#     col_val += 1 
#     if col_val > 3: 
#         col_val = 0 
#         row_val += 1



# root.mainloop()



# def click(event): 
#     text = event.widget.cget("text") 
#     if text == "=": 
#         try: 
#             expression = screen_var.get() 
#             result = eval(expression) 
#             screen_var.set(result) 
#         except Exception as e: 
#             screen_var.set("Error") 
#     elif text == "C": 
#         screen_var.set("") 
#     else: 
#         current = screen_var.get() 
#         screen_var.set(current + text)

# root = tk.Tk()
# root.title("Basic Calculator")


# screen_var = tk.StringVar()

# screen_var.set("")

# screen = tk.Entry(root, textvariable = screen_var, font = "Arial 20 bold", 
#                   borderwidth = 4, relief = "ridge")

# screen.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# buttons = [ 
#     "7", "8", "9", "/", 
#     "4", "5", "6", "*", 
#     "1", "2", "3", "-", 
#     "C", "0", "=", "+" 
# ]

# row_val = 1
# col_val = 0 

# for button_text in buttons:
#     button = tk.Button(root, text=button_text, font="Arial 18", padx=20, 
#                        pady=20) 
#     button.grid(row=row_val, column=col_val, padx=5, pady=5)
#     col_val += 1 
#     if col_val > 3: 
#         col_val = 0 
#         row_val += 1


# button.bind("<Button-1>", click)

# root.mainloop()

import tkinter as tk 
 
def click(event): 
    text = event.widget.cget("text") 
    if text == "=": 
        try: 
            expression = screen_var.get() 
            result = eval(expression) 
            screen_var.set(result) 
        except Exception as e: 
            screen_var.set("Error") 
    elif text == "C": 
        screen_var.set("") 
    else: 
        current = screen_var.get() 
        screen_var.set(current + text) 
 
root = tk.Tk() 
root.title("Basic Calculator") 
 
screen_var = tk.StringVar() 
screen_var.set("") 
 
screen = tk.Entry(root, textvar=screen_var, font="Arial 20 bold", 
borderwidth=4, relief="ridge", justify="right") 
screen.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10) 
 

buttons = [ 
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "=", "+" 
] 
 
row_val = 1 
col_val = 0 
 
for button_text in buttons: 
    button = tk.Button(root, text=button_text, font="Arial 18", padx=20, 
pady=20) 
    button.grid(row=row_val, column=col_val, padx=5, pady=5) 
    button.bind("<Button-1>", click) 
    col_val += 1 
    if col_val > 3: 
        col_val = 0 
        row_val += 1 
 
root.mainloop() 