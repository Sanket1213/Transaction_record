from tkinter import *
from tkinter import ttk
import pymysql
import tkinter.messagebox
import random
from datetime import datetime
import time

class Customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1350x700+0+0")  

        abc=Frame(self.root, relief=RIDGE)#, bg="crimson")
        abc.grid()

        #===========================================
        Firstname=StringVar()
        Surname=StringVar()
        Mobile=StringVar()
        Address=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        Discount=StringVar()
        #===========================================
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        #===========================================

        P_Shirt=StringVar()
        P_Pant=StringVar()
        P_Kurta=StringVar()
        P_Pyjama=StringVar()
        P_Safari=StringVar()
        P_Suit=StringVar()
        
        P_Shirt.set("0")
        P_Pant.set("0")
        P_Kurta.set("0")
        P_Pyjama.set("0")
        P_Safari.set("0")
        P_Suit.set("0")

        #===========================================
        abc1=Frame(abc,bd=7, width=1350, height=100, padx=10, relief=RIDGE)   #title frame
        abc1.grid(row=0,column=0,columnspan=4, sticky=W)
        abc2=Frame(abc,bd=7, width=450, height=580, padx=10, relief=RIDGE)    #costumer details
        abc2.grid(row=1,column=0, sticky=W)
        abc3=Frame(abc,bd=7, width=450, height=580, padx=10, relief=RIDGE)    #product details
        abc3.grid(row=1,column=1, sticky=W)

        abc4=Frame(abc, width=450, height=580, relief=RIDGE)    #bill details
        abc4.grid(row=1,column=2, sticky=W)
        
        abc5=Frame(abc4,bd=7, width=450, height=428, padx=10, relief=RIDGE)    #button details
        abc5.grid(row=0,column=0, sticky=W)
        abc6=Frame(abc4,bd=7, width=450, height=180, padx=10, relief=RIDGE)   
        abc6.grid(row=1,column=0,columnspan=4, sticky=W)

        Date1= StringVar()
        Time1= StringVar()
        Date1.set(time.strftime("%d/%m/%y"))
        Time1.set(time.strftime("%H:%M:%S"))

        self.lblTitle= Label(abc1, textvariable=Date1, font=('arial',20,'bold'),pady=9).grid(row=0,column=0)
        self.lblTitle= Label(abc1, text="\t\t\t Shop name    \t\t", font=('arial',30,'bold'),pady=9,justify=CENTER).grid(row=0,column=1)
        self.lblTitle= Label(abc1, textvariable=Time1, font=('arial',20,'bold'),pady=9).grid(row=0,column=2)
        #==========================================================

        def iExit():
            iExit=tkinter.messagebox.askyesno("Customer Billing System","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.txtReceipt.delete("1.0", END)
            P_Shirt.set("0")
            P_Pant.set("0")
            P_Kurta.set("0")
            P_Pyjama.set("0")
            P_Safari.set("0")
            P_Suit.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)

            self.txtShirt.configure(state=DISABLED)
            self.txtPant.configure(state=DISABLED)
            self.txtKurta.configure(state=DISABLED)
            self.txtPyjama.configure(state=DISABLED)
            self.txtSafari.configure(state=DISABLED)
            self.txtSuit.configure(state=DISABLED)

        def chkShirt():
            if(var1.get() == 1):
                self.txtShirt.configure(state=NORMAL)
                self.txtShirt.focus()
                self.txtShirt.delete('0',END)
                P_Shirt.set("")
            else:
                self.txtShirt.configure(state=DISABLED)
                self.txtShirt.set("0")
                

        def chkPant():
            if(var2.get() == 1):
                self.txtPant.configure(state=NORMAL)
                self.txtPant.focus()
                self.txtPant.delete('0',END)
                P_Pant.set("")
            elif(var2.get() == 0):
                self.txtPant.configure(state=DISABLED)
                self.txtPant.set("0")
                

        def chkKurta():
            if(var3.get() == 1):
                self.txtKurta.configure(state=NORMAL)
                self.txtKurta.focus()
                self.txtKurta.delete('0',END)
                P_Kurta.set("")
            elif(var3.get() == 0):
                self.txtKurta.configure(state=DISABLED)
                self.txtKurta.set("0")

        def chkPyjama():
            if(var4.get() == 1):
                self.txtPyjama.configure(state=NORMAL)
                self.txtPyjama.focus()
                self.txtPyjama.delete('0',END)
                P_Pyjama.set("")
            elif(var4.get() == 0):
                self.txtPyjama.configure(state=DISABLED)
                self.txtPyjama.set("0")

        def chkSafari():
            if(var5.get() == 1):
                self.txtSafari.configure(state=NORMAL)
                self.txtSafari.focus()
                self.txtSafari.delete('0',END)
                P_Safari.set("")
            elif(var5.get() == 0):
                self.txtSafari.configure(state=DISABLED)
                self.txtSafari.set("0")

        def chkSuit():
            if(var6.get() == 1):
                self.txtSuit.configure(state=NORMAL)
                self.txtSuit.focus()
                self.txtSuit.delete('0',END)
                P_Suit.set("")
            elif(var6.get() == 0):
                self.txtSuit.configure(state=DISABLED)
                self.txtSuit.set("0")
                
        #==========================================================

        c_title=Label(abc2,text="Customer Details", font=("times new roman",20,"bold"), fg="black")
        c_title.grid(row=0, columnspan=2, pady=20)

        lbl_name=Label(abc2,text="First Name:", font=("times new roman",20,"bold"), fg="black")
        lbl_name.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        txt_name=Entry(abc2, font=("times new roman",15,"bold"), bd=2, relief=GROOVE, textvariable=Firstname)
        txt_name.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_sur_name=Label(abc2,text="Last Name:", font=("times new roman",20,"bold"), fg="black")
        lbl_sur_name.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        txt_sur_name=Entry(abc2, font=("times new roman",15,"bold"), bd=2, relief=GROOVE, textvariable=Surname)
        txt_sur_name.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_contact=Label(abc2,text="Contact:", font=("times new roman",20,"bold"), fg="black")
        lbl_contact.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        txt_contact=Entry(abc2, font=("times new roman",15,"bold"), bd=2, relief=GROOVE, textvariable=Mobile)
        txt_contact.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        lbl_address=Label(abc2,text="Address:", font=("times new roman",20,"bold"), fg="black")
        lbl_address.grid(row=4, column=0, pady=5, padx=10, sticky="w")
        txt_address=Entry(abc2, font=("times new roman",15,"bold"), bd=2, relief=GROOVE, textvariable=Address)
        txt_address.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        lbl_name=Label(abc2,text="", font=("times new roman",20,"bold"), fg="black")
        lbl_name.grid(row=5, column=0, pady=5, padx=10, sticky="w")
        lbl_name=Label(abc2,text="", font=("times new roman",20,"bold"), fg="black")
        lbl_name.grid(row=6, column=0, pady=5, padx=10, sticky="w")
        lbl_name=Label(abc2,text="", font=("times new roman",20,"bold"), fg="black")
        lbl_name.grid(row=7, column=0, pady=5, padx=10, sticky="w")
        lbl_name=Label(abc2,text="", font=("times new roman",20,"bold"), fg="black")
        lbl_name.grid(row=8, column=0, pady=5, padx=10, sticky="w")
        lbl_name=Label(abc2,text="", font=("times new roman",20,"bold"), fg="black")
        lbl_name.grid(row=9, column=0, pady=5, padx=10, sticky="w")
        lbl_name=Label(abc2,text="", font=("times new roman",20,"bold"), fg="black")
        lbl_name.grid(row=10, column=0, pady=15, padx=10, sticky="w")
        #==========================================================
        self.txtReceipt = Text(abc5, height=26, width=56, bd=10, font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0)

        

        
        #===========================================

        self.Shirt=Checkbutton(abc3, text="Shirt:", variable=var1, onvalue=1, offvalue=0, font=("times new roman",20,"bold"), command=chkShirt).grid(row=1, sticky=W)
        self.txtShirt=Entry(abc3, font=("times new roman",20,"bold"), width=18, justify='left', state=DISABLED, textvariable=P_Shirt)
        self.txtShirt.grid(row=1, column=1)

        self.Pant=Checkbutton(abc3, text="Pant:", variable=var2, onvalue=1, offvalue=0, font=("times new roman",20,"bold"), command=chkPant).grid(row=2, sticky=W)
        self.txtPant=Entry(abc3, font=("times new roman",20,"bold"), width=18, justify='left', state=DISABLED, textvariable=P_Pant)
        self.txtPant.grid(row=2, column=1)

        self.Kurta=Checkbutton(abc3, text="Kurta:", variable=var3, onvalue=1, offvalue=0, font=("times new roman",20,"bold"), command=chkKurta).grid(row=3, sticky=W)
        self.txtKurta=Entry(abc3, font=("times new roman",20,"bold"), width=18, justify='left', state=DISABLED, textvariable=P_Kurta)
        self.txtKurta.grid(row=3, column=1)

        self.Pyjama=Checkbutton(abc3, text="Pyjama:", variable=var4, onvalue=1, offvalue=0, font=("times new roman",20,"bold"), command=chkPyjama).grid(row=4, sticky=W)
        self.txtPyjama=Entry(abc3, font=("times new roman",20,"bold"), width=18, justify='left', state=DISABLED, textvariable=P_Pyjama)
        self.txtPyjama.grid(row=4, column=1)

        self.Safari=Checkbutton(abc3, text="Safari:", variable=var5, onvalue=1, offvalue=0, font=("times new roman",20,"bold"), command=chkSafari).grid(row=5, sticky=W)
        self.txtSafari=Entry(abc3, font=("times new roman",20,"bold"), width=18, justify='left', state=DISABLED, textvariable=P_Safari)
        self.txtSafari.grid(row=5, column=1)

        self.Suit=Checkbutton(abc3, text="Suit:", variable=var6, onvalue=1, offvalue=0, font=("times new roman",20,"bold"), command=chkSuit).grid(row=6, sticky=W)
        self.txtSuit=Entry(abc3, font=("times new roman",20,"bold"), width=18, justify='left', state=DISABLED, textvariable=P_Suit)
        self.txtSuit.grid(row=6, column=1)

        self.Space=Label(abc3, text=" ", font=("times new roman",20,"bold")).grid(row=7, sticky=W)
        

        self.lblspace=Label(abc3,text="Tax, Sum and Discount",font=('arial',18,'bold'),pady=3, bd=5, bg="light grey", width=26, justify=CENTER).grid(row=8, column=0, columnspan=4)

        #=====

        self.lbl_Discount=Label(abc3,text="Discount:", font=("times new roman",20,"bold"), fg="black")
        self.lbl_Discount.grid(row=9, column=0, pady=5, padx=10, sticky="w")
        self.txt_Discount=Entry(abc3, font=("times new roman",15,"bold"), bd=2, relief=GROOVE, textvariable=Discount)
        self.txt_Discount.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        self.lbl_SubTotal=Label(abc3,text="Sub Total:", font=("times new roman",20,"bold"), fg="black")
        self.lbl_SubTotal.grid(row=10, column=0, pady=5, padx=10, sticky="w")
        self.txt_SubTotal=Entry(abc3, font=("times new roman",15,"bold"), bd=2, relief=GROOVE, textvariable=SubTotal)
        self.txt_SubTotal.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        self.lbl_TotalCost=Label(abc3,text="Total Cost:", font=("times new roman",20,"bold"), fg="black")
        self.lbl_TotalCost.grid(row=11, column=0, pady=5, padx=10, sticky="w")
        self.txt_TotalCost=Entry(abc3, font=("times new roman",15,"bold"), bd=2, relief=GROOVE, textvariable=TotalCost)
        self.txt_TotalCost.grid(row=11, column=1, pady=5, padx=10, sticky="w")

        self.Shirt=Label(abc3, text=" ", font=("times new roman",21,"bold")).grid(row=12, sticky=W)
        self.Shirt=Label(abc3, text=" ", font=("times new roman",21,"bold")).grid(row=13, sticky=W)

        #==========================================================

        

        def subTotal(self):
            iShirt=float(P_Shirt.get())
            iPant=float(P_Pant.get())
            iKurta=float(P_Kurta.get())
            iPyjama=float(P_Pyjama.get())
            iSafari=float(P_Safari.get())
            iSuit=float(P_Suit.get())

            sub=iShirt+iPant+iKurta+iPyjama+iSafari+iSuit
            SubTotal.set(sub)

            dis_val=float(Discount.get())
            per_dis=sub*dis_val*0.01
            T_dis=int(sub-per_dis)
            TotalCost.set(T_dis)

            

            

        #==========================================================

        

        #==========================================================
        self.btnTotal=Button(abc6, padx=14, pady=7, bd=2, font=('arial',20,'bold'),width=6,height=1,bg="light grey",text="Total", command=subTotal).grid(row=0,column=0)
        self.btnReset=Button(abc6, padx=14, pady=7, bd=2, font=('arial',20,'bold'),width=6,height=1,bg="light grey",text="Reset", command=Reset).grid(row=0,column=1)
        self.btnExit=Button(abc6, padx=14, pady=7, bd=2, font=('arial',20,'bold'),width=6,height=1,bg="light grey",text="Exit", command=iExit).grid(row=0,column=2)
        self.btnTotal=Button(abc6, padx=14, pady=7, bd=2, font=('arial',20,'bold'),width=20,height=1,bg="light grey",text="Print Bill").grid(row=1,column=0,columnspan=3)
        #==========================================================
        self.wellcomeBill()
        def wellcomeBill(self):
            #self.textReceipt('1.0', END)
            self.textReceipt.insert(END,"Well-Come")
        

        

if __name__=='__main__':
    root=Tk()
    application=Customer(root)
    root.mainloop()