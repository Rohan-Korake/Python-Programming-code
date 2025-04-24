import tkinter as tk

root = tk.Tk()
root.title("Label Widgets")
root.geometry("300x150")

label=tk.Label(root,text="Label added successfully!!")
label.pack()

root.mainloop()
