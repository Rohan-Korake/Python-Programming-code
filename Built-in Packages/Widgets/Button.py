import tkinter as tk

root=tk.Tk()
root.title("Button Widgets")
root.geometry("300x150")

def Clicked():
    print("Button Clicked...")

btn=tk.Button(root,text="Click Here",command=Clicked)
btn.pack()

root.mainloop()