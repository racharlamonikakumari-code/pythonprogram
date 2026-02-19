import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Welcome App")
root.geometry("300x200")

# Function to show message
def show_welcome():
    messagebox.showinfo("Welcome", "Welcome to Tkinter")

# Create button
btn = tk.Button(root, text="Show Welcome", command=show_welcome)
btn.pack(pady=20)

# Run window
root.mainloop()
