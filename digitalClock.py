import tkinter as tk
from tkinter import Label
import time



# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create and configure the clock label
clock_label = Label(root, font=("Helvetica", 48), background="black", foreground="white")
clock_label.pack(anchor='center')


# Run the Tkinter event loop
root.mainloop()