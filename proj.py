import tkinter as tk 
from tkinter import ttk
from csv import DictWriter


window=tk.Tk()

tk.Label(window, text="Name : ").grid(row=0)
n=tk.Entry(window)
n.grid(row=0, column=10)


tk.Label(window, text="Mobile_no : ").grid(row=2)
m=tk.Entry(window)
m.grid(row=2, column=10)

tk.Label(window, text="Email : ").grid(row=4)
em=tk.Entry(window)
em.grid(row=4, column=10)

tk.Label(window, text="Age : ").grid(row=6)
age=tk.Spinbox(window, from_=1, to=100)
age.grid(row=6, column=10)

gender=tk.Label(window, text="Gender : ").grid(row=8)
gender=ttk.Combobox(window,values=["Female" , "Male" , "Transgender"])
gender.grid(row=8, column=10)

elig=tk.StringVar()

tk.Radiobutton(window, text="Eligible", value=1,variable=elig).grid(row=10, column=10)
tk.Radiobutton(window, text=" Not-Eligible", value=2, variable=elig).grid(row=10, column=15)

tk.Checkbutton(window, text="Agree terms and condition", onvalue=1).grid(row=12, column=10)

def mobile_check():
    t=m.get()
    if len(t)==10:
        return True
    else:
        popup_mobile()

def mail_check():
    t=em.get()
    if t.endswith("@gmail.com"):
        return True
    else:
        popup_mail()

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

def status():
    popup=tk.Toplevel()

    tk.Label(popup, text="Entry recorded !!").grid(row=0, column=0)
   # tk.Button(popup, text="Exit", command=window.destroy).grid(row=2, column=0)

    

def text():

    if mobile_check() and mail_check():
        f=open("record.txt",'a')
        f.write(n.get())
        f.write( "\t")   
        f.write(m.get())         
        f.write("\t")
        f.write(em.get())
        f.write("\t")
        f.write(age.get())
        f.write("\t")
        f.write(gender.get())
        f.write("\t")
        f.write(elig.get())
        f.write("\n")
        f.close()
        status()

def csv():
    file=open('file.csv', 'a')
    dict_write=DictWriter(file,fieldnames=['Name','Mobile_no','Email','Age','Gender','Elig'])

    if not file:
        dict_write.writeheader()
    
    if mobile_check() and mail_check():
    
    
        dict_write.writerow({'Name':n.get(), 'Mobile_no':m.get(),'Email':em.get(),'Age':age.get(),'Gender':gender.get(),'Elig':elig.get()})
    
from fpdf import FPDF

def pdf():
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=15)
    pdf.cell(200,10,txt=n.get(),align="L",ln=1)
    pdf.cell(200,10,txt=m.get(),align="L",ln=1)
    pdf.cell(200,10,txt=em.get(),align="L",ln=1)
    pdf.cell(200,10,txt=age.get(),align="L",ln=1)
    pdf.output("record.pdf")




tk.Button(window, text="Get txt", command=text).grid(row=14, column=10)
tk.Button(window, text="Get csv",  command=csv).grid(row=14, column=12)
tk.Button(window, text="Get pdf",  command=pdf).grid(row=14, column=16)

t=tk.Text(window, height=6, width=25)
t.grid(row=16, column=10)

def check():

    f=open("record.txt",'r')
    data=f.read()
    t.insert(0.0, data)
    f.close()  
         

def clear():
    t.delete(0.0,tk.END)


tk.Button(window, text="Check", command=check).grid(row=16, column=14)
tk.Button(window, text="Clear", command=clear).grid(row=18, column=14)

window.mainloop()
