import tkinter as tk

window=tk.Tk()

tk.Label(window, text="First Name : ").grid(row=0)
fn=tk.Entry(window)
fn.grid(row=0, column=10)


tk.Label(window, text="Last Name : ").grid(row=2)
ln=tk.Entry(window)
ln.grid(row=2, column=10)

def status():
    popup=tk.Toplevel()

    tk.Label(popup, text="Entry recorded !!").grid(row=0, column=0)
    tk.Button(popup, text="Exit", command=window.destroy).grid(row=2, column=0)

def register():
    fname=fn.get()
    lname=ln.get()
    f=open('data.txt','a')
    f.write(fname)
    f.write(" ")
    f.write(lname)
    f.write("\n")
    f.close()
    status()



tk.Button(window, text="Submit", activebackground="yellow", command=register).grid(row=4,column=10)

window.mainloop()