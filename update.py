from tkinter import*
from tkinter import messagebox
from projectdb import DBM


class PEU(DBM):

    def display(self):

        def call_update_expense():
            def call_update_exepense_insert_record():
                db_object1.expense_update_insert_record(ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8)
                if ent1.get()=="" or ent2.get()=="" or ent3.get()=="" or ent4.get()=="" or ent5.get()=="" or ent6.get()=="" or ent7.get()=="" or ent8.get()=="":
                    messagebox.showinfo('Question',"empty field",icon='warning')
                else:
                    messagebox.showinfo('Answer',"successfully updated")

            def call_update_expense_clear_record():
                ent1.delete(0,END)
                ent2.delete(0,END)
                ent3.delete(0,END)
                ent4.delete(0,END)
                ent5.delete(0,END)
                ent6.delete(0,END)
                ent7.delete(0,END)
                ent8.delete(0,END)
                messagebox.showinfo('Answer',"cleared")
                
            


            
            db_object1=DBM()
            db_object1.select_expense_record()
            self.window2=Tk()
            self.window2.title("EXPENSES")
            self.window2.geometry("650x700")
            lb1=Label(self.window2,text="UPDATE EXPENSE",font=("Arabic Bold",30))
            lb1.place(x=70,y=80)
            lb2=Label(self.window2,text="NAME",font=("Arabic Bold",15))
            lb2.place(x=50,y=150)
            lb3=Label(self.window2,text="ID",font=("Arabic Bold",15))
            lb3.place(x=50,y=200)
            lb4=Label(self.window2,text="GROCERIES",font=("Arabic Bold",15))
            lb4.place(x=50,y=250)
            lb5=Label(self.window2,text="RECHARGE BILL",font=("Arabic Bold",15))
            lb5.place(x=50,y=300)
            lb6=Label(self.window2,text="CURRENT BILL",font=("Arabic Bold",15))
            lb6.place(x=50,y=350)
            lb7=Label(self.window2,text="WIFI BILL",font=("Arabic Bold",15))
            lb7.place(x=50,y=400)
            lb8=Label(self.window2,text="TRANSPORT",font=("Arabic Bold",15))
            lb8.place(x=50,y=450)
            lb9=Label(self.window2,text="EMI",font=("Arabic Bold",15))
            lb9.place(x=50,y=500)
            ent1=Entry(self.window2,text="enter the name",fg="black",bg="white",font=15)
            ent1.place(x=270,y=150)
            ent1.insert(0,db_object1.d[0][0])
            ent2=Entry(self.window2,text="enter the id",fg="black",bg="white",font=15)
            ent2.place(x=270,y=200)
            ent2.insert(0,db_object1.d[0][1])
            ent3=Entry(self.window2,text="money invested in groceries",fg="black",bg="white",font=15)
            ent3.place(x=270,y=250)
            ent3.insert(0,db_object1.d[0][2])
            ent4=Entry(self.window2,text="money invested in mobile recharge",fg="black",bg="white",font=15)
            ent4.place(x=270,y=300)
            ent4.insert(0,db_object1.d[0][3])
            ent5=Entry(self.window2,text="money invested in usage of current",fg="black",bg="white",font=15)
            ent5.place(x=270,y=350)
            ent5.insert(0,db_object1.d[0][4])
            ent6=Entry(self.window2,text="money invested in usage of wifi",fg="black",bg="white",font=15)
            ent6.place(x=270,y=400)
            ent6.insert(0,db_object1.d[0][5])
            ent7=Entry(self.window2,text="money invested in usage of personal transport",fg="black",bg="white",font=15)
            ent7.place(x=270,y=450)
            ent7.insert(0,db_object1.d[0][6])
            ent8=Entry(self.window2,text="money invested in emi products",fg="black",bg="white",font=15)
            ent8.place(x=270,y=500)
            ent8.insert(0,db_object1.d[0][7])
            bt1=Button(self.window2,text="UPDATE",fg="red",bg="white",command=call_update_exepense_insert_record)
            bt1.place(x=50,y=550)
            bt2=Button(self.window2,text="CANCEL",fg="red",bg="white",command=call_update_expense_clear_record)
            bt2.place(x=150,y=550)
            bt3=Button(self.window2,text="Quit",fg="red",bg="white",command=self.window2.destroy)
            bt3.place(x=250,y=550)
            self.window2.mainloop()

        
        def call_create_expense():
            def call_E_insert_record():
                db_object_dbm=DBM()
                db_object_dbm.create_expense_table()
                db_object_dbm.insert_expense_record(ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8)
                if ent1.get()=="" or ent2.get()=="" or ent3.get()=="" or ent4.get()=="" or ent5.get()=="" or ent6.get()=="" or ent7.get()=="" or ent8.get()=="":
                    messagebox.showinfo('Question',"empty field",icon='warning')
                else:
                    messagebox.showinfo('Answer',"Expenses created successfully")
    
            def call_E_clear_record():
                ent1.delete(0,END)
                ent2.delete(0,END)
                ent3.delete(0,END)
                ent4.delete(0,END)
                ent5.delete(0,END)
                ent6.delete(0,END)
                ent7.delete(0,END)
                ent8.delete(0,END)
                messagebox.showinfo('Answer',"cleared")
                
                    
            self.window2=Tk()
            self.window2.title("EXPENSES")
            self.window2.geometry("650x700")
            lb1=Label(self.window2,text="USER EXPENSE",font=("Arabic Bold",30))
            lb1.place(x=70,y=80)
            lb2=Label(self.window2,text="NAME",font=("Arabic Bold",15))
            lb2.place(x=50,y=150)
            lb3=Label(self.window2,text="ID",font=("Arabic Bold",15))
            lb3.place(x=50,y=200)
            lb4=Label(self.window2,text="GROCERIES",font=("Arabic Bold",15))
            lb4.place(x=50,y=250)
            lb5=Label(self.window2,text="RECHARGE BILL",font=("Arabic Bold",15))
            lb5.place(x=50,y=300)
            lb6=Label(self.window2,text="CURRENT BILL",font=("Arabic Bold",15))
            lb6.place(x=50,y=350)
            lb7=Label(self.window2,text="WIFI BILL",font=("Arabic Bold",15))
            lb7.place(x=50,y=400)
            lb8=Label(self.window2,text="TRANSPORT",font=("Arabic Bold",15))
            lb8.place(x=50,y=450)
            lb9=Label(self.window2,text="EMI",font=("Arabic Bold",15))
            lb9.place(x=50,y=500)
            ent1=Entry(self.window2,text="enter the name",fg="black",bg="white",font=15)
            ent1.place(x=270,y=150)
            ent2=Entry(self.window2,text="enter the id",fg="black",bg="white",font=15)
            ent2.place(x=270,y=200)
            ent3=Entry(self.window2,text="money invested in groceries",fg="black",bg="white",font=15)
            ent3.place(x=270,y=250)
            ent4=Entry(self.window2,text="money invested in mobile recharge",fg="black",bg="white",font=15)
            ent4.place(x=270,y=300)
            ent5=Entry(self.window2,text="money invested in usage of current",fg="black",bg="white",font=15)
            ent5.place(x=270,y=350)
            ent6=Entry(self.window2,text="money invested in usage of wifi",fg="black",bg="white",font=15)
            ent6.place(x=270,y=400)
            ent7=Entry(self.window2,text="money invested in usage of personal transport",fg="black",bg="white",font=15)
            ent7.place(x=270,y=450)
            ent8=Entry(self.window2,text="money invested in emi products",fg="black",bg="white",font=15)
            ent8.place(x=270,y=500)
            bt1=Button(self.window2,text="CREATE",fg="red",bg="white",command=call_E_insert_record)
            bt1.place(x=50,y=550)
            bt2=Button(self.window2,text="CANCEL",fg="red",bg="white",command=call_E_clear_record)
            bt2.place(x=150,y=550)
            bt3=Button(self.window2,text="Quit",fg="red",bg="white",command=self.window2.destroy)
            bt3.place(x=250,y=550)
            self.window2.mainloop()



        def call_profile():
            def call_profile_insert_record():  
                db_object.profile_insert_record(ent1,ent2,ent3,ent4,ent5,ent6)
                if ent1.get()=="" or ent2.get()=="" or ent3.get()=="" or ent4.get()=="" or ent5.get()=="" or ent6.get()=="":
                    messagebox.showinfo('Question',"empty field",icon='warning')
                else:
                    messagebox.showinfo('Answer',"successfully updated")

            def call_cancel():
                    ent1.delete(0,END)
                    ent2.delete(0,END)
                    ent3.delete(0,END)
                    ent4.delete(0,END)
                    ent5.delete(0,END)
                    ent6.delete(0,END)
                    messagebox.showinfo('Answer',"cleared")
            
            
            db_object=DBM()
            db_object.select_record()  
            self.window1=Tk()
            self.window1.title("profile")
            self.window1.geometry("500x650")
            lb1=Label(self.window1,text="PROFILE UPDATE",font=("Arabic Bold",30))
            lb1.place(x=70,y=80)
            lb2=Label(self.window1,text="NAME",font=("Arabic Bold",15))
            lb2.place(x=50,y=150)
            lb3=Label(self.window1,text="ID",font=("Arabic Bold",15))
            lb3.place(x=50,y=200)
            lb4=Label(self.window1,text="MOBILE NUM",font=("Arabic Bold",15))
            lb4.place(x=50,y=250)
            lb5=Label(self.window1,text="LOGIN ID",font=("Arabic Bold",15))
            lb5.place(x=50,y=300)
            lb6=Label(self.window1,text="PASSWORD",font=("Arabic Bold",15))
            lb6.place(x=50,y=350)
            lb7=Label(self.window1,text="CONFIRM PASSWORD",font=("Arabic Bold",15))
            lb7.place(x=50,y=400)
            ent1=Entry(self.window1,text="enter the name",fg="black",bg="white",font=15)
            ent1.place(x=270,y=150)
            ent1.insert(0,db_object.d[0][0])
            ent2=Entry(self.window1,text="enter the id",fg="black",bg="white",font=15)
            ent2.place(x=270,y=200)
            ent2.insert(0,db_object.d[0][1])
            ent3=Entry(self.window1,text="enter the mobile number",fg="black",bg="white",font=15)
            ent3.place(x=270,y=250)
            ent3.insert(0,db_object.d[0][2])
            ent4=Entry(self.window1,text="enter the login id",fg="black",bg="white",font=15)
            ent4.place(x=270,y=300)
            ent4.insert(0,db_object.d[0][3])
            ent5=Entry(self.window1,text="enter the password",fg="black",bg="white",font=15,show="*")
            ent5.place(x=270,y=350)
            ent5.insert(0,db_object.d[0][4])
            ent6=Entry(self.window1,text="enter the confirmed password",fg="black",bg="white",font=15,show="*")
            ent6.place(x=270,y=400)
            ent6.insert(0,db_object.d[0][5])
            bt1=Button(self.window1,text="UPDATE",fg="red",bg="white",command=call_profile_insert_record)
            bt1.place(x=50,y=450)
            bt2=Button(self.window1,text="CANCEL",fg="red",bg="white",command=call_cancel)
            bt2.place(x=150,y=450)
            bt3=Button(self.window1,text="Quit",fg="red",bg="white",command=self.window1.destroy)
            bt3.place(x=250,y=450)
            self.window1.mainloop()
            
            
                            
        
        self.window3=Tk()
        self.window3.title("PROFILE")
        self.window3.geometry("400x450")
        lb1=Label(self.window3,text="UPDATION",font=("Arabic Bold",30))
        lb1.place(x=70,y=80)
        bt1=Button(self.window3,text="PROFILE",fg="red",bg="white",command=call_profile)
        bt1.place(x=145,y=150)
        bt2=Button(self.window3,text="CREATE EXPENSES",fg="red",bg="white",command=call_create_expense)
        bt2.place(x=120,y=200)
        bt3=Button(self.window3,text="UPDATE EXPENSES",fg="red",bg="white",command=call_update_expense)
        bt3.place(x=120,y=250)
        bt4=Button(self.window3,text="LOG OUT",fg="red",bg="white",command=self.window3.destroy)
        bt4.place(x=140,y=300)
        self.window3.mainloop()



            
    
