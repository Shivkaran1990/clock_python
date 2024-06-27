import tkinter as tk
from tkinter import Label
import time

# Function to update the time
def time_update():
    current_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, time_update)  # Update the time every second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create and configure the clock label
clock_label = Label(root, font=("Helvetica", 48), background="black", foreground="white")
clock_label.pack(anchor='center')

# Start the clock
time_update()

# Run the Tkinter event loop
root.mainloop()