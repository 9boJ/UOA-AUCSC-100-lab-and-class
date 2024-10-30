import tkinter as tk 
 
# Initialize main window 
root = tk.Tk() 
root.title("Stopwatch") 
 
# Variables to track time and running state 
time_elapsed = 0 
is_running = False 
 
# Function to update the time 
def update_time(): 
    if is_running: 
        global time_elapsed 
        time_elapsed += 1 
        hours = time_elapsed // 3600 
        minutes = (time_elapsed // 60) % 60 
        seconds = time_elapsed % 60 
        time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}") 
        root.after(1000, update_time) 
 
# Function to start the stopwatch 
def start(): 
    global is_running 
    if not is_running: 
        is_running = True 
        update_time() 
 
# Function to stop the stopwatch 
def stop(): 
    global is_running 
    if is_running: 
        is_running = False 
 
# Function to reset the stopwatch 
def reset(): 
    global time_elapsed, is_running 
    is_running = False 
    time_elapsed = 0 
    time_label.config(text="00:00:00") 
 
# Create label to display time 
time_label = tk.Label(root, text="00:00:00", font=("Arial", 40)) 
time_label.grid(row=0, column=0, columnspan=3, pady=20) 
 
# Create buttons for start, stop, and reset 
start_button = tk.Button(root, text="Start", command=start, width=10) 
start_button.grid(row=1, column=0, padx=5, pady=5) 
 
stop_button = tk.Button(root, text="Stop", command=stop, width=10) 
stop_button.grid(row=1, column=1, padx=5, pady=5) 
 
reset_button = tk.Button(root, text="Reset", command=reset, width=10) 
reset_button.grid(row=1, column=2, padx=5, pady=5) 
 
# Run the application 
root.mainloop()

