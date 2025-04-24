import tkinter as tk

root=tk.Tk()
root.title("Checkbutton Widgets")
root.geometry("300x150")

checked=tk.IntVar()
ck=tk.Checkbutton(root,text="I Agree",variable=checked)
ck.pack()

def Status():
    if checked.get()==1:
        print("Checked")
    else:
        print("unchecked")

btn=tk.Button(root,text="Submit",command=Status)
btn.pack()

root.mainloop()