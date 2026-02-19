import tkinter as tk

def add_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    result_label.config(text="Sum = " + str(result))

root = tk.Tk()
root.title("Addition Program")
root.geometry("300x200")


tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()


tk.Button(root, text="Add", command=add_numbers).pack()

result_label = tk.Label(root, text="Sum = ")
result_label.pack()

root.mainloop()