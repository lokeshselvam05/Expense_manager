import pymysql
import datetime



class DBM:

    store_login_id=str()
    d=tuple()
    store_name=str()
    

    def __init__(self):
        self.db=pymysql.connect("localhost","root","","project1")
        self.c=self.db.cursor()

    def create_table(self):
        try:
            self.c.execute("""create table SIGN_UP(name varchar(26),ID int,Mobile_num bigint,login_id varchar(26),password varchar(26),confirm_password varchar(26),created_time varchar(200),updated_time varchar(200),primary key(id))""")
        except Exception as e:
            print(e)


    def insert_record(self,ent1,ent2,ent3,ent4,ent5,ent6):
        created_time=datetime.datetime.now()
        updated_time=""
        self.c.execute("""insert into SIGN_UP(name,id,mobile_num,login_id,password,confirm_password,created_time,updated_time)values("{}",{},{},"{}","{}","{}","{}","{}")""".format(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent6.get(),created_time,updated_time))
        self.db.commit()


    def select_record(self):
        print(self.store_login_id)
        self.c.execute(""" select * from SIGN_UP where login_id='{}'""".format(self.store_login_id))
        self.d=self.c.fetchall()


    def profile_insert_record(self,ent1,ent2,ent3,ent4,ent5,ent6):
        updated_time=datetime.datetime.now()
        self.c.execute("""UPDATE SIGN_UP SET name='{}',id='{}',mobile_num='{}',login_id='{}',password='{}',confirm_password='{}',updated_time='{}'where login_id = '{}'""".format(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent6.get(),updated_time,self.store_login_id))
        self.db.commit()


    def create_expense_table(self):
        try:
            self.c.execute("""create table EXPENSES(name varchar(26),ID int,GROCERIES int,RECHARGE_BILL int,CURRENT_BILL int,WIFI_BILL int,TRANSPORT int,EMI int,created_time varchar(200),updated_time varchar(200),Created_Total bigint,Updated_Total bigint,foreign key(id)references sign_up(id))""")
        except Exception as e:
            print(e)

            
    def insert_expense_record(self,ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8):
        created_time=datetime.datetime.now()
        updated_time=""
        Created_Total=int(ent3.get())+int(ent4.get())+int(ent5.get())+int(ent6.get())+int(ent7.get())+int(ent8.get())
        Updated_Total=int()
        self.c.execute("""insert into EXPENSES(name,ID,Groceries,Recharge_bill,Current_bill,Wifi_bill,Transport,Emi,created_time,updated_time,Created_Total,Updated_Total)values("{}",{},{},{},{},{},{},{},"{}","{}",{},{})""".format(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent6.get(),ent7.get(),ent8.get(),created_time,updated_time,Created_Total,Updated_Total))
        self.db.commit()


    def select_expense_record(self):
        print(self.store_name)
        self.c.execute("""select * from EXPENSES where name='{}'limit 1""".format(self.store_name))
        self.d=self.c.fetchall()

    def expense_update_insert_record(self,ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8):
        updated_time=datetime.datetime.now()
        Updated_Total=int(ent3.get())+int(ent4.get())+int(ent5.get())+int(ent6.get())+int(ent7.get())+int(ent8.get())
        self.c.execute("""UPDATE EXPENSES SET name='{}',id='{}',Groceries='{}',Recharge_bill='{}',Current_bill='{}',Wifi_bill='{}',Transport='{}',Emi='{}',updated_time='{}',Updated_Total='{}'where name='{}'""".format(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent6.get(),ent7.get(),ent8.get(),updated_time,Updated_Total,self.store_name))
        self.db.commit()









        


        
        
        

    



