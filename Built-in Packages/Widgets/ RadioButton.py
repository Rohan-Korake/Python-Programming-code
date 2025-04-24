import tkinter as tk
from random import choice

root=tk.Tk()
root.title("RadioButton Widgets")
root.geometry("300x150")

choice=tk.IntVar()
rb1=tk.Radiobutton(root,text="Yes",variable=choice,value=1)
rb2=tk.Radiobutton(root,text="No",variable=choice,value=2)
rb1.pack()
rb2.pack()

def Selection():
    print("You selected option",choice.get())

btn=tk.Button(root,text="Submit",command=Selection)
btn.pack()

root.mainloop()