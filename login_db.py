import pymysql
import tkinter as tk
from tkinter import *
from random import *
import string
from tkinter import messagebox as m_box
from tkinter import filedialog

root=tk.Tk()

db=pymysql.connect(host="localhost", user="Roopal", passwd="pankaj12",database="LOGIN_frame")
cursor=db.cursor()


try:
    db=pymysql.connect(host="localhost", user="Roopal", passwd="pankaj12",database="LOGIN_frame")
    cursor=db.cursor()

    cursor.execute("CREATE DATABASE LOGIN_frame ")
    

except pymysql.err.ProgrammingError:
    print("DATABASE ALREADY EXISTS")

finally:
    print("Connection established !!!")
    #db.select_db()
    try:
        cursor.execute("CREATE TABLE Info(User_id int primary key auto_increment, U_Name varchar(255), Email_Id varchar(200), U_Password varchar(30))") 
        cursor.execute("CREATE TABLE Info2(Info_id int primary key auto_increment,Age numeric(3),DOB date,Img longblob,About text)")       

    except pymysql.err.InternalError:
        print("TABLE EXISTS !!")



def raise_frame(frame):
    frame.tkraise()



frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)
frame5=Frame(root)

for f in (frame1,frame2,frame3,frame4,frame5):
    f.grid(row=0,column=0,sticky='news')

tk.Label(frame1, text="HOME").grid(row=0,column=8)


def date_format():
    from tkcalendar import Calendar
    
    top=tk.Toplevel(root)

    def print_sel():
        var1=cal.selection_get()
        dob.insert(0.0,var1)
        top.destroy()

    cal=Calendar(top,font="Arial 14",selectmode='day',cursor="hand1")
    cal.pack()
    butn=Button(top,text="OK",command=print_sel).pack()



def image():
    upload_image=filedialog.askopenfilename(initialdir=' ',title="Select image file",filetypes=(("png files",'*.png'),("all files","*.*")))
    t1.insert(0.0,upload_image)

def finish():
    age=a.get()
    birth=dob.get(0.0, END)
    pic=t1.get(0.0,END)
    about=t2.get(0.0,END)
    print(age,birth,pic,about)
    
    replaced_image=pic.replace("\n","")
    print(replaced_image)

    with open(replaced_image,'rb') as image1:
        stored = image1.read()
        print(stored)
    query="INSERT INTO Info2(Age,DOB,Img,About) VALUES(%s,%s,%s,%s)"
    finish=(age,birth,stored,about)
    cursor.execute(query,finish)
    db.commit()


def out():
    raise_frame(frame1)

tk.Label(frame4,text="Welcome").grid(row=1,column=3)
tk.Label(frame4,text="Age").grid(row=3,column=1)
a=tk.Entry(frame4)
a.grid(row=3,column=2)
tk.Label(frame4,text="D.O.B").grid(row=4,column=1)
dob=tk.Text(frame4,height=1,width=15)
dob.grid(row=4,column=2)
b=tk.Button(frame4, text="C" , command=date_format)
b.grid(row=4, column=5)
t1=tk.Text(frame4, height=1, width=30)
t1.grid(row=5, column=2)
button=tk.Button(frame4, text="Upload image" , command=image)
button.grid(row=5, column=5)
tk.Label(frame4, text="About").grid(row=6,column=1)
t2=tk.Text(frame4, height=5, width=30)
t2.grid(row=6, column=2)
button1=tk.Button(frame4, text="Finish" , command=finish)
button1.grid(row=8, column=5)
button2=tk.Button(frame4, text="Log out" , command=out)
button2.grid(row=8, column=10)


tk.Label(frame5,text="Verify details !!!").grid(row=2,column=5)

def done():
    email=e.get()
    print(email)
    passw=p.get()
    print(passw)
    db.select_db("LOGIN_frame")
    cursor.execute("SELECT Email_Id,U_Password FROM  Info where Email_Id='"+email+"' AND U_Password='"+ passw +"'")
    # cursor.execute(query)
    var = cursor.fetchone()
    print(var)
    try: 
        if (email and passw) in var:
            raise_frame(frame4)
    except:
        m_box.showerror('error',"Incorrect Details !!!")

def b():
    raise_frame(frame1)

def login():
    raise_frame(frame2)
    tk.Label(frame2, text="LOGIN").grid(row=0,column=8)
    lbl1=Label(frame2 , text="Email_Id")
    lbl1.grid(row=1 , column=0)
    e=tk.Entry(frame2)
    e.grid(row=1, column=10)
    global e

    lbl2=Label(frame2 , text="Password")
    lbl2.grid(row=2 , column=0)
    p=tk.Entry(frame2)
    p.grid(row=2, column=10)
    global p

    btn3=tk.Button(frame2, text="Login" , command=done)
    btn3.grid(row=3, column=8)

    b5=tk.Button(frame2, text="Back" , command=b)
    b5.grid(row=4, column=8)


tk.Label(frame3, text="SIGNUP").grid(row=0,column=8)
lbl1=Label(frame3 , text="Name")
lbl1.grid(row=1 , column=0)
n=tk.Entry(frame3)
n.grid(row=1, column=10)

lbl2=Label(frame3 , text="Email_Id")
lbl2.grid(row=2 , column=0)
e1=tk.Entry(frame3)
e1.grid(row=2, column=10)

lbl3=Label(frame3 , text="Password")
lbl3.grid(row=3 , column=0)
p1=tk.Entry(frame3)
p1.grid(row=3, column=10)

def submit():
    
    name=n.get()
    email=e1.get()
    passw=p1.get()
    confirm_pass = cp.get()
    captch = c.get()
    c_captcha = t.get(0.0,END)
    #print(name,email,passw,c_captcha,captch,confirm_pass)
    db.select_db("LOGIN_frame")
    # print(type(captch))
    # print(type(c_captcha))
    # try:
    #     cursor.execute("SELECT Email_Id FROM Info WHERE Email_Id='"+ email +"'")
    #     email_cur = cursor.fetchone()
    #     print(email_cur)
    #     if email in email_cur:
    #         print("Email Exists")

    # try:
    #     for i in c_captcha:
    #         print(c_captcha[i])

    if passw == confirm_pass:
        #for i in c_captcha:
            # print(c_captcha[i])
        #if captch == c_captcha:
        query="INSERT INTO Info(U_Name,Email_Id,U_Password) VALUES(%s,%s,%s)"
        submit=(name,email,passw)
        cursor.execute(query,submit)
        db.commit()
    else:
        m_box.showerror('error',"Incorrect data !!!")
    #         # except:
    #     print("pass wrong")

    #     m_box.showerror('error',"Incorrect Password !!!")


t=tk.Text(frame3, height=2, width=15)
t.grid(row=6, column=10)


def refresh():
    t.delete(0.0,tk.END)
    str_char=string.ascii_letters + string.digits
    empty_list=[]
    for x in range(randint(1,5)):
        empty_list.append(choice(str_char))
        # print(empty_list)
    data="".join(empty_list)
    t.insert(0.0, data)


def signup():
    raise_frame(frame3)
    # tk.Label(frame3, text="SIGNUP").grid(row=0,column=8)
    # lbl1=Label(frame3 , text="Name")
    # lbl1.grid(row=1 , column=0)
    # n=tk.Entry(frame3)
    # n.grid(row=1, column=10)

    # lbl2=Label(frame3 , text="Email_Id")
    # lbl2.grid(row=2 , column=0)
    # e1=tk.Entry(frame3)
    # e1.grid(row=2, column=10)

    # lbl3=Label(frame3 , text="Password")
    # lbl3.grid(row=3 , column=0)
    # p1=tk.Entry(frame3)
    # p1.grid(row=3, column=10)

    lbl4=Label(frame3 , text="Confirm_password")
    lbl4.grid(row=4 , column=0)
    global cp
    cp=tk.Entry(frame3)
    cp.grid(row=4, column=10)
    

    lbl5=Label(frame3 , text="Captcha")
    lbl5.grid(row=5 , column=0)
    global c
    c=tk.Entry(frame3)
    c.grid(row=5, column=10)
    
    # t=tk.Text(frame3, height=2, width=15)
    # t.grid(row=6, column=10)

    btn1=tk.Button(frame3, text="Submit" , command=submit)
    btn1.grid(row=7, column=0)

    btn2=tk.Button(frame3, text="Refresh" , command=refresh)
    btn2.grid(row=7, column=10)

    btn3=tk.Button(frame3, text="Back" , command=lambda:raise_frame(frame1))
    btn3.grid(row=7, column=15)


raise_frame(frame1)

btn1=tk.Button(frame1, text="Login" , command=login)
btn1.grid(row=3, column=5)

btn2=tk.Button(frame1, text="Signup" , command=signup)
btn2.grid(row=3, column=10)

root.mainloop()