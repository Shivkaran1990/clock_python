import tkinter as tk
from tkinter import Label
import time



# Create the main window
root = tk.Tk()
root.title("Digital Clock Digital Clock in EST")
root.configure(bg="red")
root.geometry("400x400");

# Create and configure the clock label
clock_label = Label(root, text ="Welcome",font=("Helvetica", 48), background="red", foreground="black")
clock_label.pack(anchor='center')
clock_label.pack(pady=100);



# Run the Tkinter event loop
root.mainloop()