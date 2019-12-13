import pymysql
import tkinter as tk
from tkinter import *


window=tk.Tk()

tk.Label(window, text="P_id: ").grid(row=0, column=0)
i=tk.Entry(window)
i.grid(row=0, column=1)
    
tk.Label(window, text="P_name: ").grid(row=1 ,column=0)
n=tk.Entry(window)
n.grid(row=1, column=1)

tk.Label(window, text="P_diagonsis : ").grid(row=2,column=0)
d=tk.Entry(window)
d.grid(row=2, column=1)

tk.Label(window, text="P_address : ").grid(row=3,column=0)
a=tk.Entry(window)
a.grid(row=3, column=1)

def insert():
    id=i.get()
    name=n.get()
    diag=d.get()
    addr=a.get()

    query="INSERT INTO Patient(P_id,P_name,P_diagnosis,P_address) VALUES(%s,%s,%s,%s)"
    insert=(id,name,diag,addr)
    cursor.execute(query,insert)
    db.commit()


tk.Label(window, text="H_id: ").grid(row=0,column=2)
hid=tk.Entry(window)
hid.grid(row=0, column=3)
    
tk.Label(window, text="H_name: ").grid(row=1,column=2)
hn=tk.Entry(window)
hn.grid(row=1, column=3)

tk.Label(window, text="H_city : ").grid(row=2,column=2)
hc=tk.Entry(window)
hc.grid(row=2, column=3)

tk.Label(window, text="H_address : ").grid(row=3,column=2)
ha=tk.Entry(window)
ha.grid(row=3, column=3)

def insert1():
    hos_id=hid.get()
    hos_name=hn.get()
    city=hc.get()
    address=ha.get()

    query="INSERT INTO Hospital(H_id,H_name,H_city,H_address) VALUES(%s,%s,%s,%s)"
    insert1=(hos_id,hos_name,city,address)
    cursor.execute(query,insert1)
    db.commit()


tk.Label(window, text="D_id: ").grid(row=0,column=4)
did=tk.Entry(window)
did.grid(row=0, column=5)
    
tk.Label(window, text="D_name: ").grid(row=1,column=4)
dn=tk.Entry(window)
dn.grid(row=1, column=5)

tk.Label(window, text="salary : ").grid(row=2,column=4)
s=tk.Entry(window)
s.grid(row=2, column=5)

tk.Label(window, text="Qualification : ").grid(row=3,column=4)
q=tk.Entry(window)
q.grid(row=3, column=5)

def insert2():
    doc_id=did.get()
    doc_name=dn.get()
    sal=s.get()
    qual=q.get()

    query="INSERT INTO Doctor(D_id,D_name,salary,Qualification) VALUES(%s,%s,%s,%s)"
    insert2=(doc_id,doc_name,sal,qual)
    cursor.execute(query,insert2)
    db.commit()


tk.Label(window, text="Record_id: ").grid(row=0,column=6)
r=tk.Entry(window)
r.grid(row=0, column=7)
    
tk.Label(window, text="Problem: ").grid(row=1,column=6)
p=tk.Entry(window)
p.grid(row=1, column=7)

tk.Label(window, text="Date_of_examination : ").grid(row=2,column=6)
date=tk.Entry(window)
date.grid(row=2, column=7)

def insert3():
    rec=r.get()
    prob=p.get()
    doe=date.get()

    query="INSERT INTO Medical(Record_id,Problem,Date_of_examination) VALUES(%s,%s,%s)"
    insert3=(rec,prob,doe)
    cursor.execute(query,insert3)
    db.commit()


tk.Label(window, text="Parking_id: ").grid(row=0,column=8)
parking=tk.Entry(window)
parking.grid(row=0, column=9)
    
tk.Label(window, text="Vehicle_no: ").grid(row=1,column=8)
v=tk.Entry(window)
v.grid(row=1, column=9)

def insert4():
    park=parking.get()
    veh=v.get()
    

    query="INSERT INTO Parking(Parking_id,Vehicle_no) VALUES(%s,%s)"
    insert4=(park,veh)
    cursor.execute(query,insert4)
    db.commit()


tk.Button(window, text="INSERT", command=insert).grid(row=4, column=1)
tk.Button(window, text="INSERT1", command=insert1).grid(row=4, column=3)
tk.Button(window, text="INSERT2", command=insert2).grid(row=4, column=5)
tk.Button(window, text="INSERT3", command=insert3).grid(row=4, column=7)
tk.Button(window, text="INSERT4", command=insert4).grid(row=4, column=9)


try:
    db=pymysql.connect(host= "localhost", user="Roopal", passwd="pankaj12",database="HOSPITAL_MANAGEMENT")
    cursor=db.cursor()
    #cursor.execute("CREATE DATABASE HOSPITAL_MANAGEMENT")
    

#except pymysql.err.ProgrammingError:
   # print("DATABASE ALREADY EXISTS")

finally:
    try:

        cursor.execute("CREATE TABLE Patient(P_id int primary key, P_name varchar(255), P_diagnosis varchar(200), P_address varchar(30))")
        cursor.execute("CREATE TABLE Hospital(H_id numeric(20), H_name varchar(255), H_city varchar(200), H_address varchar(30))")
        cursor.execute("CREATE TABLE Doctor(D_id numeric(20), D_name varchar(255), salary numeric(20), Qualification varchar(30))")
        cursor.execute("CREATE TABLE Medical(Record_id numeric(20), Problem varchar(255), Date_of_examination date)")
        cursor.execute("CREATE TABLE Parking(Parking_id numeric(20), Vehicle_no numeric(20))")
        


    
    except pymysql.err.InternalError:
        print("TABLE EXISTS !!")

   # finally:
     #  cursor.execute("INSERT INTO Patient(P_id,P_name,P_diagnosis,P_address) VALUES(%s,%s,%s,%s)" )

window.mainloop()