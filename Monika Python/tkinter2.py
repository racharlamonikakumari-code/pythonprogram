import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First GUI App")
root.geometry("300x200")  # Width x Height

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
l2 = tk.Label(root, text="Hello, Monika!")
l2.pack()


# Start the GUI event loop
root.mainloop()