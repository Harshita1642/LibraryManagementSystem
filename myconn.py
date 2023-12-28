import random
import string
import smtplib
import mysql.connector
import tkinter.messagebox as tmsg
class choice():
    def __init__(self):
        # import mysql.connector
        self.username="root"
        self.password="1234"
        self.database="library"
        try:
            self.conn=mysql.connector.connect(host="localhost",user=self.username,password=self.password,database=self.database)
            self.mycur=self.conn.cursor()
        except Exception as e:
            tmsg.showerror("DB Error","Error")
    def login(self,query):
        self.mycur.execute(query)
        for x in self.mycur:
            print(x)
        print("rows are",self.mycur.rowcount)
        if(self.mycur.rowcount==-1):
            print("Not available")
        else:
            print("Available")
        print("task completed")
    def executing(self,query):
        try:
            self.mycur.execute(query)
            self.conn.commit()
        except Exception as e:
            tmsg.showerror("showerror","Error")
    def getinfo(self,query):
        self.mycur.execute(query)
        return self.mycur
    def send_email(self,email_address: str, subject: str, body: str):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("harshita97003@gmail.com", "hweoumimaocumeia")
        server.sendmail("harshita97003@gmail.com", email_address,
                        "Subject: {}\n\n{}".format(subject, body))
        server.quit()
    def generate_password(self,length=8):
        characters=string.ascii_letters+string.digits + string.punctuation
        password=''.join(random.choice(characters) for i in range(length))
        return password
    def entry_validation(self,a,msg):
        x=False
        if(len(a)==0):
            tmsg.showerror("Problem",msg)
            x=True
        return x