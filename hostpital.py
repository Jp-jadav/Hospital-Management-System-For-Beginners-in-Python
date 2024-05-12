from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref = StringVar()
        self.Dose=StringVar()
        self.NumbersOfTablets=StringVar()
        self.Lote=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nshNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.addess=StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman",30,"bold"))
        lbltitle.pack(side=TOP, fill=X)

        # data fram
        Datafram = Frame(self.root,bd=20,relief=RIDGE)
        Datafram.place(x=0,y=90,width=1370,height=390)

        DataframLeft= LabelFrame(Datafram,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        DataframLeft.place(x=0,y=5,width=950,height=350)

        DataframRight= LabelFrame(Datafram,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        DataframRight.place(x=960,y=5,width=360,height=350)

        #buttons fram
        Buttonfram = Frame(self.root,bd=20,relief=RIDGE)
        Buttonfram.place(x=0,y=470,width=1370,height=70)

        #Details fram
        Detailsfram = Frame(self.root,bd=20,relief=RIDGE)
        Detailsfram.place(x=0,y=540,width=1370,height=150)

        #DataFramLeft
        lblNameTablet=Label(DataframLeft,text="Names OF Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframLeft,textvariable=self.Nameoftablets,state="readonly",font=("times new roman",12,"bold"),width=30)
        comNametablet["values"] = ("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframLeft,text="Refence No:",font=("arial",12,"bold"),padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref= Entry(DataframLeft,textvariable=self.ref,font=("arial",13,"bold"),width=29)
        txtref.grid(row=1,column=1)

        lblDos=Label(DataframLeft,text="Dose:",font=("arial",12,"bold"),padx=2,pady=4)
        lblDos.grid(row=2,column=0,sticky=W)
        txtDos= Entry(DataframLeft,textvariable=self.Dose,font=("arial",13,"bold"),width=29)
        txtDos.grid(row=2,column=1)

        lblNoOfTablets=Label(DataframLeft,text="No Of Tablets:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets= Entry(DataframLeft,textvariable=self.NumbersOfTablets,font=("arial",13,"bold"),width=29)
        txtNoOfTablets.grid(row=3,column=1)

        lblLot=Label(DataframLeft,text="Lot:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot= Entry(DataframLeft,textvariable=self.Lote,font=("arial",13,"bold"),width=29)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframLeft,text="Issue Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate= Entry(DataframLeft,textvariable=self.Issuedate,font=("arial",13,"bold"),width=29)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframLeft,text="Exp Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate= Entry(DataframLeft,textvariable=self.ExpDate,font=("arial",13,"bold"),width=29)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframLeft,text="Daily Dose:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose= Entry(DataframLeft,textvariable=self.DailyDose,font=("arial",13,"bold"),width=29)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframLeft,text="Side Effect:",font=("arial",12,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect= Entry(DataframLeft,textvariable=self.SideEffect,font=("arial",13,"bold"),width=29)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframLeft,text="Further Information:",font=("arial",12,"bold"),padx=30,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo= Entry(DataframLeft,textvariable=self.FurtherInformation,font=("arial",13,"bold"),width=29)
        txtFurtherinfo.grid(row=0,column=3)

        lblBooldPressure=Label(DataframLeft,text="Boold Pressure:",font=("arial",12,"bold"),padx=30,pady=6)
        lblBooldPressure.grid(row=1,column=2,sticky=W)
        txtBooldPressure= Entry(DataframLeft,textvariable=self.DrivingUsingMachine,font=("arial",13,"bold"),width=29)
        txtBooldPressure.grid(row=1,column=3)

        lblStorageAdvice=Label(DataframLeft,text="StorageAdvice:",font=("arial",12,"bold"),padx=30,pady=6)
        lblStorageAdvice.grid(row=2,column=2,sticky=W)
        txtStorageAdvice= Entry(DataframLeft,textvariable=self.StorageAdvice,font=("arial",13,"bold"),width=29)
        txtStorageAdvice.grid(row=2,column=3)

        lblMedication=Label(DataframLeft,text="Medication:",font=("arial",12,"bold"),padx=30,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        txtMedication= Entry(DataframLeft,textvariable=self.HowToUseMedication,font=("arial",13,"bold"),width=29)
        txtMedication.grid(row=3,column=3)

        lblPatientId=Label(DataframLeft,text="Patient Id:",font=("arial",12,"bold"),padx=30,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId= Entry(DataframLeft,textvariable=self.PatientId,font=("arial",13,"bold"),width=29)
        txtPatientId.grid(row=4,column=3)

        lblNHSnumbers=Label(DataframLeft,text="NHS Numbers:",font=("arial",12,"bold"),padx=30,pady=6)
        lblNHSnumbers.grid(row=5,column=2,sticky=W)
        txtNHSnumbers= Entry(DataframLeft,textvariable=self.nshNumber,font=("arial",13,"bold"),width=29)
        txtNHSnumbers.grid(row=5,column=3)

        lblPatientName=Label(DataframLeft,text="Patient Name:",font=("arial",12,"bold"),padx=30,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName= Entry(DataframLeft,textvariable=self.PatientName,font=("arial",13,"bold"),width=29)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframLeft,text="Date Of Birth:",font=("arial",12,"bold"),padx=30,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth= Entry(DataframLeft,textvariable=self.DateOfBirth,font=("arial",13,"bold"),width=29)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientadd=Label(DataframLeft,text="Patient Addres:",font=("arial",12,"bold"),padx=30,pady=6)
        lblPatientadd.grid(row=8,column=2,sticky=W)
        txtPatientadd= Entry(DataframLeft,textvariable=self.addess,font=("arial",13,"bold"),width=29)
        txtPatientadd.grid(row=8,column=3)

        #Dataframe right
        self.txtPrescription = Text(DataframRight,font=("arial",12,"bold"),width=35,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #buttons
        btnPrescription=Button(Buttonfram,command=self.iPrescription,text="Prescription",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=1,padx=5,pady=4)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData=Button(Buttonfram,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=1,padx=5,pady=4)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonfram,command=self.update_data,text="Update",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=1,padx=5,pady=4)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonfram,command=self.delete_data,text="Delete",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=1,padx=5,pady=4)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonfram,command=self.clear_data,text="Clear",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=1,padx=5,pady=4)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonfram,command=self.exit_data,text="Exit",bg="green",fg="white",font=("arial",11,"bold"),width=22,height=1,padx=5,pady=4)
        btnExit.grid(row=0,column=5)

        #Table, Scroll Bar
        scroll_x=ttk.Scrollbar(Detailsfram,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsfram,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsfram,column=("nameoftable","ref","dose","nooftablets","lot","issuedae",
                                                             "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x= ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y= ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedae",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Numbers")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="Date Of Birth")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedae",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()

        # Functinality Declaration
    def iPrescriptionData(self):
            if self.Nameoftablets.get() =="" or self.ref.get()=="":
                messagebox.showerror("Error","All field are required")
            else:
                conn = mysql.connector.connect(host="localhost",user="root",password="jp007",database="mydata")
                my_cursor=conn.cursor()
                # my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                #                                                                                     self.Nameoftablets.get(),
                #                                                                                     self.ref.get(),
                #                                                                                     self.Dose.get(),
                #                                                                                     self.NumbersOfTablets.get(),
                #                                                                                     self.Lote.get(),
                #                                                                                     self.Issuedate.get(),
                #                                                                                     self.ExpDate.get(),
                #                                                                                     self.DailyDose.get(),
                #                                                                                     self.StorageAdvice.get(),
                #                                                                                     self.nshNumber.get(),
                #                                                                                     self.PatientName.get(),
                #                                                                                     self.DateOfBirth.get(),
                #                                                                                     self.addess.get()       
                #                                                                                     ))
                tbl="insert into hospital(Nameoftablets,Reference_No,dose,Numbersoftablets,lot,issuedate,expdate,dailydose,storage,nhsnumber,patientname,DOB,patientaddress) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                data=(self.Nameoftablets.get(),self.ref.get(),self.Dose.get(),self.NumbersOfTablets.get(),self.Lote.get(),self.Issuedate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StorageAdvice.get(),self.nshNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.addess.get())
                my_cursor.execute(tbl,data)
                conn.commit()
                self.fatch_data()
                messagebox.showinfo("Result",(my_cursor.rowcount,"Record inserted"))

    def update_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="jp007",database="mydata")
        my_cursor=conn.cursor()
        # query="update hospital set Nameoftablets=%s,dose=%s,Numbersoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s where Reference_No=%s"
        # data=(self.Nameoftablets.get(),self.Dose.get(),self.NumbersOfTablets.get(),self.Lote.get(),self.Issuedate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StorageAdvice.get(),self.nshNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.addess.get(),self.ref.get())
        # my_cursor.execute(query,data)
        my_cursor.execute("update hospital set Nameoftablets=%s,dose=%s,Numbersoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s where Reference_No=%s",(
                                                                                                                                                                                                                                self.Nameoftablets.get(),
                                                                                                                                                                                                                                self.Dose.get(),
                                                                                                                                                                                                                                self.NumbersOfTablets.get(),
                                                                                                                                                                                                                                self.Lote.get(),
                                                                                                                                                                                                                                self.Issuedate.get(),
                                                                                                                                                                                                                                self.ExpDate.get(),
                                                                                                                                                                                                                                self.DailyDose.get(),
                                                                                                                                                                                                                                self.StorageAdvice.get(),
                                                                                                                                                                                                                                self.nshNumber.get(),
                                                                                                                                                                                                                                self.PatientName.get(),
                                                                                                                                                                                                                                self.DateOfBirth.get(),
                                                                                                                                                                                                                                self.addess.get(),
                                                                                                                                                                                                                                self.ref.get()
                                                                                                                                                                                                                                ))
        conn.commit()
        self.fatch_data()
        messagebox.showinfo("Update",(my_cursor.rowcount,"Data Updated."))
    
    def iPrescription(self):
        self.txtPrescription.insert(END,"Name Of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.NumbersOfTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lote:\t\t\t"+self.Lote.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.SideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Info:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"HowToUseMedication:\t\t\t"+self.HowToUseMedication.get()+"\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t"+self.nshNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DOB:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Addess:\t\t\t"+self.addess.get()+"\n")
    def delete_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="jp007",database="mydata")
        my_cursor=conn.cursor()
        query= "delete from hospital where Reference_No=%s"
        data = (self.ref.get(),)

        my_cursor.execute(query,data)
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete",(my_cursor.rowcount,"Data Deleted."))

    def clear_data(self):
        self.Nameoftablets.set(""),
        self.ref.set(""),
        self.Dose.set(""),
        self.NumbersOfTablets.set(""),
        self.Lote.set(""),
        self.Issuedate.set(""),
        self.ExpDate.set(""),
        self.DailyDose.set(""),
        self.StorageAdvice.set(""),
        self.nshNumber.set(""),
        self.PatientName.set(""),
        self.DateOfBirth.set(""),
        self.addess.set("")
    def exit_data(self):
        exit_data=messagebox.askyesno("Hospital Management system","Conform you want to exit")
        if exit_data>0:
            root.destroy()
            return    
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="jp007",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows= my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
        conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1]),
        self.Dose.set(row[2]),
        self.NumbersOfTablets.set(row[3]),
        self.Lote.set(row[4]),
        self.Issuedate.set(row[5]),
        self.ExpDate.set(row[6]),
        self.DailyDose.set(row[7]),
        self.StorageAdvice.set(row[8]),
        self.nshNumber.set(row[9]),
        self.PatientName.set(row[10]),
        self.DateOfBirth.set(row[11]),
        self.addess.set(row[12])  


root = Tk()
ob = Hospital(root)
root.mainloop()