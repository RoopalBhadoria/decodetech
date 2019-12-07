import tkinter as tk

window=tk.Tk()
window.title("First task")

tk.Label(window,text="Name").grid(row=0)
n=tk.Entry(window)
n.grid(row=0 , column=10)
n1=n.get()

tk.Label(window,text="Mobile_no").grid(row=2)
mob=tk.Entry(window)
mob.grid(row=2 , column=10)

tk.Label(window,text="Address").grid(row=4)
add=tk.Entry(window)
add.grid(row=4 , column=10)
add1=add.get()

tk.Label(window,text="Email").grid(row=6)
m=tk.Entry(window)
m.grid(row=6 , column=10)

def mobile_check():
    t=mob.get()
    if len(t)==10:
        return True
    else:
        popup_mobile()

def mail_check():
    t=m.get()
    if t.endswith("@gmail.com"):
        return True
    else:
        popup_mail()

def correct():
    w=tk.Toplevel()
    w.wm_title("Oops !!!")
    l=tk.Label(w,text="Details recorded correctly !")
    l.grid(row=0,column=0)
    b=tk.Button(w,text="Finish",command=w.destroy)
    b.grid(row=1,column=0)

def final_check():
    if mobile_check() and mail_check():
        correct()

def popup_mobile():
    w1=tk.Toplevel()
    w1.wm_title("Oops !!!")
    l=tk.Label(w1,text="Enter valid mobile number !")
    l.grid(row=0,column=0)
    b=tk.Button(w1,text="Finish",command=w1.destroy)
    b.grid(row=1,column=0)

def popup_mail():
    w2=tk.Toplevel()
    w2.wm_title("Oops !!!")
    l=tk.Label(w2,text="Enter a valid gmail !")
    l.grid(row=0,column=0)
    b=tk.Button(w2,text="Finish",command=w2.destroy)
    b.grid(row=1,column=0)

tk.Button(window,text="Submit",command=final_check).grid(row=8,column=5)

window.mainloop()
