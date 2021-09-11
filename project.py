#PROJECT:
from tkinter import*
from tkinter import messagebox
from projectdb import DBM
from update import PEU
window=Tk()
class EM(PEU):
    
    
    def login_page(self):
        def submit_record():
            if ent1.get()=="" or ent2.get()=="":
                messagebox.showinfo('Question',"empty field",icon='warning')
            else:
                self.c.execute("""select login_id,password,name from sign_up where login_id="{}" and password='{}'""".format(ent1.get(),ent2.get()))
                DBM.d=self.c.fetchall()
                try:
                    if(DBM.d[0][0]==ent1.get() and DBM.d[0][1]==ent2.get()):
                        print("user&passwrd crrt")
                        messagebox.showinfo('Answer',"valid login id & password")
                        DBM.store_login_id=DBM.d[0][0]
                        DBM.store_name=DBM.d[0][2]
                        obj.display()
                except Exception as e:
                    print(e)
                    messagebox.showinfo('Answer',"Invalid login id or password",icon="warning")
            

        def reset_record():
            if ent1.get()=="" and ent2.get()=="":
                messagebox.showinfo('Question',"empty fields",icon="warning")
            else:
                ent1.delete(0,END)
                ent2.delete(0,END)
                messagebox.showinfo('Answer',"cleared")
            
            

        def sign_up():

            def call_insert_record():
                if ent1.get()=="" or ent2.get()=="" or ent3.get()=="" or ent4.get()=="" or ent5.get()=="" or ent6.get()=="":
                    messagebox.showinfo('Question',"some fields are empty",icon='warning')
                    
                else:
                    if ent5.get()==ent6.get():
                        obj.insert_record(ent1,ent2,ent3,ent4,ent5,ent6)
                        messagebox.showinfo('Answer',"sign-in successfull")
                    else:
                        messagebox.showinfo('Question',"password & confirm password is different",icon='warning')
            def clear_record():
                    ent1.delete(0,END)
                    ent2.delete(0,END)
                    ent3.delete(0,END)
                    ent4.delete(0,END)
                    ent5.delete(0,END)
                    ent6.delete(0,END)
                    messagebox.showinfo('Answer',"cleared")
                
                
        
            self.window1=Tk()
            self.window1.title("SIGN-UP")
            self.window1.geometry("500x650")
            lb1=Label(self.window1,text="ACCOUNT SIGN-UP",font=("Arabic Bold",30))
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
            ent2=Entry(self.window1,text="enter the id",fg="black",bg="white",font=15)
            ent2.place(x=270,y=200)
            ent3=Entry(self.window1,text="enter the mobile number",fg="black",bg="white",font=15)
            ent3.place(x=270,y=250)
            ent4=Entry(self.window1,text="enter the login id",fg="black",bg="white",font=15)
            ent4.place(x=270,y=300)
            ent5=Entry(self.window1,text="enter the password",fg="black",bg="white",font=15,show="*")
            ent5.place(x=270,y=350)
            ent6=Entry(self.window1,text="enter the confirmed password",fg="black",bg="white",font=15,show="*")
            ent6.place(x=270,y=400)
            bt1=Button(self.window1,text="SIGN-IN",fg="red",bg="white",command=call_insert_record)
            bt1.place(x=50,y=450)
            bt2=Button(self.window1,text="CANCEL",fg="red",bg="white",command=clear_record)
            bt2.place(x=150,y=450)
            bt3=Button(self.window1,text="Quit",fg="red",bg="white",command=self.window1.destroy)
            bt3.place(x=250,y=450)
            self.window1.mainloop()
            
            
            
                                                                 

        window.title("EXPENSE MANAGER")
        window.geometry("500x550")
        lb1=Label(window,text="EXPENSE MANAGER",font=("Arabic Bold",30))
        lb1.place(x=70,y=80)
        lb2=Label(window,text="LOGIN ID",font=("Arabic Bold",20))
        lb2.place(x=50,y=150)
        lb3=Label(window,text="PASSWORD",font=("Arabic Bold",20))
        lb3.place(x=50,y=210)
        ent1=Entry(window,text="enter the id",fg="black",bg="white",font=26)
        ent1.place(x=220,y=160)
        ent2=Entry(window,text="enter the password",fg="black",bg="white",font=26,show="*")
        ent2.place(x=220,y=220)
        bt1=Button(window,text="submit",fg="red",bg="white",command=submit_record)
        bt1.place(x=80,y=280)
        bt2=Button(window,text="Cancel",fg="red",bg="white",command=reset_record)
        bt2.place(x=170,y=280)
        bt3=Button(window,text="Sign-up",fg="red",bg="white",command=sign_up)
        bt3.place(x=270,y=280)
        bt4=Button(window,text="Quit",fg="red",bg="white",command=window.destroy)
        bt4.place(x=350,y=280)
        window.mainloop()
obj=EM()
obj.create_table()
obj.login_page()




            




    




