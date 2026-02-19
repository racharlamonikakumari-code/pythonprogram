import tkinter as tk

# function to add numbers
def calculate_si():
    try:
        principal = float(entry1.get())
        rate = float(entry2.get())
        time = float(entry3.get())

        si=(principal*rate*time)/100

        entry4.delete(0, tk.END)
        entry4.insert(0, float(si))

    except ValueError:
        entry4.delete(0, tk.END)
        entry4.insert(0, "Invalid input")

# main window
root = tk.Tk()
root.title("Simple Interest Calculator")

# labels
tk.Label(root, text="Principal").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Rate (%)").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Time (Years)").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Simple Interest").grid(row=3, column=0, padx=10, pady=5)

# entry fields
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)


entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)

# button
tk.Button(root, text="Calculate SI", command=calculate_si).grid(row=4, column=0, columnspan=2, pady=10)

# run window
root.mainloop()