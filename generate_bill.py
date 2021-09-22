#import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox

conn=sqlite3.connect("storedb.db")
c=conn.cursor()
result=c.execute("SELECT Max(id) from inventory")
for r in result:
    id=r[0]

class Bill:
    def __init__(self, master, *args, **kwargs):
         self.master=master
         self.heading=Label(master, text="Generate Bill", font=('arial 40 bold'), fg='steelblue')
         self.heading.place(x=400, y=0)

         #lables  for the window
         self.name_l=Label(master,text="Product Name",font=('arial 18 bold'))
         self.name_l.place(x=0,y=70)

         self.stock_l=Label(master,text="Stocks",font=('arial 18 bold'))
         self.stock_l.place(x=0,y=120)

         self.cp_l = Label(master, text="Cost Price ", font=('arial 18 bold'))
         self.cp_l.place(x=0, y=170)

         self.sp_l = Label(master, text="Selling Price", font=('arial 18 bold'))
         self.sp_l.place(x=0, y=220)

         self.vendor_l = Label(master, text="Customer Name", font=('arial 18 bold'))
         self.vendor_l.place(x=0, y=270)

         self.vendor_phone_l = Label(master, text="Customer Phone Number", font=('arial 18 bold'))
         self.vendor_phone_l.place(x=0, y=320)

         self.id_l = Label(master, text="Enter ID", font=('arial 18 bold'))
         self.id_l.place(x=0, y=370)

        #enteries for window

         self.name_e=Label(master,Text)
         self.name_e.place(x=380,y=70)


         #button to add to the Bill
         self.btn_add=Button(master,text='Add to Bill',width=25,height=2,bg='steelblue',fg='white',command=self.get_items)
         self.btn_add.place(x=520,y=420)

         self.btn_clear=Button(master,text="Clear All Fields",width=18,height=2,bg='lightgreen',fg='white',command=self.clear_all)
         self.btn_clear.place(x=350,y=420)

          #text box for the log
         self.tbBox=Text(master,width=60,height=18)
         self.tbBox.place(x=750,y=70)
         self.tbBox.insert(END,"ID has reached up to:"+str(id))

         self.master.bind('<Return>', self.get_items)
         self.master.bind('<Up>', self.clear_all)

    def get_items(self, *args, **kwargs):
    # get from entries
       self.name = self.name_e.get()
       self.stock = self.get_items.get()
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
        self.tbBox.insert(END, "\n\nInseted " + str(self.name) + " into the Bill with code " + str(self.id_e.get()))
        tkinter.messagebox.showinfo("Success", "Successfully added to the Bill")


    def clear_all(self, *args, **kwargs):
       num = id + 1
       self.name_e.delete(0, END)
       self.stock_e.delete(0, END)
       self.cp_e.delete(0, END)
       self.sp_e.delete(0, END)
       self.vendor_e.delete(0, END)
       self.vendor_phone_e.delete(0, END)



blllWindow=Tk()
b=Bill(blllWindow)

blllWindow.geometry("1366x768+0+0")
blllWindow.title("Add in the Bill")
blllWindow.mainloop()