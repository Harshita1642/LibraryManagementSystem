from tkinter import *
import customtkinter
import os
import mysql.connector
import myconn
from tkinter import ttk
import tkinter.messagebox as tmsg
from datetime import datetime
import time
from PIL import Image
customtkinter.set_appearance_mode("dark")
def entry_validation(a,msg):
    x=False
    if(len(a)==0):
        tmsg.showerror("Problem",msg)
        x=True
    return x
def duplicacy_check(a,query,msg):
    x=myconn.choice()
    y=x.getinfo(query)
    for i in y:
        t=i[0]
    # print(t)
    if(int(t)==1):
        tmsg.showerror("Problem",msg)
        return True
    else:
        return False
def datatype_check(a,msg):
    x=False
    try:
        a=int(a)
        #tmsg.showerror("Problem",msg)
        return x
    except:
        tmsg.showerror("Problem",msg)
        x=True
        return x
def treeview_issueddata():
    root=Tk()
    root.resizable(False,False)
    columns=('S_No','Rollno','Book_Id','Issued_data','Return_date')
    tv=ttk.Treeview(root,columns=columns)
    tv.column('#0',width=0,stretch=NO)
    tv.column('S_No',anchor=CENTER,width=80)
    tv.column('Rollno',anchor=CENTER,width=120)
    tv.column('Book_Id',anchor=CENTER,width=120)
    tv.column('Issued_data',anchor=CENTER,width=120)
    tv.column('Return_date',anchor=CENTER,width=120)
    tv.heading('#0',text='',anchor=CENTER)
    tv.heading('S_No',text='S_No',anchor=CENTER)
    tv.heading('Rollno',text='Rollno',anchor=CENTER)
    tv.heading('Book_Id',text='Book_Id',anchor=CENTER)
    tv.heading('Issued_data',text='Issued_data',anchor=CENTER)
    tv.heading('Return_date',text='Return_date',anchor=CENTER)
    x=myconn.choice()
    query="select * from studentcard order by S_No asc"
    y=x.getinfo(query)
    for i in y:
        tv.insert(parent="",index=0,values=i)
    tv.grid(row=0,column=0)
    y.close()
    tv.pack(side = 'left')    
    scrollbar = ttk.Scrollbar(root, orient = "vertical", command = tv.yview)  
    scrollbar.pack(side = 'left', fill = 'x')  
    tv.configure(xscrollcommand = scrollbar.set)
    root.mainloop()
def treeview_libregistor():
    from tkinter import ttk
    root=Toplevel()
    root.resizable(False,False)
    columns=('S_No','sname','class','rollno','bname','author','book_id','subjectcode','phoneno','Issued_data','Return_date')
    tv=ttk.Treeview(root,columns=columns)
    tv.pack(side="right")
    verscrlbar=ttk.Scrollbar(root,orient="vertical",command=tv.xview)
    tv.column('#0',width=0,stretch=NO)
    tv.column('S_No',anchor=CENTER,width=80)
    tv.column('sname',anchor=CENTER,width=120)
    tv.column('class',anchor=CENTER,width=120)
    tv.column('rollno',anchor=CENTER,width=80)
    tv.column('bname',anchor=CENTER,width=120)
    tv.column('author',anchor=CENTER,width=120)
    tv.column('book_id',anchor=CENTER,width=120)
    tv.column('subjectcode',anchor=CENTER,width=80)
    tv.column('phoneno',anchor=CENTER,width=120)
    tv.column('Issued_data',anchor=CENTER,width=120)
    tv.column('Return_date',anchor=CENTER,width=80)
    tv.heading('#0',text='',anchor=CENTER)
    tv.heading('S_No',text='S.No',anchor=CENTER)
    tv.heading('sname',text='Name',anchor=CENTER)
    tv.heading('class',text='Class',anchor=CENTER)
    tv.heading('rollno',text='Roll No',anchor=CENTER)
    tv.heading('bname',text='Title of Book',anchor=CENTER)
    tv.heading('author',text='Author',anchor=CENTER)
    tv.heading('book_id',text='Book Id',anchor=CENTER)
    tv.heading('subjectcode',text='Subject Code',anchor=CENTER)
    tv.heading('phoneno',text='phoneno',anchor=CENTER)
    tv.heading('Issued_data',text='Issued Date',anchor=CENTER)
    tv.heading('Return_date',text='Return Date',anchor=CENTER)
    x=myconn.choice()
    query="select sc.S_No,s.name,s.class,s.rollno,b.name,b.author,b.book_id,subjectcode,phoneno,Issued_data,Return_date from studentcard sc join student s on sc.Rollno=s.rollno join books b on sc.Book_Id=b.book_id"
    y=x.getinfo(query)
    for i in y:
        tv.insert(parent="",index=0,values=i)
    tv.grid(row=0,column=0)
    y.close()
    tv.pack(side = 'left')  
    scrollbar = ttk.Scrollbar(root, orient = "vertical", command = tv.yview)  
    scrollbar.pack(side = 'left', fill = 'x')  
    tv.configure(xscrollcommand = scrollbar.set)
    root.mainloop()
def treeview_student():
    from tkinter import ttk
    root=Tk()
    root.resizable(False,False)
    columns=('rollno','name','phoneno','Class')
    tv=ttk.Treeview(root,columns=columns)
    tv.column('#0',width=0,stretch=NO)
    tv.column('rollno',anchor=CENTER,width=80)
    tv.column('name',anchor=CENTER,width=120)
    tv.column('phoneno',anchor=CENTER,width=120)
    tv.column('Class',anchor=CENTER,width=80)
    tv.heading('#0',text='',anchor=CENTER)
    tv.heading('rollno',text='Roll no',anchor=CENTER)
    tv.heading('name',text='Name',anchor=CENTER)
    tv.heading('phoneno',text='Phone no',anchor=CENTER)
    tv.heading('Class',text='Class',anchor=CENTER)
    x=myconn.choice()
    query="select * from student"
    y=x.getinfo(query)
    for i in y:
        tv.insert(parent="",index=0,values=i)
    tv.grid(row=0,column=0)
    y.close()
    tv.pack(side = 'left')   
    scrollbar = ttk.Scrollbar(root, orient = "vertical", command = tv.yview)  
    scrollbar.pack(side = 'left', fill = 'x')  
    tv.configure(xscrollcommand = scrollbar.set)
    root.mainloop()
def deadlinecrossedrecords():
    root=Tk()
    columns=('S_No','Rollno','BookId','Issued_data','Return_date')
    tv=ttk.Treeview(root,columns=columns)
    tv.column('#0',width=0,stretch=NO)
    tv.column('S_No',anchor=CENTER,width=80)
    tv.column('Rollno',anchor=CENTER,width=120)
    tv.column('BookId',anchor=CENTER,width=80)
    tv.column('Issued_data',anchor=CENTER,width=120)
    tv.column('Return_date',anchor=CENTER,width=120)
    tv.heading('#0',text='',anchor=CENTER)
    tv.heading('S_No',text='S_No',anchor=CENTER)
    tv.heading('Rollno',text='Rollno',anchor=CENTER)
    tv.heading('BookId',text='BookId',anchor=CENTER)
    tv.heading('Issued_data',text='Issued_date',anchor=CENTER)
    tv.heading('Return_date',text='To_be_Return_date',anchor=CENTER)
    x=myconn.choice()
    query="select S_No,Rollno,Book_Id,Issued_data,Return_date from studentcard where now()>Return_date and actual_returning_date=0"
    y=x.getinfo(query)
    for i in y:
        tv.insert(parent="",index=0,values=i)
    tv.grid(row=0,column=0)
    y.close()
    tv.pack(side = 'left')   
    scrollbar = ttk.Scrollbar(root, orient = "vertical", command = tv.yview)  
    scrollbar.pack(side = 'left', fill = 'x')  
    tv.configure(xscrollcommand = scrollbar.set)
    root.mainloop()
def treeview_books():
    root=Tk()
    root.resizable(False,False)
    columns=('Id no','name','Subject','Author','Class','Price')
    tv=ttk.Treeview(root,columns=columns)  
    tv.column('#0',width=0,stretch=NO)
    tv.column('Id no',anchor=CENTER,width=100)
    tv.column('name',anchor=CENTER,width=120)
    tv.column('Subject',anchor=CENTER,width=80)
    tv.column('Author',anchor=CENTER,width=120)
    tv.column('Class',anchor=CENTER,width=80)
    tv.column('Price',anchor=CENTER,width=80)
    tv.heading('#0',text='',anchor=CENTER)
    tv.heading('Id no',text='Numberofbooks',anchor=CENTER)
    tv.heading('name',text='Title_Of_book',anchor=CENTER)
    tv.heading('Subject',text='Subject',anchor=CENTER)
    tv.heading('Author',text='Author',anchor=CENTER)
    tv.heading('Class',text='Class',anchor=CENTER)
    tv.heading('Price',text='Price',anchor=CENTER)
    x=myconn.choice()
    query="select count(*),name,subject,author,class,price from books where status='Y' group by author"
    y=x.getinfo(query)
    for i in y:
        tv.insert(parent="",index=0,values=i)
    tv.grid(row=0,column=0)
    y.close()
    tv.pack(side = 'left')   
    scrollbar = ttk.Scrollbar(root, orient = "vertical", command = tv.yview)  
    scrollbar.pack(side = 'left', fill = 'x')  
    tv.configure(xscrollcommand = scrollbar.set)
    root.mainloop()
class App(customtkinter.CTk):
    width=1000
    height=800
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("CustomTkinter example_background_image.py")
        self.geometry(f"{self.width}x{self.height}")
        #self.resizable(False, False)
        # create main frame
        self.main_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_label = customtkinter.CTkLabel(self.main_frame, text="Library Management System",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Admin",command=self.login_frame, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.back_button1 = customtkinter.CTkButton(self.main_frame, text="Student",command=self.loginstd_frame, width=200)
        self.back_button1.grid(row=2, column=0, padx=30, pady=(15, 15))
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms.png"),
                                  dark_image=Image.open("\Lms-Python\lms.png"),
                                  size=(600, 450))
        self.label = customtkinter.CTkLabel(self.main_frame, image=my_image)
        self.label.grid(row=0,column=2,padx=30, pady=(50, 15))
        #create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid_columnconfigure(0, weight=1)
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Login Page For Admin",
                                                  font=customtkinter.CTkFont(size=40, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login",command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms2.png"),
                                  dark_image=Image.open("\Lms-Python\lms2.png"),
                                  size=(900, 500))
        self.label = customtkinter.CTkLabel(self.login_frame, image=my_image)
        self.label.grid(row=0,rowspan=4,column=6,padx=30, pady=15)
        #create lms frame
        self.lms_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.lms_frame.grid_columnconfigure(0, weight=1)
        self.label= customtkinter.CTkLabel(self.lms_frame,text="Online Library System & Management",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn=customtkinter.CTkButton(self.lms_frame,text="Books Record",command=self.framework_book)
        self.btn.grid(row=1,column=2,ipadx=10,ipady=10,pady=10)
        self.btn2=customtkinter.CTkButton(self.lms_frame,text="Student Record",command=self.framework_std)
        self.btn2.grid(row=2,column=2,ipadx=2,ipady=10,pady=10)
        self.btn3=customtkinter.CTkButton(self.lms_frame,text="Issued Data",command=self.framework_issued_data)
        self.btn3.grid(row=3,column=2,ipadx=10,ipady=10,pady=10)
        self.btn4=customtkinter.CTkButton(self.lms_frame,text="Library Registor",command=self.framework_libregistor)
        self.btn4.grid(row=4,column=2,ipadx=10,ipady=10,pady=10)
        self.btn5 = customtkinter.CTkButton(self.lms_frame, text="Showcase The Deadline Crossed Records ",command=deadlinecrossedrecords, width=200)
        self.btn5.grid(row=5,column=2,ipadx=10,ipady=10,pady=10)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms9.png"),
                                  dark_image=Image.open("\Lms-Python\lms9.png"),
                                  size=(600, 600))
        self.label = customtkinter.CTkLabel(self.lms_frame, image=my_image)
        self.label.grid(row=0,rowspan=6,column=6,padx=30, pady=15)
        #create framework_book
        self.framework_book_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.framework_book_frame.grid_columnconfigure(0, weight=1)
        self.label=customtkinter.CTkLabel(self.framework_book_frame,text="Keeping Track of Books ",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.framework_book_frame,text="Add Book",command=self.open_bookrecord)
        self.btn1.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn2=customtkinter.CTkButton(self.framework_book_frame,text="Update Book",command=self.open_bookrecord1)
        self.btn2.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn3=customtkinter.CTkButton(self.framework_book_frame,text="Delete Book",command=self.open_bookrecord2)
        self.btn3.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn4=customtkinter.CTkButton(self.framework_book_frame,text="Show Books",command=treeview_books)
        self.btn4.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn5=customtkinter.CTkButton(self.framework_book_frame,text="Back",command=self.backTolms1)
        self.btn5.grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms7.png"),
                                  dark_image=Image.open("\Lms-Python\lms7.png"),
                                  size=(600, 600))
        self.label = customtkinter.CTkLabel(self.framework_book_frame, image=my_image)
        self.label.grid(row=0,rowspan=6,column=6,padx=30, pady=15) 
        #create framework for inserting a book
        self.open_bookrecord_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.open_bookrecord_frame.grid_columnconfigure(0, weight=1)
        self.label=customtkinter.CTkLabel(self.open_bookrecord_frame,text="Adding a new Book in Library",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordL1=customtkinter.CTkLabel(self.open_bookrecord_frame,text="Book Name",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.open_bookrecordL1.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordtxt1=customtkinter.CTkEntry(self.open_bookrecord_frame)
        self.open_bookrecordtxt1.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordL2=customtkinter.CTkLabel(self.open_bookrecord_frame,text="Subject",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.open_bookrecordL2.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordtxt2=customtkinter.CTkEntry(self.open_bookrecord_frame)
        self.open_bookrecordtxt2.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordL3=customtkinter.CTkLabel(self.open_bookrecord_frame,text="Subject Code",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.open_bookrecordL3.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordtxt3=customtkinter.CTkEntry(self.open_bookrecord_frame)
        self.open_bookrecordtxt3.grid(row=3,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordL4=customtkinter.CTkLabel(self.open_bookrecord_frame,text="Author",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.open_bookrecordL4.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordtxt4=customtkinter.CTkEntry(self.open_bookrecord_frame)
        self.open_bookrecordtxt4.grid(row=4,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordL5=customtkinter.CTkLabel(self.open_bookrecord_frame,text="Class",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.open_bookrecordL5.grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordtxt5=customtkinter.CTkEntry(self.open_bookrecord_frame)
        self.open_bookrecordtxt5.grid(row=5,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordL6=customtkinter.CTkLabel(self.open_bookrecord_frame,text="Price",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.open_bookrecordL6.grid(row=6,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecordtxt6=customtkinter.CTkEntry(self.open_bookrecord_frame)
        self.open_bookrecordtxt6.grid(row=6,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.open_bookrecord_frame,text="Insert",command=self.inserting_book)
        self.btn1.grid(row=5,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.open_bookrecord_frame,text="Back",command=self.backtoframewook_book_frame)
        self.btn1.grid(row=6,column=6,ipadx=10,ipady=10,padx=25,pady=25)  
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms9.png"),
                                  dark_image=Image.open("\Lms-Python\lms9.png"),
                                  size=(500, 500))
        self.label = customtkinter.CTkLabel(self.open_bookrecord_frame, image=my_image)
        self.label.grid(row=0,rowspan=5,column=6,padx=30, pady=15)
        #create framework to update book
        self.open_bookrecord1_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.open_bookrecord1_frame.grid_columnconfigure(0, weight=1)
        self.label=customtkinter.CTkLabel(self.open_bookrecord1_frame,text="Updating the Book Record",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1L1=customtkinter.CTkLabel(self.open_bookrecord1_frame,text="Book Id",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1txt1=customtkinter.CTkEntry(self.open_bookrecord1_frame)
        self.open_bookrecord1txt1.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1txt1.bind('<FocusOut>',self.fetching_bookdata)
        self.open_bookrecord1L2=customtkinter.CTkLabel(self.open_bookrecord1_frame,text="Book Name",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1txt2=customtkinter.CTkEntry(self.open_bookrecord1_frame)
        self.open_bookrecord1txt2.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1L3=customtkinter.CTkLabel(self.open_bookrecord1_frame,text="Subject",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1txt3=customtkinter.CTkEntry(self.open_bookrecord1_frame)
        self.open_bookrecord1txt3.grid(row=3,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1L4=customtkinter.CTkLabel(self.open_bookrecord1_frame,text="Author",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1txt4=customtkinter.CTkEntry(self.open_bookrecord1_frame)
        self.open_bookrecord1txt4.grid(row=4,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1L5=customtkinter.CTkLabel(self.open_bookrecord1_frame,text="Class",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1txt5=customtkinter.CTkEntry(self.open_bookrecord1_frame)
        self.open_bookrecord1txt5.grid(row=5,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1L6=customtkinter.CTkLabel(self.open_bookrecord1_frame,text="Price",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=6,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord1txt6=customtkinter.CTkEntry(self.open_bookrecord1_frame)
        self.open_bookrecord1txt6.grid(row=6,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn2=customtkinter.CTkButton(self.open_bookrecord1_frame,text="Update",command=self.updating_book)
        self.btn2.grid(row=5,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.open_bookrecord1_frame,text="Back",command=self.backtoframewook_book_frame1)
        self.btn1.grid(row=6,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms9.png"),
                                  dark_image=Image.open("\Lms-Python\lms9.png"),
                                  size=(550, 500))
        self.label = customtkinter.CTkLabel(self.open_bookrecord1_frame, image=my_image)
        self.label.grid(row=0,rowspan=5,column=6,padx=30, pady=15)
        #create a framework to delete book
        self.open_bookrecord2_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.open_bookrecord2_frame.grid_columnconfigure(0, weight=1)
        self.open_bookrecord2label=customtkinter.CTkLabel(self.open_bookrecord2_frame,text="Deleting Mistakenly Entered Record",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.open_bookrecord2label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord2L1=customtkinter.CTkLabel(self.open_bookrecord2_frame,text="Book Id",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord2txt1=customtkinter.CTkEntry(self.open_bookrecord2_frame)
        self.open_bookrecord2txt1.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord2L2=customtkinter.CTkLabel(self.open_bookrecord2_frame,text="Book Name",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.open_bookrecord2txt2=customtkinter.CTkEntry(self.open_bookrecord2_frame)
        self.open_bookrecord2txt2.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn3=customtkinter.CTkButton(self.open_bookrecord2_frame,text="Delete",command=self.deleting_book)
        self.btn3.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.open_bookrecord2_frame,text="Back",command=self.backtoframewook_book_frame2)
        self.btn1.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms9.png"),
                                  dark_image=Image.open("\Lms-Python\lms9.png"),
                                  size=(400, 500))
        self.label = customtkinter.CTkLabel(self.open_bookrecord2_frame, image=my_image)
        self.label.grid(row=0,rowspan=4,column=6,padx=30, pady=15)
        #create framework_std
        self.framework_std_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.framework_std_frame.grid_columnconfigure(0, weight=1)
        self.label=customtkinter.CTkLabel(self.framework_std_frame,text="Keeping Track Of Student Record  ",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.framework_std_frame,text="Add Student Data  ",command=self.std_record)
        self.btn1.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn2=customtkinter.CTkButton(self.framework_std_frame,text="Update Student Data",command=self.std_record1)
        self.btn2.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn3=customtkinter.CTkButton(self.framework_std_frame,text="Delete Student Data ",command=self.std_record2)
        self.btn3.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn4=customtkinter.CTkButton(self.framework_std_frame,text="Show Students Data",command=treeview_student)
        self.btn4.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn5=customtkinter.CTkButton(self.framework_std_frame,text="Back",command=self.backTolms)
        self.btn5.grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms8.png"),
                                  dark_image=Image.open("\Lms-Python\lms8.png"),
                                  size=(600, 600))
        self.label = customtkinter.CTkLabel(self.framework_std_frame, image=my_image)
        self.label.grid(row=0,rowspan=6,column=6,padx=30, pady=(10,15)) 
        # create framework to insert a student entry
        self.std_record_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.std_record_frame.grid_columnconfigure(0, weight=1)
        self.std_recordlabel=customtkinter.CTkLabel(self.std_record_frame,text="Adding A New Student Entry",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.std_recordlabel.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_recordL1=customtkinter.CTkLabel(self.std_record_frame,text="Roll Number",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_recordtxt1=customtkinter.CTkEntry(self.std_record_frame)
        self.std_recordtxt1.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_recordL2=customtkinter.CTkLabel(self.std_record_frame,text="Name",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_recordtxt2=customtkinter.CTkEntry(self.std_record_frame)
        self.std_recordtxt2.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_recordL3=customtkinter.CTkLabel(self.std_record_frame,text="Phone Number",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_recordtxt3=customtkinter.CTkEntry(self.std_record_frame)
        self.std_recordtxt3.grid(row=3,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_recordL4=customtkinter.CTkLabel(self.std_record_frame,text="Class",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_recordtxt4=customtkinter.CTkEntry(self.std_record_frame)
        self.std_recordtxt4.grid(row=4,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.std_record_frame,text="Insert",command=self.inserting_std)
        self.btn1.grid(row=3,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.std_record_frame,text="Back",command=self.backtoframewook_std_frame)
        self.btn1.grid(row=4,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms5.png"),
                                  dark_image=Image.open("\Lms-Python\lms5.png"),
                                  size=(500, 300))
        self.label = customtkinter.CTkLabel(self.std_record_frame, image=my_image)
        self.label.grid(row=0,rowspan=3,column=6,padx=30, pady=(10,15))
        #create a framework to update student data
        self.std_record1_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.std_record1_frame.grid_columnconfigure(0, weight=1)
        self.std_record1label=customtkinter.CTkLabel(self.std_record1_frame,text="Update A Student Record",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.std_record1label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record1L1=customtkinter.CTkLabel(self.std_record1_frame,text="Roll Number",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record1txt1=customtkinter.CTkEntry(self.std_record1_frame)
        self.std_record1txt1.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record1txt1.bind('<FocusOut>',self.fetching_std)
        self.std_record1L2=customtkinter.CTkLabel(self.std_record1_frame,text="Name",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record1txt2=customtkinter.CTkEntry(self.std_record1_frame)
        self.std_record1txt2.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record1L3=customtkinter.CTkLabel(self.std_record1_frame,text="Contact Number",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record1txt3=customtkinter.CTkEntry(self.std_record1_frame)
        self.std_record1txt3.grid(row=3,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record1L4=customtkinter.CTkLabel(self.std_record1_frame,text="Class",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record1txt4=customtkinter.CTkEntry(self.std_record1_frame)
        self.std_record1txt4.grid(row=4,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn2=customtkinter.CTkButton(self.std_record1_frame,text="Update",command=self.updating_std)
        self.btn2.grid(row=3,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.std_record1_frame,text="Back",command=self.backtoframewook_std_frame1)
        self.btn1.grid(row=4,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms5.png"),
                                  dark_image=Image.open("\Lms-Python\lms5.png"),
                                  size=(500, 300))
        self.label = customtkinter.CTkLabel(self.std_record1_frame, image=my_image)
        self.label.grid(row=0,rowspan=3,column=6,padx=30, pady=(10,15))
        #create a framework to delete a student entry
        self.std_record2_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.std_record2_frame.grid_columnconfigure(0, weight=1)
        self.std_record2label=customtkinter.CTkLabel(self.std_record2_frame,text="Deleting A Student Entry",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.std_record2label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record2L2=customtkinter.CTkLabel(self.std_record2_frame,text="Roll Number",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record2txt2=customtkinter.CTkEntry(self.std_record2_frame)
        self.std_record2txt2.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record2L3=customtkinter.CTkLabel(self.std_record2_frame,text="Name",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record2txt3=customtkinter.CTkEntry(self.std_record2_frame)
        self.std_record2txt3.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn3=customtkinter.CTkButton(self.std_record2_frame,text="Delete",command=self.deleting_std)
        self.btn3.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.std_record2_frame,text="Back",command=self.backtoframewook_std_frame2)
        self.btn1.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms5.png"),
                                  dark_image=Image.open("\Lms-Python\lms5.png"),
                                  size=(500, 500))
        self.label = customtkinter.CTkLabel(self.std_record2_frame, image=my_image)
        self.label.grid(row=0,rowspan=5,column=6,padx=30, pady=(10,15))
        # create a framework_issued
        self.framework_issued_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.framework_issued_frame.grid_columnconfigure(0, weight=1) 
        self.label=customtkinter.CTkLabel(self.framework_issued_frame,text="Keeping Track Of Issuing Of Books  ",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.framework_issued_frame,text="Add Issue Info  ",command=self.issued_data1)
        self.btn1.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn2=customtkinter.CTkButton(self.framework_issued_frame,text="Update Issue Info  ",command=self.issued_data)
        self.btn2.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn4=customtkinter.CTkButton(self.framework_issued_frame,text="Delete Issue Info  ",command=self.issued_data2)
        self.btn4.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn5=customtkinter.CTkButton(self.framework_issued_frame,text="Show Issue Info   ",command=treeview_issueddata)
        self.btn5.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn6=customtkinter.CTkButton(self.framework_issued_frame,text="Back  ",command=self.backTolms3)
        self.btn6.grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms6.png"),
                                  dark_image=Image.open("\Lms-Python\lms6.png"),
                                  size=(500, 500))
        self.label = customtkinter.CTkLabel(self.framework_issued_frame, image=my_image)
        self.label.grid(row=0,rowspan=6,column=4,padx=30, pady=(10,15))
        # create a framework to issue book
        self.issued_data1_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.issued_data1_frame.grid_columnconfigure(0, weight=1)
        self.issued_data1label=customtkinter.CTkLabel(self.issued_data1_frame,text="Issuing A Book  ",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.issued_data1label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_data1l1=customtkinter.CTkLabel(self.issued_data1_frame,text="Roll Number",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_data1txt1=customtkinter.CTkEntry(self.issued_data1_frame)
        self.issued_data1txt1.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_data1l2=customtkinter.CTkLabel(self.issued_data1_frame,text="Book Id",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_data1txt2=customtkinter.CTkEntry(self.issued_data1_frame)
        self.issued_data1txt2.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_data1l3=customtkinter.CTkLabel(self.issued_data1_frame,text="Time Period",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_data1txt3=customtkinter.CTkEntry(self.issued_data1_frame)
        self.issued_data1txt3.grid(row=3,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.issued_data1_frame,text="Insert",command=self.inserting_issueddata)
        self.btn1.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.issued_data1_frame,text="Back",command=self.backtoframework_issueddata1)
        self.btn1.grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms4.png"),
                                  dark_image=Image.open("\Lms-Python\lms4.png"),
                                  size=(500, 500))
        self.label = customtkinter.CTkLabel(self.issued_data1_frame, image=my_image)
        self.label.grid(row=0,rowspan=6,column=6,padx=30, pady=(10,15))
        # create a framework to delete issued record
        self.issued_data2_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.issued_data2_frame.grid_columnconfigure(0, weight=1)
        self.std_record2label=customtkinter.CTkLabel(self.issued_data2_frame,text="Deleting A Mistakenly Entered Entry  ",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.std_record2label.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record2l1=customtkinter.CTkLabel(self.issued_data2_frame,text="S_No",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=1,column=0,ipadx=10,ipady=10,padx=25,pady=25)
        self.std_record2txt1=customtkinter.CTkEntry(self.issued_data2_frame)
        self.std_record2txt1.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.issued_data2_frame,text="Delete",command=self.deleting_issueddata)
        self.btn1.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.issued_data2_frame,text="Back",command=self.backtoframework_issueddata2)
        self.btn1.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms4.png"),
                                  dark_image=Image.open("\Lms-Python\lms4.png"),
                                  size=(500, 500))
        self.label = customtkinter.CTkLabel(self.issued_data2_frame, image=my_image)
        self.label.grid(row=0,rowspan=4,column=4,padx=30, pady=(10,15))
        # create a framework_issued_data to reissue or return book
        self.issued_data_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.issued_data_frame.grid_columnconfigure(0, weight=1)
        self.issued_datalabel=customtkinter.CTkLabel(self.issued_data_frame,text="ReIssue Or Return A Book  ",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.issued_datalabel.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datal1=customtkinter.CTkLabel(self.issued_data_frame,text="S_No",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datatxt1=customtkinter.CTkEntry(self.issued_data_frame)
        self.issued_datatxt1.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datatxt1.bind('<FocusOut>',self.fetching_issueddata)
        self.issued_datal2=customtkinter.CTkLabel(self.issued_data_frame,text="Roll Number",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datatxt2=customtkinter.CTkEntry(self.issued_data_frame)
        self.issued_datatxt2.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datal3=customtkinter.CTkLabel(self.issued_data_frame,text="Book Id",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datatxt3=customtkinter.CTkEntry(self.issued_data_frame)
        self.issued_datatxt3.grid(row=3,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datal5=customtkinter.CTkLabel(self.issued_data_frame,text="Issuing date",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datatxt5=customtkinter.CTkEntry(self.issued_data_frame)
        self.issued_datatxt5.grid(row=4,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datal6=customtkinter.CTkLabel(self.issued_data_frame,text="Returning date",font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.issued_datatxt6=customtkinter.CTkEntry(self.issued_data_frame)
        self.issued_datatxt6.grid(row=5,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.issued_data_frame,text="Reissue",command=self.updating_issued)
        self.btn1.grid(row=4,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.issued_data_frame,text="Return",command=self.returning_book)
        self.btn1.grid(row=5,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.issued_data_frame,text="Back",command=self.backtoframework_issueddata)
        self.btn1.grid(row=6,column=3,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms4.png"),
                                  dark_image=Image.open("\Lms-Python\lms4.png"),
                                  size=(400, 400))
        self.label = customtkinter.CTkLabel(self.issued_data_frame, image=my_image)
        self.label.grid(row=0,rowspan=4,column=6,padx=30, pady=(10,15)) 
        # create a framework libregistor
        self.libregistor_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.libregistor_frame.grid_columnconfigure(0, weight=1)
        self.btn1=customtkinter.CTkButton(self.libregistor_frame,text="Show Library Registor",command=treeview_libregistor)
        self.btn1.grid(row=2,columnspan=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn2=customtkinter.CTkButton(self.libregistor_frame,text="Back",command=self.backTolms2)
        self.btn2.grid(row=4,columnspan=4,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms4.png"),
                                  dark_image=Image.open("\Lms-Python\lms4.png"),
                                  size=(600, 600))
        self.label = customtkinter.CTkLabel(self.libregistor_frame, image=my_image)
        self.label.grid(row=0,rowspan=6,column=6,padx=30, pady=15)
        # create a framework for studentlogin
        self.loginstd_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.loginstd_frame.grid_columnconfigure(0, weight=1)
        self.loginstdlabel=customtkinter.CTkLabel(self.loginstd_frame,text="Student Login  ",font=customtkinter.CTkFont(size=40, weight="bold") )
        self.loginstdlabel.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.loginstdlabel=customtkinter.CTkLabel(self.loginstd_frame,text="Roll Number",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.loginstdlabel.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.loginstdtxt=customtkinter.CTkEntry(self.loginstd_frame)
        self.loginstdtxt.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.loginstdlabel1=customtkinter.CTkLabel(self.loginstd_frame,text="Password",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.loginstdlabel1.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.loginstdtxt1=customtkinter.CTkEntry(self.loginstd_frame,show="*",placeholder_text="Password")
        self.loginstdtxt1.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn1=customtkinter.CTkButton(self.loginstd_frame,text="Login",command=self.loginstd_event)
        self.btn1.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn2=customtkinter.CTkButton(self.loginstd_frame,text="Sign Up",command=self.studentsignup)
        self.btn2.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn3=customtkinter.CTkButton(self.loginstd_frame,text="Forget Password",command=self.forgetpass_frame)
        self.btn3.grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms2.png"),
                                  dark_image=Image.open("\Lms-Python\lms2.png"),
                                  size=(600, 600))
        self.label = customtkinter.CTkLabel(self.loginstd_frame, image=my_image)
        self.label.grid(row=0,rowspan=6,column=6,padx=30, pady=15)
        #create a framework for forget password for students
        self.forgetpass_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.forgetpass_frame.grid_columnconfigure(0, weight=1)
        self.forgetpasslbl=customtkinter.CTkLabel(self.forgetpass_frame,text="Forget Password",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.forgetpasslbl.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.forgetpasslbl=customtkinter.CTkLabel(self.forgetpass_frame,text="Email Address",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.forgetpasslbl.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.forgetpasstxt=customtkinter.CTkEntry(self.forgetpass_frame)
        self.forgetpasstxt.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.forgetpassbtn=customtkinter.CTkButton(self.forgetpass_frame,text="Verify Password",command=self.verifypass)
        self.forgetpassbtn.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.forgetpassbtn1=customtkinter.CTkButton(self.forgetpass_frame,text="Back",command=self.backTologinstd)
        self.forgetpassbtn1.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms2.png"),
                                  dark_image=Image.open("\Lms-Python\lms2.png"),
                                  size=(600, 600))
        self.label = customtkinter.CTkLabel(self.forgetpass_frame, image=my_image)
        self.label.grid(row=0,rowspan=4,column=6,padx=30, pady=15)
        # create framework for student signup
        self.studentsignup_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.studentsignup_frame.grid_columnconfigure(0, weight=1)
        self.lbl1=customtkinter.CTkLabel(self.studentsignup_frame,text="Create a new account  ",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.lbl1.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.lbl=customtkinter.CTkLabel(self.studentsignup_frame,text="Roll Number",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.lbl.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.txt=customtkinter.CTkEntry(self.studentsignup_frame)
        self.txt.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.label1=customtkinter.CTkLabel(self.studentsignup_frame,text="Name",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label1.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.txt1=customtkinter.CTkEntry(self.studentsignup_frame)
        self.txt1.grid(row=2,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.label2=customtkinter.CTkLabel(self.studentsignup_frame,text="Email address",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label2.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.txt2=customtkinter.CTkEntry(self.studentsignup_frame)
        self.txt2.grid(row=3,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.label3=customtkinter.CTkLabel(self.studentsignup_frame,text="Group",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label3.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.txt3=customtkinter.CTkEntry(self.studentsignup_frame)
        self.txt3.grid(row=4,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.label4=customtkinter.CTkLabel(self.studentsignup_frame,text="Branch",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label4.grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.txt4=customtkinter.CTkEntry(self.studentsignup_frame)
        self.txt4.grid(row=5,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        btn1=customtkinter.CTkButton(self.studentsignup_frame,text="Sign Up",command=self.signup)
        btn1.grid(row=4,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        btn2=customtkinter.CTkButton(self.studentsignup_frame,text="Back",command=self.backTologinstd1)
        btn2.grid(row=5,column=6,ipadx=10,ipady=10,padx=25,pady=25)
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms2.png"),
                                  dark_image=Image.open("\Lms-Python\lms2.png"),
                                  size=(500, 500))
        self.label = customtkinter.CTkLabel(self.studentsignup_frame, image=my_image)
        self.label.grid(row=0,rowspan=4,column=6,padx=30, pady=(10,15))
    def login_event(self):
        x=myconn.choice()
        a,b=self.getInfo()
        print(a,b)
        if(a!=0):
            query="select password from createuseracc where username='{}'".format(a)
            y=x.getinfo(query)
            for i in y:
                t=str(i[0])
            if(t==b):
                    print("perfect credentials")
                    self.login_frame.grid_forget()
                    self.lms_frame.grid(row=0,column=0,sticky="nsew")
            else:
                x=myconn.choice()
                query="select password,emailaddress from createuseracc where username='{}'".format(a)
                y=x.getinfo(query)
                for i in y:
                    t=str(i[0])
                    t1=str(i[1])
                print(a,t,t1)
                #str1="It's a confirmation mail\nKindly Check your username='{}' and password='{}'".format(a,t)
                #print(str1)
                x.send_email(t1,"Unwanted login","It's a confirmation mail\nKindly Check your username='{}' and password='{}'".format(a,t))
                #print("done")     
                tmsg.showinfo("Info","Is it you \n Verification mail is sent to your email")  
    def getInfo(self):
            a=self.username_entry.get()
            b=self.password_entry.get()
            print("#")
            if(not(entry_validation(a,"Please Fill Username")or entry_validation(b,"Please Fill Password"))):
                return a,b
            else:
                return 0,0
    def login_frame(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="nsew")  # show login frame
    def loginstd_frame(self):
        self.main_frame.grid_forget()  # remove main frame
        self.loginstd_frame.grid(row=0, column=0, sticky="nsew")
    def framework_book(self):
        self.lms_frame.grid_forget()
        self.framework_book_frame.grid(row=0,column=0,sticky="nsew")
    def framework_std(self):
        self.lms_frame.grid_forget()
        self.framework_std_frame.grid(row=0,column=0,sticky="nsew")
    def framework_libregistor(self):
        self.lms_frame.grid_forget()
        self.libregistor_frame.grid(row=0,column=0,sticky="nsew")
    def open_bookrecord(self):
        self.framework_book_frame.grid_forget()
        self.open_bookrecord_frame.grid(row=0,column=0,sticky="nsew")
    def backtoframewook_book_frame(self):
        self.open_bookrecord_frame.grid_forget()
        self.framework_book_frame.grid(row=0,column=0,sticky="nsew")
    def backtoframewook_book_frame1(self):
        self.open_bookrecord1_frame.grid_forget()
        self.framework_book_frame.grid(row=0,column=0,sticky="nsew")
    def backtoframewook_book_frame2(self):
        self.open_bookrecord2_frame.grid_forget()
        self.framework_book_frame.grid(row=0,column=0,sticky="nsew")
    def backTolms(self):
        self.framework_std_frame.grid_forget()
        self.lms_frame.grid(row=0,column=0,sticky="nsew")
    def backTolms1(self):
        self.framework_book_frame.grid_forget()
        self.lms_frame.grid(row=0,column=0,sticky="nsew")
    def backTolms2(self):
        self.libregistor_frame.grid_forget()
        self.lms_frame.grid(row=0,column=0,sticky="nsew")
    def backTolms3(self):
        self.framework_issued_frame.grid_forget()
        self.lms_frame.grid(row=0,column=0,sticky="nsew")
    def framework_issued_data(self):
        self.lms_frame.grid_forget()
        self.framework_issued_frame.grid(row=0,column=0,sticky="nsew")
    def issued_data(self):
        self.framework_issued_frame.grid_forget()
        self.issued_data_frame.grid(row=0,column=0,sticky="nsew")
    def issued_data1(self):
        self.framework_issued_frame.grid_forget()
        self.issued_data1_frame.grid(row=0,column=0,sticky="nsew")
    def issued_data2(self):
        self.framework_issued_frame.grid_forget()
        self.issued_data2_frame.grid(row=0,column=0,sticky="nsew")
    def backtoframework_issueddata(self):
        self.issued_data_frame.grid_forget()
        self.framework_issued_frame.grid(row=0,column=0,sticky="nsew")
    def backtoframework_issueddata1(self):
        self.issued_data1_frame.grid_forget()
        self.framework_issued_frame.grid(row=0,column=0,sticky="nsew")
    def backtoframework_issueddata2(self):
        self.issued_data2_frame.grid_forget()
        self.framework_issued_frame.grid(row=0,column=0,sticky="nsew")
    def backTologinstd1(self):
        self.studentsignup_frame.grid_forget()
        self.loginstd_frame.grid(row=0,column=0,sticky="nsew")
    def backTologinstd(self):
        self.forgetpass_frame.grid_forget()
        self.loginstd_frame.grid(row=0,column=0,sticky="nsew")
    def forgetpass_frame(self):
        self.loginstd_frame.grid_forget()
        self.forgetpass_frame.grid(row=0,column=0,sticky="nsew")
    def verifypass(self):
        a=self.forgetpasstxt.get()
        if(not(entry_validation(a,"Please Fill Email Address"))):
            t=1
        else:
            t=0
        if(t!=0):
            x=myconn.choice()
            query="select rollno,password from createstdacc where emailaddress='{}'".format(a)
            y=x.getinfo(query)
            for i in y:
                m1=str(i[0])
                m2=str(i[1])
            x.send_email(a,"Verify It's You","As per you request of forget password\nKindly Check your username='{}' and password='{}'".format(m1,m2))
    def value_pickin_insert_book(self):
            a=self.open_bookrecordtxt1.get()
            b=self.open_bookrecordtxt2.get()
            c=self.open_bookrecordtxt3.get()
            d=self.open_bookrecordtxt4.get()
            e=self.open_bookrecordtxt5.get()
            f=self.open_bookrecordtxt6.get()
            print(a,b)
            if(not(entry_validation(a,"Please Fill Book Name") or entry_validation(b,"Please Fill Subject") 
            or entry_validation(c,"Please Fill SubjectCode") or entry_validation(d,"Please Fill Author Name") 
            or entry_validation(e,"Please Fill Class") or entry_validation(f,"Please Fill Price")
            or datatype_check(f,"Price should be integer") )):
                return a,b,c,d,e,f   
            else:
                return 0,0,0,0,0,0
    def inserting_book(self):
        a,b,c,d,e,f=self.value_pickin_insert_book()
        x=myconn.choice()
        if(a!=0):
                query="insert into books(name,subject,subjectcode,author,class,price,status) values('{}','{}','{}','{}','{}','{}','Y')".format(a,b,c,d,e,f)
                x.executing(query)
                a=tmsg.showinfo("Show Info","New Entry Inserted!!")
    def open_bookrecord1(self):
        self.framework_book_frame.grid_forget()
        self.open_bookrecord1_frame.grid(row=0,column=0,sticky="nsew")
    def fetching_bookdata(self,event):
            x=myconn.choice()
            a=self.open_bookrecord1txt1.get()
            query="select name,subject,author,class,price from books where book_id='{}'".format(a)
            y=x.getinfo(query)
            for i in y:
                self.open_bookrecord1txt2.delete(0,END)
                self.open_bookrecord1txt2.insert(0,str(i[0]))
                self.open_bookrecord1txt3.insert(0,str(i[1]))
                self.open_bookrecord1txt4.insert(0,str(i[2]))
                self.open_bookrecord1txt5.insert(0,str(i[3]))
                self.open_bookrecord1txt6.insert(0,str(i[4]))
    def updating_book(self):
        a=self.open_bookrecord1txt1.get()
        b=self.open_bookrecord1txt2.get()
        c=self.open_bookrecord1txt3.get()
        d=self.open_bookrecord1txt4.get()
        e=self.open_bookrecord1txt5.get()
        f=self.open_bookrecord1txt6.get()
        if(not(entry_validation(a,"Please Fill Book ID") or entry_validation(b,"Please Fill Book Name") 
            or entry_validation(c,"Please Fill Subject") or entry_validation(d,"Please Fill Author Name") 
            or entry_validation(e,"Please Fill price") )):
            t=1   
        else:
            t=0
        x=myconn.choice()
        if(t!=0):
                query="update books set price={} where book_id='{}'".format(f,a)
                x.executing(query)
                a=tmsg.showinfo("Show Info","Data Updated!!")
    def open_bookrecord2(self):
        self.framework_book_frame.grid_forget()
        self.open_bookrecord2_frame.grid(row=0,column=0,sticky="nsew")
    def deleting_book(self):
        b=self.open_bookrecord2txt1.get()
        c=self.open_bookrecord2txt2.get()
        if(not(entry_validation(b,"Please Fill  Rollno") or entry_validation(c,"Please Fill Name") )
               ):
            t=1
        else:
            t=0
        if(t!=0):
            x=myconn.choice()
            query="delete from student where rollno={} and name='{}' ".format(b,c)
            x.executing(query)
            a=tmsg.showinfo("Show Info","Entry Deleted!!")
    def std_record(self):
        self.framework_std_frame.grid_forget()
        self.std_record_frame.grid(row=0,column=0,sticky="nsew")
    def inserting_std(self):
        a=self.std_recordtxt1.get()
        b=self.std_recordtxt2.get()
        c=self.std_recordtxt3.get()
        d=self.std_recordtxt4.get()
        if(not(entry_validation(a,"Please Fill Rollno") or entry_validation(b,"Please Fill Name") 
            or entry_validation(c,"Please Fill Phoneno") or entry_validation(d,"Please Fill Class")) ):
                t=1
        else:
                t=0
        if(t!=0 and duplicacy_check(a,"select count(*) from student where rollno='{}'".format(a),"This Student is already registered")):
            x=myconn.choice()
            query="insert into student values({},'{}','{}','{}')".format(a,b,c,d)
            x.executing(query)
            a=tmsg.showinfo("Show Info","New Entry Inserted!!")
    def backtoframewook_std_frame(self):
        self.std_record_frame.grid_forget()
        self.framework_std_frame.grid(row=0,column=0,sticky="nsew")
    def backtoframewook_std_frame1(self):
        self.std_record1_frame.grid_forget()
        self.framework_std_frame.grid(row=0,column=0,sticky="nsew")
    def backtoframewook_std_frame2(self):
        self.std_record2_frame.grid_forget()
        self.framework_std_frame.grid(row=0,column=0,sticky="nsew")
    def std_record1(self):
        self.framework_std_frame.grid_forget()
        self.std_record1_frame.grid(row=0,column=0,sticky="nsew")
    def std_record2(self):
        self.framework_std_frame.grid_forget()
        self.std_record2_frame.grid(row=0,column=0,sticky="nsew")
    def updating_std(self):
        a=self.std_record1txt1.get()
        b=self.std_record1txt2.get()
        c=self.std_record1txt3.get()
        d=self.std_record1txt4.get()
        if(not(entry_validation(a,"Please Fill Rollno") or entry_validation(b,"Please Fill Name") 
            or entry_validation(c,"Please Fill Phoneno") or entry_validation(d,"Please Fill Class"))):
            t=1
        else:
            t=0
        x=myconn.choice()
        if(t!=0):
            query="update student set name='{}', phoneno='{}', class='{}' where rollno='{}'".format(b,c,d,a)
            x.executing(query)
            print("no you cant")
            a=tmsg.showinfo("Show Info","Data Updated!!")
    def fetching_std(self,event):
        x=myconn.choice()
        a=self.std_record1txt1.get()
        query="select name,phoneno,class from student where rollno='{}'".format(a)
        y=x.getinfo(query)
        for i in y:
            self.std_record1txt2.delete(0,END)
            self.std_record1txt2.insert(0,str(i[0]))
            self.std_record1txt3.insert(0,str(i[1]))
            self.std_record1txt4.insert(0,str(i[2]))
    def deleting_std(self):
        b=self.std_record2txt2.get()
        c=self.std_record2txt3.get()
        if(not(entry_validation(b,"Please Fill Rollno") or entry_validation(c,"Please Fill Student Name"))):
            t=1
        else:
            t=0
        if(t!=0):
            x=myconn.choice()
            query="delete from student where rollno={} and name='{}' ".format(b,c)
            x.executing(query)
            a=tmsg.showinfo("Show Info","Entry Deleted!!") 
    def fetching_issueddata(self,event):
            x=myconn.choice()
            a=self.issued_datatxt1.get()
            query="select Rollno,Book_Id,Issued_data,Return_date from studentcard where S_No='{}'".format(a)
            y=x.getinfo(query)
            for i in y:
                self.issued_datatxt2.delete(0,END)
                self.issued_datatxt2.insert(0,str(i[0]))
                self.issued_datatxt3.insert(0,str(i[1]))
                self.issued_datatxt5.insert(0,str(i[2]))
                self.issued_datatxt6.insert(0,str(i[3]))
    def updating_issued(self):
        a=self.issued_datatxt1.get()
        b=self.issued_datatxt2.get()
        c=self.issued_datatxt3.get()
        if(not(entry_validation(a,"Please Fill S_No") or entry_validation(b,"Please Fill Rollno") 
            or entry_validation(c,"Please Fill Book Id") ) and datatype_check(a,"S_No should be integer type")):
            t=1
        else:
            t=0
        if(t!=0):
            x=myconn.choice()
            query="update studentcard set rollno='{}',Book_Id={},Return_Date=now()+interval 7 day where S_No={} ".format(b,c,a)
            x.executing(query)
            a=tmsg.showinfo("Show Info","Data Updated!!")
    def returning_book(self):
        x=myconn.choice()
        a=self.issued_datatxt1.get()
        if((not(entry_validation(a,"Please Fill S_No")))):
            t=1
        else:
            t=0
        if(t!=0):
            query="select Return_date from studentcard where S_No='{}'".format(a)
            y=x.getinfo(query)
            for i in y:
                t1=str(i[0])
            query="update studentcard set actual_returning_date=now() where S_No='{}'".format(a)
            x.executing(query)
            query="select datediff(now(),'{}')".format(t1)
            y=x.getinfo(query)
            for i in y:
                days=str(i[0])
            if(int(days)==0):
                tmsg.showinfo("Show Info","Book Returned!!")
            else:
                fine=int(days)*5
                tmsg.showinfo("Show Info","U r charged a fine of {} Rupees.".format(fine))
    def inserting_issueddata(self):
        a=self.issued_data1txt1.get()
        b=self.issued_data1txt2.get()
        c=self.issued_data1txt3.get()
        if(not(entry_validation(a,"Please Fill Rollno") or entry_validation(b,"Please Fill Book Id") 
            or entry_validation(c,"Please Fill Time period"))):
            t=1
        else:
            t=0
        if(t!=0):
            x=myconn.choice()
            query2="select status from books where book_id={}".format(b)
            y=x.getinfo(query2)
            for i in y:
                m=str(i[0])
            print(m)
            if(m=='Y'):
                query="insert into studentcard (Rollno,Book_Id,Issued_data,Return_date,actual_returning_date) values({},'{}',now(),now()+interval {} day,0)".format(a,b,c)
                x.executing(query)
                    #print(b)
                query1="update books set status='N' where book_id={}".format(b)
                x.executing(query1)
                a=tmsg.showinfo("Show Info","New Entry Inserted!!")
            else:
                a=tmsg.showinfo("Show Info","This Book is not available")
    def deleting_issueddata(self):
        a=self.std_record2txt1.get()
        if(not(entry_validation(a,"Please Fill S_No"))):
            t=1
        else:
            t=0
        if(t!=0):
            x=myconn.choice()
            query="delete from studentcard where S_No={}".format(a)
            x.executing(query)
            a=tmsg.showinfo("Show Info","Entry Deleted!!")
    def loginstd_event(self):
        a=self.loginstdtxt.get()
        b=self.loginstdtxt1.get()
        if(not(entry_validation(a,"Please Fill Username") or (entry_validation(b,"Please Fill Password")))):
            t=1
        else:
            t=0
        if(t!=0):
            x=myconn.choice()
            query="select password from createstdacc where rollno='{}'".format(a)
            y=x.getinfo(query)
            for i in y:
                m=str(i[0])
            print(t)
            if(m==b):
                print("perfect credentials")
                self.stdsoftware(a)
            else:
                x=myconn.choice()
                query="select emailaddress from createstdacc where rollno='{}'".format(a)
                y=x.getinfo(query)
                for i in y:
                    t1=str(i[0])
                x.send_email("{}".format(t1),"Unwanted login","It's a confirmation mail\nKindly Check your username='{}' and password='{}'".format(a,m))
                print(a,m,t1)
                print("done")
    def stdsoftware(self,a):
        self.loginstd_frame.grid_forget()
        x=myconn.choice()
        print(a)
        query="select * from createstdacc where rollno='{}'".format(a)
        y=x.getinfo(query)
        for i in y:
            t=str(i[0])
            t1=str(i[1])
            t2=str(i[2])
            t3=str(i[3])
            t4=str(i[4])
        self.stdprofile_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.stdprofile_frame.grid_columnconfigure(0, weight=1)
        self.stdprofilelabel=customtkinter.CTkLabel(self.stdprofile_frame,text="Profile  ",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.stdprofilelabel.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.stdprofilelbl=customtkinter.CTkLabel(self.stdprofile_frame,text="Roll no: '{}'".format(t),font=customtkinter.CTkFont(size=20, weight="bold"))
        self.stdprofilelbl.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.stdprofilelbl1=customtkinter.CTkLabel(self.stdprofile_frame,text="Name: '{}'".format(t1),font=customtkinter.CTkFont(size=20, weight="bold"))
        self.stdprofilelbl1.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.stdprofilelbl2=customtkinter.CTkLabel(self.stdprofile_frame,text="Group: '{}'".format(t3),font=customtkinter.CTkFont(size=20, weight="bold"))
        self.stdprofilelbl2.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.stdprofilelbl3=customtkinter.CTkLabel(self.stdprofile_frame,text="Branch: '{}'".format(t4),font=customtkinter.CTkFont(size=20, weight="bold"))
        self.stdprofilelbl3.grid(row=4,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.stdprofilelbl4=customtkinter.CTkLabel(self.stdprofile_frame,text="Email address: '{}'".format(t2),font=customtkinter.CTkFont(size=20, weight="bold"))
        self.btn2=customtkinter.CTkButton( self.stdprofile_frame,text="Availability of Books",command=self.showavailablebooks)
        self.btn2.grid(row=5,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.btn3=customtkinter.CTkButton(self.stdprofile_frame,text="History    ",command=self.treeview_history)
        self.btn3.grid(row=5,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        self.stdprofile_frame.grid(row=0,column=0,sticky="nsew")
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms7.png"),
                                  dark_image=Image.open("\Lms-Python\lms7.png"),
                                  size=(600, 600))
        self.label = customtkinter.CTkLabel(self.stdprofile_frame, image=my_image)
        self.label.grid(row=0,rowspan=6,column=6,padx=30, pady=(10,15))
    def treeview_history(self):
        a=self.loginstdtxt.get()
        root=Tk()
        root.resizable(False,False)
        columns=('S_No','Rollno','Book_Id','Issued_data','Return_date')
        tv=ttk.Treeview(root,columns=columns)
        tv.column('#0',width=0,stretch=NO)
        tv.column('S_No',anchor=CENTER,width=80)
        tv.column('Rollno',anchor=CENTER,width=120)
        tv.column('Book_Id',anchor=CENTER,width=120)
        tv.column('Issued_data',anchor=CENTER,width=120)
        tv.column('Return_date',anchor=CENTER,width=120)
        tv.heading('#0',text='',anchor=CENTER)
        tv.heading('S_No',text='S_No',anchor=CENTER)
        tv.heading('Rollno',text='Rollno',anchor=CENTER)
        tv.heading('Book_Id',text='Book_Id',anchor=CENTER)
        tv.heading('Issued_data',text='Issued_data',anchor=CENTER)
        tv.heading('Return_date',text='Return_date',anchor=CENTER)
        x=myconn.choice()
        query="select * from studentcard where Rollno='{}' order by S_No asc".format(a)
        y=x.getinfo(query)
        for i in y:
            tv.insert(parent="",index=0,values=i)
        tv.grid(row=0,column=0)
        y.close()
        tv.pack(side = 'left')    
        scrollbar = ttk.Scrollbar(root, orient = "vertical", command = tv.yview)  
        scrollbar.pack(side = 'left', fill = 'x')  
        tv.configure(xscrollcommand = scrollbar.set)
        root.mainloop()
    def showavailablebooks(self):
        self.availablebooks_frame=customtkinter.CTkFrame(self,corner_radius=0)
        self.availablebooks_frame.grid_columnconfigure(0, weight=1)
        self.availablebookslbl1=customtkinter.CTkLabel(self.availablebooks_frame,text="Avialable books of your choice",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.availablebookslbl1.grid(row=0,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.availablebookslbl=customtkinter.CTkLabel(self.availablebooks_frame,text="Subject Code",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.availablebookslbl.grid(row=1,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.availablebookstxt=customtkinter.CTkEntry(self.availablebooks_frame)
        self.availablebookstxt.grid(row=1,column=4,ipadx=10,ipady=10,padx=25,pady=25)
        btn1=customtkinter.CTkButton(self.availablebooks_frame,text="Proceed",command=self.books)
        btn1.grid(row=2,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        btn2=customtkinter.CTkButton(self.availablebooks_frame,text="Back")
        btn2.grid(row=3,column=2,ipadx=10,ipady=10,padx=25,pady=25)
        self.stdprofile_frame.grid_forget()
        self.availablebooks_frame.grid(row=0,column=0,sticky="nsew")
        self.stdprofile_frame.grid(row=0,column=0,sticky="nsew")
        my_image = customtkinter.CTkImage(light_image=Image.open("\Lms-Python\lms10.png"),
                                  dark_image=Image.open("\Lms-Python\lms10.png"),
                                  size=(600, 600))
        self.label = customtkinter.CTkLabel(self.availablebooks_frame, image=my_image)
        self.label.grid(row=0,rowspan=4,column=6,padx=30, pady=(10,15))
    def books(self):
        a=self.availablebookstxt.get()
        root=Tk()
        columns=('Id no','name','Subject','Author','Class','Price')
        tv=ttk.Treeview(root,columns=columns)
        tv.column('#0',width=0,stretch=NO)
        tv.column('Id no',anchor=CENTER,width=80)
        tv.column('name',anchor=CENTER,width=120)
        tv.column('Subject',anchor=CENTER,width=80)
        tv.column('Author',anchor=CENTER,width=120)
        tv.column('Class',anchor=CENTER,width=80)
        tv.column('Price',anchor=CENTER,width=80)
        tv.heading('#0',text='',anchor=CENTER)
        tv.heading('Id no',text='Id no',anchor=CENTER)
        tv.heading('name',text='Title_Of_book',anchor=CENTER)
        tv.heading('Subject',text='Subject',anchor=CENTER)
        tv.heading('Author',text='Author',anchor=CENTER)
        tv.heading('Class',text='Class',anchor=CENTER)
        tv.heading('Price',text='Price',anchor=CENTER)
        conn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
        mycurr=conn.cursor()
        mycurr.execute("select book_id,name,author,subject,class,price from books where subjectcode='{}' and status='{}'".format(a,'Y'))
        for i in mycurr:
            tv.insert(parent="",index=0,values=i)
            tv.grid(row=0,column=0)
        mycurr.close()
        root.mainloop()
    def studentsignup(self):
        self.loginstd_frame.grid_forget()
        self.studentsignup_frame.grid(row=0,column=0,sticky="nsew")
    def signup(self):
        a=self.txt.get()
        b=self.txt1.get()
        c=self.txt2.get()
        d=self.txt3.get()
        e=self.txt4.get()
        if(not(entry_validation(a,"Please Fill Rollno") or entry_validation(b,"Please Fill Name") or entry_validation(c,"Please Fill Email Address")
               or entry_validation(d,"Please Fill Groupno") or entry_validation(e,"Please Fill Branch"))):
            t=1
        else:
            t=0
        if(t!=0):
            x=myconn.choice()
            y=x.generate_password(8)
            query="insert into createstdacc values('{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,y)
            x.executing(query)
            x.send_email("{}".format(c),"Your Account is created","New account confirmation mail\n Username='{}' and Password='{}'".format(a,y))
            self.stdsoftware()
if __name__ == "__main__":
    app = App()
    app.mainloop()