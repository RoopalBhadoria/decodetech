from tkinter import *

root=Tk()

def raise_frame(frame):
    frame.tkraise()

frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)

for used_frames in (frame1,frame2,frame3,frame4):
    used_frames.grid(row=0,column=0)

btn1=Button(frame1 , text="FRAME 1", command=lambda:raise_frame(frame2))
btn1.grid(row=0 , column=0)
lbl1=Label(frame1 , text="FRAME 1")
lbl1.grid(row=1 , column=0)

btn2=Button(frame2 , text="FRAME 2" , command=lambda:raise_frame(frame3))
btn2.grid(row=0 , column=0)
lbl2=Label(frame2 , text="FRAME 2")
lbl1.grid(row=1 , column=0)

btn3=Button(frame3 , text="FRAME 3" , command=lambda:raise_frame(frame4))
btn3.grid(row=0 , column=0)
lbl3=Label(frame3 , text="FRAME 3")
lbl3.grid(row=1 , column=0)

btn4=Button(frame4 , text="FRAME 4" , command=lambda:raise_frame(frame1))
btn4.grid(row=0 , column=0)
lbl4=Label(frame4 , text="FRAME 4")
lbl4.grid(row=1 , column=0)

raise_frame(frame1)
root.mainloop()
