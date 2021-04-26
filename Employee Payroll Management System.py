from tkinter import*
from tkinter import messagebox,ttk
import pymysql
import time
import os
import tempfile
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="grey")
        title=Label(self.root,text="Employee Payroll Management System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All Employee's",command=self.employee_frame,font=("times new roman",13),bg="gray",fg="white").place(x=1100,y=10,height=30,width=120)
        btn_logout=Button(self.root,text="LOG OUT",command=self.root.destroy,font=("times new roman",13),bg="gray",fg="white").place(x=1230,y=10,height=30,width=100)
        

        #---------------Frame1-----------------------------
        #---------------variables------------------------
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar()
        self.var_contact=StringVar()
        self.var_experience=StringVar()

        
        frame1=Frame(self.root,bd=3,relief=RIDGE,bg="orange")
        frame1.place(x=10,y=70,width=750,height=620)
        title2=Label(frame1,text="Employee Details",font=("times new roman",20),bg="black",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)


        lb1_code=Label(frame1,text="Employee code:",font=("times new roman",20),bg="orange",fg="black").place(x=10,y=70)
        self.txt_code=Entry(frame1,font=("times new roman",15),textvariable=self.var_emp_code,bg="lightyellow",fg="black")
        self.txt_code.place(x=220,y=75)

        lb1_search=Button(frame1,text="Search",command=self.search,font=("times new roman",20),bg="gray",fg="black").place(x=430,y=73,height=30)
        #-----row1------   
        lb1_designation=Label(frame1,text="Designation:",font=("times new roman",20),bg="orange",fg="black").place(x=10,y=120)
        txt_designation=Entry(frame1,font=("times new roman",15),textvariable=self.var_designation,bg="lightyellow",fg="black").place(x=160,y=130)

        lb1_dob=Label(frame1,text="D.O.B",font=("times new roman",20),bg="orange",fg="black").place(x=370,y=125)
        txt_dob=Entry(frame1,font=("times new roman",15),textvariable=self.var_dob,bg="lightyellow",fg="black").place(x=510,y=130)

        #-----row2------
        lb1_name=Label(frame1,text="Name:",font=("times new roman",20),bg="orange",fg="black").place(x=10,y=170)
        txt_name=Entry(frame1,font=("times new roman",15),textvariable=self.var_name,bg="lightyellow",fg="black").place(x=160,y=180)

        lb1_doj=Label(frame1,text="D.O.J",font=("times new roman",20),bg="orange",fg="black").place(x=370,y=175)
        txt_doj=Entry(frame1,font=("times new roman",15),textvariable=self.var_doj,bg="lightyellow",fg="black").place(x=510,y=180)

        #-----row3------
        lb1_age=Label(frame1,text="Age:",font=("times new roman",20),bg="orange",fg="black").place(x=10,y=220)
        txt_age=Entry(frame1,font=("times new roman",15),textvariable=self.var_age,bg="lightyellow",fg="black").place(x=160,y=230)

        lb1_experience=Label(frame1,text="Experience:",font=("times new roman",20),bg="orange",fg="black").place(x=370,y=225)
        txt_experience=Entry(frame1,font=("times new roman",15),textvariable=self.var_experience,bg="lightyellow",fg="black").place(x=510,y=230)

        #-----row4------
        self.radio=StringVar()
        self.radio.set("Gender")
        lb1_gender=Label(frame1,text="Gender:",font=("times new roman",20),bg="orange",fg="black").place(x=10,y=270)
        r_gender=OptionMenu(frame1,self.radio,"Male","Female","Other")
        r_gender.config(width=15,font=("times new roman",15))
        r_gender.place(x=160,y=280)

        lb1_Proof=Label(frame1,text="Proof ID:",font=("times new roman",20),bg="orange",fg="black").place(x=370,y=275)
        txt_proof=Entry(frame1,font=("times new roman",15),textvariable=self.var_proof_id,bg="lightyellow",fg="black").place(x=510,y=280)

        #-----row5------
        lb1_Email=Label(frame1,text="Email:",font=("times new roman",20),bg="orange",fg="black").place(x=10,y=320)
        txt_Email=Entry(frame1,font=("times new roman",15),textvariable=self.var_email,bg="lightyellow",fg="black").place(x=160,y=330)

        lb1_Contact=Label(frame1,text="Contact No:",font=("times new roman",20),bg="orange",fg="black").place(x=370,y=325)
        txt_Contact=Entry(frame1,font=("times new roman",15),textvariable=self.var_contact,bg="lightyellow",fg="black").place(x=510,y=330)


        #-----row6------
        lb1_hired=Label(frame1,text="Hired Location",font=("times new roman",17),bg="orange",fg="black").place(x=10,y=375)
        txt_hired=Entry(frame1,font=("times new roman",15),textvariable=self.var_hr_location,bg="lightyellow",fg="black").place(x=160,y=380)

        lb1_status=Label(frame1,text="Status:",font=("times new roman",20),bg="orange",fg="black").place(x=370,y=375)

        self.clicked=StringVar()
        self.clicked.set("Employee Status")

        Ostatus=OptionMenu(frame1,self.clicked,"Active","Permanent","trainee")
        Ostatus.config(width=15,font=("times new roman",15))
        Ostatus.place(x=510,y=380)


        #-----row7------
        lb1_Address=Label(frame1,text="Address",font=("times new roman",17),bg="orange",fg="black").place(x=10,y=420)
        self.txt_Address=Text(frame1,font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_Address.place(x=160,y=430,width=555,height=170)


        #---------------Frame2-----------------------------
        #---------------variables------------------------
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_tdays=StringVar()
        self.var_salary=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_net_salary=StringVar()
        self.var_convence=StringVar()
        
        frame2=Frame(self.root,bd=3,relief=RIDGE,bg="cyan")
        frame2.place(x=770,y=70,width=580,height=300)
        title3=Label(frame2,text="Employee Salary Details",font=("times new roman",20),bg="black",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)


        lb1_month=Label(frame2,text="Month",font=("times new roman",15),bg="cyan",fg="black").place(x=10,y=60)
        txt_month=Entry(frame2,font=("times new roman",15),textvariable=self.var_month,bg="lightyellow",fg="black").place(x=80,y=60,width=100)
        
        lb1_year=Label(frame2,text="Year",font=("times new roman",15),bg="cyan",fg="black").place(x=190,y=60)
        txt_year=Entry(frame2,font=("times new roman",15),textvariable=self.var_year,bg="lightyellow",fg="black").place(x=240,y=60,width=100)

        lb1_Salary=Label(frame2,text="Salary",font=("times new roman",15),bg="cyan",fg="black").place(x=350,y=60)
        txt_Salary=Entry(frame2,font=("times new roman",15),textvariable=self.var_salary,bg="lightyellow",fg="black").place(x=410,y=60,width=100)
        #-----row1------   
        lb1_days=Label(frame2,text="Total Days",font=("times new roman",18),bg="cyan",fg="black").place(x=10,y=110)
        txt_days=Entry(frame2,font=("times new roman",15),textvariable=self.var_tdays,bg="lightyellow",fg="black").place(x=140,y=120,width=100)

        lb1_absent=Label(frame2,text="Absent",font=("times new roman",18),bg="cyan",fg="black").place(x=270,y=115)
        txt_absent=Entry(frame2,font=("times new roman",15),textvariable=self.var_absent,bg="lightyellow",fg="black").place(x=390,y=120,width=100)

        #-----row2------
        lb1_medical=Label(frame2,text="Medical",font=("times new roman",18),bg="cyan",fg="black").place(x=10,y=140)
        txt_medical=Entry(frame2,font=("times new roman",15),textvariable=self.var_medical,bg="lightyellow",fg="black").place(x=140,y=150,width=100)

        lb1_pf=Label(frame2,text="PF",font=("times new roman",18),bg="cyan",fg="black").place(x=270,y=145)
        txt_pf=Entry(frame2,font=("times new roman",15),textvariable=self.var_pf,bg="lightyellow",fg="black").place(x=390,y=150,width=100)

        #-----row3------
        lb1_convence=Label(frame2,text="Convence",font=("times new roman",18),bg="cyan",fg="black").place(x=10,y=170)
        txt_convence=Entry(frame2,font=("times new roman",15),textvariable=self.var_convence,bg="lightyellow",fg="black").place(x=140,y=180,width=100)

        lb1_ns=Label(frame2,text="Net Salary",font=("times new roman",18),bg="cyan",fg="black").place(x=270,y=175)
        txt_ns=Entry(frame2,font=("times new roman",15),textvariable=self.var_net_salary,state='readonly',bg="lightyellow",fg="black").place(x=390,y=180,width=100)

        
        #-----row4------
        lb1_cals=Button(frame2,text="Calculate",command=self.calculate,font=("times new roman",18),bg="orange",fg="black").place(x=160,y=225,height=30,width=100)
        self.lb1_save=Button(frame2,text="Save",command=self.add,font=("times new roman",18),bg="green",fg="white")
        self.lb1_save.place(x=270,y=225,height=30,width=100)
        lb1_clear=Button(frame2,text="Clear",command=self.clear,font=("times new roman",18),bg="gray",fg="black").place(x=380,y=225,height=30,width=100)
        
        self.lb1_update=Button(frame2,text="Update",state=DISABLED,command=self.update,font=("times new roman",18),bg="blue",fg="white")
        self.lb1_update.place(x=160,y=260,height=30,width=160)
        self.lb1_delete=Button(frame2,text="Delete",state=DISABLED,command=self.delete,font=("times new roman",18),bg="brown",fg="white")
        self.lb1_delete.place(x=325,y=260,height=30,width=155)
        
        #---------------Frame3-----------------------------
        frame3=Frame(self.root,bd=3,relief=RIDGE,bg="purple")
        frame3.place(x=770,y=380,width=580,height=310)


        #----------------calculator frame----
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)


        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        def clear():
            self.var_txt.set('')
            self.var_operator=''




        cal_frame=Frame(frame3,bg="white",bd=2,relief=RIDGE)
        cal_frame.place(x=2,y=2,width=247,height=300)
        txt_result=Entry(cal_frame,bg="lightyellow",textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=50)

        #-----------row1------------
        btn_7=Button(cal_frame,text='7',command=lambda:btn_click(7),font=("times new roman",20,"bold")).place(x=0,y=52,w=60,h=60)
        btn_8=Button(cal_frame,text='8',command=lambda:btn_click(8),font=("times new roman",20,"bold")).place(x=61,y=52,w=60,h=60)
        btn_9=Button(cal_frame,text='9',command=lambda:btn_click(9),font=("times new roman",20,"bold")).place(x=122,y=52,w=60,h=60)
        btn_div=Button(cal_frame,text='/',command=lambda:btn_click('/'),font=("times new roman",20,"bold")).place(x=183,y=52,w=60,h=60)

        #-----------row2------------
        btn_4=Button(cal_frame,text='4',command=lambda:btn_click(4),font=("times new roman",20,"bold")).place(x=0,y=112,w=60,h=60)
        btn_5=Button(cal_frame,text='5',command=lambda:btn_click(5),font=("times new roman",20,"bold")).place(x=61,y=112,w=60,h=60)
        btn_6=Button(cal_frame,text='6',command=lambda:btn_click(6),font=("times new roman",20,"bold")).place(x=122,y=112,w=60,h=60)
        btn_mul=Button(cal_frame,text='*',command=lambda:btn_click('*'),font=("times new roman",20,"bold")).place(x=183,y=112,w=60,h=60)


        #-----------row3------------
        btn_1=Button(cal_frame,text='1',command=lambda:btn_click(1),font=("times new roman",20,"bold")).place(x=0,y=172,w=60,h=60)
        btn_2=Button(cal_frame,text='2',command=lambda:btn_click(2),font=("times new roman",20,"bold")).place(x=61,y=172,w=60,h=60)
        btn_3=Button(cal_frame,text='3',command=lambda:btn_click(3),font=("times new roman",20,"bold")).place(x=122,y=172,w=60,h=60)
        btn_sub=Button(cal_frame,text='-',command=lambda:btn_click('-'),font=("times new roman",20,"bold")).place(x=183,y=172,w=60,h=60)


        #-----------row4------------
        btn_0=Button(cal_frame,text='0',command=lambda:btn_click(0),font=("times new roman",20,"bold")).place(x=0,y=233,w=60,h=60)
        btn_C=Button(cal_frame,text='C',command=clear,font=("times new roman",20,"bold")).place(x=61,y=233,w=60,h=60)
        btn_add=Button(cal_frame,text='+',command=lambda:btn_click('+'),font=("times new roman",20,"bold")).place(x=122,y=233,w=60,h=60)
        btn_equal=Button(cal_frame,text='=',command=result,font=("times new roman",20,"bold")).place(x=183,y=233,w=60,h=60)

        #----Salary frame-------
        Salary_frame=Frame(frame3,bg="white",bd=2,relief=RIDGE)
        Salary_frame.place(x=251,y=2,width=320,height=300)
        title_sal=Label(Salary_frame,text="Salary Recipt",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        Salary_frame2=Frame(Salary_frame,bg="white",bd=2,relief=RIDGE)
        Salary_frame2.place(x=0,y=30,relwidth=1,height=230)
        self.sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
-----------------------------------------------
 Employee ID\t\t:  
 Salary of\t\t:  Mon-YYYY
 Generated On\t\t:  DD-Mon-YYYY
-----------------------------------------------
 Total Days\t\t:  DD
 Total Prersent\t\t:  DD
 Total Absent\t\t:  DD
 Convence\t\t:  Rs.----
 Medical\t\t:  Rs.----
 PF\t\t:  Rs.----
 Gross Payment\t\t:  Rs.-------
 Net Salary\t\t:  Rs.------
-----------------------------------------------
 This is computer generated slip,not
 required any signature
'''



        scroll_y=Scrollbar(Salary_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt=Text(Salary_frame2,font=("times new roman",13),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        self.txt_salary_recipt.insert(END,self.sample)
        self.lb1_print=Button(Salary_frame,text="Print",state=DISABLED,command=self.print,font=("times new roman",20),bg="lime",fg="black")
        self.lb1_print.place(x=120,y=262,height=30)


        self.check_connection()


    
   #----------------all function start here--------
    def search(self):
        try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                # print(row)
                if (row==None):
                    messagebox.showerror("Error","Invalid Employee ID,please with another Employee ID",parent=self.root)
                else:
                    print(row)
                    self.var_emp_code.set(row[0])
                    self.var_designation.set(row[1])
                    self.var_name.set(row[2])
                    self.var_age.set(row[3])
                    self.var_email.set(row[4])
                    self.var_hr_location.set(row[5])
                    self.var_dob.set(row[6])
                    self.var_doj.set(row[7])
                    self.var_proof_id.set(row[8])
                    self.var_contact.set(row[9])
                    self.var_experience.set(row[10])
                    self.radio.set(row[11])
                    self.clicked.set(row[12])
                    self.txt_Address.delete('1.0',END)
                    self.txt_Address.insert(END,row[13])
                    self.var_month.set(row[14])
                    self.var_year.set(row[15])
                    self.var_salary.set(row[16])
                    self.var_tdays.set(row[17])
                    self.var_absent.set(row[18])
                    self.var_medical.set(row[19])
                    self.var_pf.set(row[20])
                    self.var_convence.set(row[21])
                    self.var_net_salary.set(row[22])
                    file=open('C:/Users/Sumit/Desktop/Salary_reciept/'+str(row[23]),'r')
                    self.txt_salary_recipt.delete('1.0',END)
                    for i in file:
                        self.txt_salary_recipt.insert(END,i)
                    file.close()
                    self.lb1_save.config(state=DISABLED)
                    self.lb1_update.config(state=NORMAL)
                    self.lb1_delete.config(state=NORMAL)
                    self.txt_code.config(state='readonly')
                    self.lb1_print.config(state=NORMAL)

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')


    def clear(self):
        self.lb1_save.config(state=NORMAL)
        self.lb1_update.config(state=DISABLED)
        self.lb1_delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)
        self.lb1_print.config(state=DISABLED)
        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_proof_id.set('')
        self.var_contact.set('')
        self.var_experience.set('')
        self.radio.set('')
        self.clicked.set('')
        self.txt_Address.delete('1.0',END)
        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_tdays.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
        self.txt_salary_recipt.delete('1.0',END)
        self.txt_salary_recipt.insert(END,self.sample)
                    
                                                                                                                                        

    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror('Error',"Employee ID must be required")
        else:
            try:
                    con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                    cur=con.cursor()
                    cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                    row=cur.fetchone()
                    # print(row)
                    if (row==None):
                        messagebox.showerror("Error","Invalid Employee ID,please with another Employee ID",parent=self.root)
                    else:
                        op=messagebox.askyesno("confirm","Do you want to delete")
                        if op==True:
                            cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
                            con.commit()
                            con.close()
                            messagebox.showinfo("Delete","Employee Recorded Deleted Succesfully",parent=self.root)
                            self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')
     
     




    def add(self):
        if self.var_emp_code.get()==''or self.var_net_salary.get()==''or self.var_name.get()=='':
            messagebox.showerror('error',"employee details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                # print(row)
                if (row!=None):
                    messagebox.showerror("Error","This Employee ID has Already in our record,try again another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (self.var_emp_code.get(),
                                     self.var_designation.get(),
                 self.var_name.get(),
                 self.var_age.get(),
                 self.var_email.get(),
                 self.var_hr_location.get(),
                 self.var_dob.get(),
                 self.var_doj.get(),
                 self.var_proof_id.get(),
                 self.var_contact.get(),
                 self.var_experience.get(),
                 self.radio.get(),
                 self.clicked.get(),
                 self.txt_Address.get('1.0',END),
                 self.var_month.get(),
                 self.var_year.get(),
                 self.var_salary.get(),
                 self.var_tdays.get(),
                 self.var_absent.get(),
                 self.var_medical.get(),
                 self.var_pf.get(),
                 self.var_convence.get(),
                 self.var_net_salary.get(),
                 self.var_emp_code.get()+".txt"
                ))
                con.commit()
                con.close()
                file=open('C:/Users/Sumit/Desktop/Salary_reciept/'+str(self.var_emp_code.get())+".txt",'w')
                file.write(self.txt_salary_recipt.get('1.0',END))
                file.close()
                messagebox.showinfo("Success",'Record Added Succesfully')
                self.lb1_print.config(state=NORMAL)
            except Exception as ex:
                    messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def update(self):
        if self.var_emp_code.get()==''or self.var_net_salary.get()==''or self.var_name.get()=='':
            messagebox.showerror('error',"employee details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                # print(row)
                if (row==None):
                    messagebox.showerror("Error","This Employee ID is invalid,try again with valid Employee ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`email`=%s,`hr_location`=%s,`dob`=%s,`doj`=%s,`proof_id`=%s,`contact`=%s,`experience`=%s,`gender`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`t_days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `e_id`=%s",
                                    (self.var_designation.get(),
                 self.var_name.get(),
                 self.var_age.get(),
                 self.var_email.get(),
                 self.var_hr_location.get(),
                 self.var_dob.get(),
                 self.var_doj.get(),
                 self.var_proof_id.get(),
                 self.var_contact.get(),
                 self.var_experience.get(),
                 self.radio.get(),
                 self.clicked.get(),
                 self.txt_Address.get('1.0',END),
                 self.var_month.get(),
                 self.var_year.get(),
                 self.var_salary.get(),
                 self.var_tdays.get(),
                 self.var_absent.get(),
                 self.var_medical.get(),
                 self.var_pf.get(),
                 self.var_convence.get(),
                 self.var_net_salary.get(),
                 self.var_emp_code.get()+".txt",
                 self.var_emp_code.get()
                                     
                
                ))
                con.commit()
                con.close()
                file=open('C:/Users/Sumit/Desktop/Salary_reciept/'+str(self.var_emp_code.get())+".txt",'w')
                file.write(self.txt_salary_recipt.get('1.0',END))
                file.close()
                messagebox.showinfo("Success",'Record Updated Succesfully')
            except Exception as ex:
                    messagebox.showerror("Error",f'Error due to:{str(ex)}')



    def calculate(self):
        if (self.var_month.get()==''or self.var_year.get()==''or self.var_tdays.get()==''or self.var_salary.get()==''or self.var_absent.get()==''or self.var_medical.get()==''or self.var_pf.get()==''or self.var_net_salary=='' or self.var_convence.get()==''):
            messagebox.showerror('Error','ALL fields are required')
        else:
            per_day=int(self.var_salary.get())/int(self.var_tdays.get())
            work_day=int(self.var_tdays.get())-int(self.var_absent.get())
            sal=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal-deduct+addition
            self.var_net_salary.set(str(round(net_sal,2)))
            #---------Update the recipt----------
            new_sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
-----------------------------------------------
 Employee ID\t\t:  {self.var_emp_code.get()}
 Salary of\t\t:  {self.var_month.get()}-{self.var_year.get()}
 Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
-----------------------------------------------
 Total Days\t\t:  {self.var_tdays.get()}
 Total Prersent\t\t:  {str(int(self.var_tdays.get())-int(self.var_absent.get()))}
 Total Absent\t\t:  {self.var_absent.get()}
 Convence\t\t:  Rs.{self.var_convence.get()}
 Medical\t\t:  Rs.{self.var_medical.get()}
 PF\t\t:  Rs.{self.var_pf.get()}
 Gross Payment\t\t:  Rs.{self.var_salary.get()}
 Net Salary\t\t:  Rs.{self.var_net_salary.get()}
-----------------------------------------------
 This is computer generated slip,not
 required any signature
'''
            self.txt_salary_recipt.delete('1.0',END)
            self.txt_salary_recipt.insert(END,new_sample)
        
       




    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')



    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll Management System")
        self.root2.geometry("900x500+120+100")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Payroll Management System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()


        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)

        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'email', 'hr_location', 'dob', 'doj', 'proof_id', 'contact', 'experience', 'gender', 'status', 'address', 'month', 'year', 'basic_salary', 't_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='EmpID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='HR LOC')
        self.employee_tree.heading('dob',text='D.O.B')
        self.employee_tree.heading('doj',text='D.O.J')
        self.employee_tree.heading('proof_id',text='Proof')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Salary')
        self.employee_tree.heading('t_days',text='Days')
        self.employee_tree.heading('absent_days',text='Absent')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Net_salary')
        self.employee_tree.heading('salary_receipt',text='Salary Receipt')
        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('t_days',width=100)
        self.employee_tree.column('absent_days',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_receipt',width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()



        self.root2.mainloop()


    def print(self):
        file=tempfile.mktemp(".txt")
        open(file,'w').write(self.txt_salary_recipt.get('1.0',END))
        os.startfile(file,'print')


root=Tk()
obj=EmployeeSystem(root)
root.mainloop() 
