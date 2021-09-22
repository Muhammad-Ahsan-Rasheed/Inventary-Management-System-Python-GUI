#import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox

conn=sqlite3.connect("storedb.db")
c=conn.cursor()
result=c.execute("SELECT Max(id) from inventory")
for r in result:
    id=r[0]

class Database:
    def __init__(self, master, *args, **kwargs):
         self.master=master
         self.heading=Label(master, text="Add in the databse", font=('arial 40 bold'), fg='steelblue')
         self.heading.place(x=400, y=0)

         #lables  for the window
         self.name_l=Label(master,text="Enter Product Name",font=('arial 18 bold'))
         self.name_l.place(x=0,y=100)

         self.stock_l=Label(master,text="Enter Stocks",font=('arial 18 bold'))
         self.stock_l.place(x=0,y=150)

         self.cp_l = Label(master, text="Enter Cost Price ", font=('arial 18 bold'))
         self.cp_l.place(x=0, y=200)

         self.sp_l = Label(master, text="Enter Selling Price", font=('arial 18 bold'))
         self.sp_l.place(x=0, y=250)

         self.vendor_l = Label(master, text="Enter Vender Name", font=('arial 18 bold'))
         self.vendor_l.place(x=0, y=300)

         self.vendor_phone_l = Label(master, text="Enter Vendor Phone Number", font=('arial 18 bold'))
         self.vendor_phone_l.place(x=0, y=350)

         self.id_l = Label(master, text="Enter ID", font=('arial 18 bold'))
         self.id_l.place(x=0, y=400)

        #enteries for window

         self.name_e=Entry(master,width=25,font=('arial 18 bold'), bg='lightblue')
         self.name_e.place(x=380,y=100)

         self.stock_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.stock_e.place(x=380, y=150)

         self.cp_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.cp_e.place(x=380, y=200)

         self.sp_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.sp_e.place(x=380, y=250)

         self.vendor_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.vendor_e.place(x=380, y=300)

         self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.vendor_phone_e.place(x=380, y=350)

         self.id_e=Entry(master,width=25,font=('arial 18 bold'), bg='lightblue')
         self.id_e.place(x=380,y=400)

         #button to add to the database
         self.btn_add=Button(master,text='Add to Database',width=25,height=2,bg='steelblue',fg='white',command=self.get_items)
         self.btn_add.place(x=520,y=450)

         self.btn_clear=Button(master,text="Clear All Fields",width=21,height=2,bg='lightgreen',fg='white',command=self.clear_all)
         self.btn_clear.place(x=360,y=450)

          #text box for the log
         self.tbBox=Text(master,width=60,height=18)
         self.tbBox.place(x=750,y=100)
         self.tbBox.insert(END,"ID has reached up to:"+str(id))

         self.master.bind('<Return>', self.get_items)
         self.master.bind('<Up>', self.clear_all)

    def get_items(self, *args, **kwargs):
    # get from entries
       self.name = self.name_e.get()
       self.stock = self.stock_e.get()
       self.cp = self.cp_e.get()
       self.sp = self.sp_e.get()
       self.vendor = self.vendor_e.get()
       self.vendor_phone = self.vendor_phone_e.get()

    # dynamic entries
       self.totalcp = float(self.cp) * float(self.stock)
       self.totalsp = float(self.sp) * float(self.stock)
       self.assumed_profit = float(self.totalsp - self.totalcp)

       if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
        tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
       else:
        sql = "INSERT INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno ) VALUES(?,?,?,?,?,?,?,?,?)"
        c.execute(sql, (
        self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor,
        self.vendor_phone))
        conn.commit()
        # textbox insert
        self.tbBox.insert(END, "\n\nInserted " + str(self.name) + " into the database with code " + str(self.id_e.get()))
        tkinter.messagebox.showinfo("Success", "Successfully added to the database")



    def clear_all(self, *args, **kwargs):
       num = id + 1
       self.name_e.delete(0, END)
       self.stock_e.delete(0, END)
       self.cp_e.delete(0, END)
       self.sp_e.delete(0, END)
       self.vendor_e.delete(0, END)
       self.vendor_phone_e.delete(0, END)