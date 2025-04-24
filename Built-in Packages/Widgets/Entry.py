import tkinter as tk

root = tk.Tk()
root.title("Entry Widgets")
root.geometry("300x150")

tk.Label(root, text="Enter your name:").pack()
entry = tk.Entry(root)
entry.pack()

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")
tk.Button(root, text="Go", command=greet).pack()
label = tk.Label(root, text="")
label.pack()

root.mainloop()
