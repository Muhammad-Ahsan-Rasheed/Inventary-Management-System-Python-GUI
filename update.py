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
    def __init__(self,master,*args,**kwargs):
         self.master=master
         self.heading=Label(master,text="Update to the databse",font=('arial 40 bold'),fg='steelblue')
         self.heading.place(x=400,y=0)

         #label and entry for id
         self.id_le=Label(master,text="Enter ID",font=('arial 18 bold'))
         self.id_le.place(x=0,y=100)

         self.id_leb=Entry(master,font=('arial 18 bold'),width=10, bg='lightblue')
         self.id_leb.place(x=380,y=100)

         self.btn_search=Button(master,text="search",width=15,height=2,bg='orange',command=self.search)
         self.btn_search.place(x=550,y=100)

         #lables  for the window
         self.name_l=Label(master,text="Enter Product Name",font=('arial 18 bold'))
         self.name_l.place(x=0,y=150)

         self.stock_l=Label(master,text="Enter Stocks",font=('arial 18 bold'))
         self.stock_l.place(x=0,y=200)

         self.cp_l = Label(master, text="Enter Cost Price ", font=('arial 18 bold'))
         self.cp_l.place(x=0, y=250)

         self.sp_l = Label(master, text="Enter Selling Price", font=('arial 18 bold'))
         self.sp_l.place(x=0, y=300)

         self.totalcp_l = Label(master, text="Enter Total Cost Price", font=('arial 18 bold'))
         self.totalcp_l.place(x=0, y=350)

         self.totalsp_l = Label(master, text="Enter Total Selling Price", font=('arial 18 bold'))
         self.totalsp_l.place(x=0, y=400)

         self.vendor_l = Label(master, text="Enter Vender Name", font=('arial 18 bold'))
         self.vendor_l.place(x=0, y=450)

         self.vendor_phone_l = Label(master, text="Enter Vendor Phone Number", font=('arial 18 bold'))
         self.vendor_phone_l.place(x=0, y=500)

        #enteries for window

         self.name_e=Entry(master,width=25,font=('arial 18 bold'), bg='lightblue')
         self.name_e.place(x=380,y=150)

         self.stock_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.stock_e.place(x=380, y=200)

         self.cp_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.cp_e.place(x=380, y=250)

         self.sp_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.sp_e.place(x=380, y=300)

         self.totalcp_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.totalcp_e.place(x=380, y=350)

         self.totalsp_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.totalsp_e.place(x=380, y=400)

         self.vendor_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.vendor_e.place(x=380, y=450)

         self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'), bg='lightblue')
         self.vendor_phone_e.place(x=380, y=500)

         #button to add to the database
         self.btn_add=Button(master,text='Update Database',width=25,height=2,bg='steelblue',fg='white',command=self.update)
         self.btn_add.place(x=520,y=550)



          #text box for the log
         self.tbBox=Text(master,width=60,height=18, bg='lightblue')
         self.tbBox.place(x=750,y=100)
         self.tbBox.insert(END,"ID has reached up to:"+str(id))

    def search(self, *args, **kwargs):
         sql = "SELECT * FROM inventory WHERE id=?"
         result = c.execute(sql, (self.id_leb.get(),))
         for r in result:
              self.n1 = r[1]  # name
              self.n2 = r[2]  # stock
              self.n3 = r[3]  # cp
              self.n4 = r[4]  # sp
              self.n5 = r[5]  # total cp
              self.n6 = r[6]  # total sp
              self.n7 = r[7]  # assumed_profit
              self.n8 = r[8]  # vendor
              self.n9 = r[9]  # vendor_phone
         conn.commit()

          #inster into the enteries to update
         self.name_e.delete(0,END)
         self.name_e.insert(0, str(self.n1))

         self.stock_e.delete(0, END)
         self.stock_e.insert(0, str(self.n2))

         self.cp_e.delete(0, END)
         self.cp_e.insert(0, str(self.n3))

         self.sp_e.delete(0, END)
         self.sp_e.insert(0, str(self.n4))

         self.vendor_e.delete(0, END)
         self.vendor_e.insert(0, str(self.n8))

         self.vendor_phone_e.delete(0, END)
         self.vendor_phone_e.insert(0, str(self.n9))

         self.totalcp_e.delete(0, END)
         self.totalcp_e.insert(0, str(self.n5))

         self.totalsp_e.delete(0, END)
         self.totalsp_e.insert(0, str(self.n6))

    def update(self,*args,**kwargs):
          self.u1=self.name_e.get()
          self.u2 = self.stock_e.get()
          self.u3 = self.cp_e.get()
          self.u4 = self.sp_e.get()
          self.u5 = self.totalcp_e.get()
          self.u6 = self.totalsp_e.get()
          self.u7 = self.vendor_e.get()
          self.u8 = self.vendor_phone_e.get()


          query="UPDATE  inventory SET name=?,stock=?,cp=?,sp=?,totalcp=?,totalsp=?,vendor=?,vendor_phoneno=?  WHERE id=?"
          c.execute(query,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.u8,self.id_leb.get()))
          conn.commit()
          tkinter.messagebox.showinfo("Success","Update Database successfully")

