from tkinter import *
import tkinter as tk

root=tk.Tk()

def raise_frame(frame):
    frame.tkraise()

frame1=Frame(root)
frame2=Frame(root)

for f in (frame1,frame2):
    f.grid(row=0,column=0,sticky='news')



tk.Label(frame1, text="Name : ").grid(row=0)
n=tk.Entry(frame1)
n.grid(row=0, column=10)


tk.Label(frame1, text="Extra : ").grid(row=2)
e=tk.Entry(frame1)
e.grid(row=2, column=10)

def click():
    name=n.get()
    etc=e.get()
    raise_frame(frame2)
    lbl1=Label(frame2 , text=name)
    lbl1.grid(row=1 , column=0)

    lbl2=Label(frame2 , text=etc)
    lbl2.grid(row=2 , column=0)

raise_frame(frame1)

btn=tk.Button(frame1, text="Click" , command=click)
btn.grid(row=3, column=5)

root.mainloop()
