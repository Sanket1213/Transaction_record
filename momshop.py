 from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from datetime import datetime
import time
import math,random
import os.path
import sys

class MomShop:
    def checkDir(self):
        check=os.path.exists("C_Record")
        if check==0:
            self.makeDir()
            
    def __init__(self,root):
        self.checkDir()
        self.root=root
        self.root.title("Shri Garments")
        self.root.geometry("1350x700+0+0")

        self.Date1= StringVar()
        self.Date1.set(time.strftime("%d/%m/%y"))

        Time1= StringVar()
        val=time.strftime("%I:%M:%S")
        Time1.set(val)
        # Title========================================================================
        Title_frame=Frame(self.root, bd=4, relief=RIDGE)
        Title_frame.pack(side=TOP, fill=X)

        title=Label(Title_frame, text="Shri Garments", bd=5, relief=GROOVE, font=("times new roman",40,"bold"), bg="light grey", fg="black")
        title.pack(side=TOP, fill=X)

        # Date Nad time Area===========================================================
        title_date=Label(self.root, textvariable=self.Date1, font=("times new roman",20,"bold"), bg="light grey", fg="black")
        title_date.place(x=15, y=15, width=100)
        title_time=Label(self.root,textvariable=Time1, font=("times new roman",20,"bold"), bg="light grey", fg="black")
        title_time.place(x=1230, y=15, width=100)

        # All Variables=================================================================
        self.Name_var=StringVar()
        self.Contact_var=StringVar()
        self.Total_var=IntVar()
        self.Paid_var=IntVar()
        self.Remaining_var=IntVar()
        self.Page_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
        #===========================================================
        # self.Total_var.set("0")
        # self.Paid_var.set("0")
        # self.Remaining_var.set("0")

        def iExit():
            iExit=messagebox.askyesno("Customer Billing System","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return
        
        # Customer Details==============================================================

        Details_Frame=Frame(self.root, bd=4, relief=RIDGE)#, bg="crimson")
        Details_Frame.place(x=20, y=100, width=500, height=580)

        D_title=Label(Details_Frame,text="Customer Details", font=("times new roman",30,"bold"), fg="black")
        D_title.grid(row=0, columnspan=2, pady=10)

        lbl_page=Label(Details_Frame,text="Page No.:", font=("times new roman",18,"bold"), fg="black")
        lbl_page.grid(row=1, column=0, pady=10, padx=18, sticky="w")

        txt_page=Entry(Details_Frame,textvariable=self.Page_var, font=("times new roman",18,"bold"), bd=2, relief=GROOVE)
        txt_page.grid(row=1, column=1, pady=10, padx=18, sticky="w")

        lbl_name=Label(Details_Frame,text="Name:", font=("times new roman",18,"bold"), fg="black")
        lbl_name.grid(row=2, column=0, pady=10, padx=18, sticky="w")

        txt_name=Entry(Details_Frame,textvariable=self.Name_var, font=("times new roman",18,"bold"), bd=2, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=18, sticky="w")

        lbl_contact=Label(Details_Frame,text="Contact:", font=("times new roman",18,"bold"), fg="black")
        lbl_contact.grid(row=3, column=0, pady=10, padx=18, sticky="w")

        txt_contact=Entry(Details_Frame,textvariable=self.Contact_var, font=("times new roman",18,"bold"), bd=2, relief=GROOVE)
        txt_contact.grid(row=3, column=1, pady=10, padx=18, sticky="w")

        lbl_totalAmmount=Label(Details_Frame,text="Total Ammount:", font=("times new roman",18,"bold"), fg="black")
        lbl_totalAmmount.grid(row=4, column=0, pady=10, padx=18, sticky="w")

        txt_totalAmmount=Entry(Details_Frame,textvariable=self.Total_var, font=("times new roman",18,"bold"), bd=2, relief=GROOVE)
        txt_totalAmmount.grid(row=4, column=1, pady=10, padx=18, sticky="w")

        lbl_paidAmmount=Label(Details_Frame,text="Paid Ammount:", font=("times new roman",18,"bold"), fg="black")
        lbl_paidAmmount.grid(row=5, column=0, pady=10, padx=18, sticky="w")

        txt_paidAmmount=Entry(Details_Frame,textvariable=self.Paid_var, font=("times new roman",18,"bold"), bd=2, relief=GROOVE)
        txt_paidAmmount.grid(row=5, column=1, pady=10, padx=18, sticky="w")

        lbl_remaining=Label(Details_Frame,text="Remaining A.", font=("times new roman",18,"bold"), fg="black")
        lbl_remaining.grid(row=6, column=0, pady=10, padx=18, sticky="w")

        txt_remaining=Entry(Details_Frame,textvariable=self.Remaining_var, font=("times new roman",18,"bold"), bd=2, relief=GROOVE)
        txt_remaining.grid(row=6, column=1, pady=10, padx=18, sticky="w")

        # Button Frame=========================================
        btn_Frame=Frame(Details_Frame, relief=RIDGE)#, bg="crimson")
        btn_Frame.place(x=10, y=445, width=450)

        Addbtn=Button(btn_Frame, text="Add",font=('arial',12,'bold'), width=20, command=self.check).grid(row=0, column=0, padx=10, pady=5)
        Update_Details_btn=Button(btn_Frame, text="Update Detalis",font=('arial',12,'bold'), width=20, command=self.Update_Details).grid(row=1, column=0, padx=10, pady=5)
        Update_Transation_btn=Button(btn_Frame, text="Clear",font=('arial',12,'bold'), width=20, command=self.Clear).grid(row=0, column=1, padx=10, pady=5)
        Exitbtn=Button(btn_Frame, text="Exit",font=('arial',12,'bold'), width=20, command=iExit).grid(row=1, column=1, padx=10, pady=5)

        # Search Data====================================================
        Search_Frame=Frame(self.root, bd=4, relief=RIDGE)#, bg="crimson")
        Search_Frame.place(x=550, y=100, width=775, height=180)

        lbl_search=Label(Search_Frame,text="Search by Name:", font=("times new roman",20,"bold"), fg="black")
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        txt_search=Entry(Search_Frame, font=("times new roman",15,"bold"),textvariable=self.search_txt, bd=2, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn=Button(Search_Frame, text="Search", width=10, command=self.search_data)
        Searchbtn.grid(row=0, column=3, padx=10, pady=10)

        # search record=============================================

        Table_Frame=Frame(Search_Frame, relief=RIDGE)#, bg="crimson")
        Table_Frame.place(x=10, y=57, width=750, height=100)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)

        self.Customer_record=ttk.Treeview(Table_Frame,columns=("page","date","name","contact","total","paid","remaining"),xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.Customer_record.xview)
        self.Customer_record.heading("page",text="Page No.")
        self.Customer_record.heading("date", text="Date")
        self.Customer_record.heading("name",text="Name")
        self.Customer_record.heading("contact",text="Contact")
        self.Customer_record.heading("total",text="Total")
        self.Customer_record.heading("paid",text="Paid")
        self.Customer_record.heading("remaining",text="Remaining")
        self.Customer_record['show']='headings' 
        self.Customer_record.column("page",width=100)
        self.Customer_record.column("date",width=100)
        self.Customer_record.column("name",width=150)
        self.Customer_record.column("contact",width=150)
        self.Customer_record.column("total",width=100)
        self.Customer_record.column("paid",width=100)
        self.Customer_record.pack(fill=BOTH,expand=1)
        self.Customer_record.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

        # file area==========================================

        File_Frame=Frame(self.root, bd=4, relief=RIDGE)#, bg="crimson")
        File_Frame.place(x=550, y=290, width=775, height=75)

        lbl_transaction=Label(File_Frame,text="Transaction Record", font=("times new roman",20,"bold"), fg="black").pack(fill=X)
        # self.His_File=Text(File_Frame)
        # self.His_File.pack(fill=X,expand=1)

        self.file_list=Listbox(File_Frame, font="4")
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.Print_Data)

        # Bill area===========================================

        History_frame=Frame(self.root, bd=4, relief=RIDGE)
        History_frame.place(x=550, y=375, width=775, height=300)

        History_Title=Label(History_frame, text="History", font=("times new roman",20,"bold"), fg="black").pack(fill=X)
        scrol_y=Scrollbar(History_frame,orient=VERTICAL)
        self.textarea=Text(History_frame, yscrollcommand=scrol_y)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        

        self.Welcome_Bill()

        #===========================================================

    def check(self):
        if self.Page_var.get()=="":
            messagebox.showerror("Error","Page number required.")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="mom_shop",port=3307)
            cur=con.cursor()
            cur.execute("select * from customer where Page_no="+str(self.Page_var.get()))
            x=cur.fetchall()
            if len(x)==0:
                self.add_data()
            
            else:
                messagebox.showerror("Error", "Page Occupied")
            con.commit()
            # self.fetch_data()
            # self.Clear()
            con.close()
            

    def add_data(self):
        global r
        t=float(self.Total_var.get())
        p=float(self.Paid_var.get())
        r=int(t-p)
        if self.Name_var.get()=="" or self.Page_var.get()=="" or self.Contact_var.get()=="" or self.Total_var.get()=="0":
            messagebox.showerror("Error","All fields are required.")
        else:
            self.Create_File()    
            con=pymysql.connect(host="localhost",user="root",password="",database="mom_shop",port=3307)
            cur=con.cursor()
            #self.Customer_record.delete(*self.Customer_record.get_children())
            cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s)",(  self.Page_var.get(),
                                                                            self.Date1.get(),
                                                                            self.Name_var.get(),
                                                                            self.Contact_var.get(),
                                                                            self.Total_var.get(),
                                                                            self.Paid_var.get(),
                                                                            r
                                                                            ))
            con.commit()
            self.fetch_data()
            self.Remaining_var.set(r)
            #self.Clear()
            con.close()
            messagebox.showinfo("Success","Record has been Created.")
             
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="mom_shop",port=3307)
        cur=con.cursor()
        cur.execute("select * from customer")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Customer_record.delete(*self.Customer_record.get_children())
            for row in rows:
                self.Customer_record.insert('',END,values=row)
            con.commit()
        con.close()

    def get_cursor(self, event):
        cursour_row=self.Customer_record.focus()
        contents=self.Customer_record.item(cursour_row)
        row=contents['values']
        self.Page_var.set(row[0])
        self.Name_var.set(row[2])
        self.Contact_var.set(row[3])
        self.Total_var.set(row[4])
        self.Paid_var.set(row[5])
        self.Remaining_var.set(row[6])
        self.Welcome_Bill()
            #self.dob_var.set(row[5])

    def search_data(self):
        if self.search_txt.get()=="":
            messagebox.showerror("Error","Enter again.")
        else:
            self.Show_List()
            con=pymysql.connect(host="localhost",user="root",password="",database="mom_shop",port=3307)
            cur=con.cursor()
            cur.execute("select * from customer where C_Name LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Customer_record.delete(*self.Customer_record.get_children())
                for row in rows:
                    self.Customer_record.insert('',END,values=row)
                con.commit()
            con.close()

    def Clear(self):
        self.Page_var.set("")
        self.Name_var.set("")
        self.Contact_var.set("")
        self.Total_var.set("")
        self.Paid_var.set("")
        self.Remaining_var.set("")

    def Update_Details(self):
        global r
        t=float(self.Total_var.get())
        p=float(self.Paid_var.get())
        r=int(t-p)
        if self.Name_var.get()=="" or self.Page_var.get()=="" or self.Contact_var.get()=="" or self.Total_var.get()=="0":
            messagebox.showerror("Error","All fields are required.")
        else:
            self.Append()
            con=pymysql.connect(host="localhost",user="root",password="",database="mom_shop",port=3307)
            cur=con.cursor()
            cur.execute("update customer set C_Name=%s,C_Contact=%s, Total_Amount=%s,Paid_Amount=%s,Remaining_Amount=%s where Page_no=%s",(self.Name_var.get(),
                                                                                self.Contact_var.get(),
                                                                                self.Total_var.get(),self.Paid_var.get(),r,self.Page_var.get()
                                                                                ))
            con.commit()
            self.fetch_data()
            self.Remaining_var.set(r)
            #self.Clear()
            con.close()
            messagebox.showinfo("Success","Record has been Updated.")

    def Create_File(self):
        
        if self.Name_var.get()=="":
            messagebox.showerror("Error","Insert Proper Details")
        else:
            f=open("C_Record/"+str(self.Name_var.get())+".txt","w")
            f.write(str(self.Date1.get())+"\t\t\t"+str(self.Total_var.get())+"\t\t\t"+str(self.Paid_var.get())+"\t\t\t\t"+str(r))
            f.close()

    def Append(self):
        if self.Name_var.get()=="":
            messagebox.showerror("Error","Insert Proper Details")
        else:
            f=open("C_Record/"+str(self.Name_var.get())+".txt","a+")
            f.seek(0)
            data=f.read(100)
            if len(data)>0:
                f.write("\n")
            f.write(str(self.Date1.get())+"\t\t\t"+str(self.Total_var.get())+"\t\t\t"+str(self.Paid_var.get())+"\t\t\t\t"+str(r))
            f.close()

    def Show_List(self):
        check=os.path.exists("C_Record/"+str(self.search_txt.get())+".txt")
        if check==1:
            files=os.listdir("C_Record/")
            self.file_list.delete(0,END)
            for file in files:
                if file == str(self.search_txt.get()+".txt"):
                    self.file_list.insert(END,file)
        else:
            messagebox.showerror("Error","No transaction record found.")

    def Welcome_Bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END,f" Name: {self.search_txt.get()}")
        self.textarea.insert(END,'\n=============================================================================================')
        self.textarea.insert(END,'\n Date\t\t\tTotal Amount\t\t\tPaid Amount\t\t\tRemaining Amount')
        self.textarea.insert(END,'\n=============================================================================================')

    
    def Print_Data(self,event):
        self.Welcome_Bill()
        get_cursor=self.file_list.curselection()
        f1=open("C_Record/"+self.file_list.get(get_cursor))
        data=[]
        x=f1.readlines()
        # self.textarea.delete('1.0',END)
        for line in x:
            self.textarea.insert(END,line)

    def makeDir(self):
        os.mkdir('C_Record')

root=Tk()
ob=MomShop(root)
root.mainloop()