from tkinter import*
from tkinter import messagebox
import mysql.connector


def main():
    screen=Tk()
    app=Portal(screen)
    screen.mainloop()

class Register_window:
    def __init__(self,screen):
        self.screen=screen
        self.screen.title("Registeration Form")
        self.screen.geometry("450x500")
        self.screen.resizable(False,False)
        Label(self.screen,text="Register here",font="Times 30 bold",bg="red",fg="white").pack(fill="both")
        Label(self.screen,text="Name",font="20").place(x=45,y=100)
        Label(self.screen,text="Roll number",font="20").place(x=45,y=150) 
        Label(self.screen,text="Section",font="20").place(x=45,y=200)
        Label(self.screen,text="Password",font="20").place(x=45,y=250)
        self.name_info=StringVar()
        self.regno_info=StringVar()
        self.section_info=StringVar()
        self.passw_info=StringVar()
        self.name_entry=Entry(self.screen,font="10",bd="4",textvariable=self.name_info)
        self.name_entry.place(x=205,y=100)
        self.regno_entry=Entry(self.screen,font="10",bd="4",textvariable=self.regno_info)
        self.regno_entry.place(x=205,y=150)
        self.section_entry=Entry(self.screen,font="10",bd="4",textvariable=self.section_info)
        self.section_entry.place(x=205,y=200)
        self.pass_entry=Entry(self.screen,font="10",bd="4",textvariable=self.passw_info)
        self.pass_entry.place(x=205,y=250)
        Button(self.screen, text="Register",font="50",bg="red",fg="white",command=self.register).place(x=185,y=350)

    def register(self):
        name=self.name_info.get()
        regno=self.regno_info.get()
        section=self.section_info.get()
        passw=self.passw_info.get()
        enter_into_db=(regno,name,section,passw)
        if name=="":
            messagebox.showerror("Empty Field!!!","Please enter your Name")
        elif regno=="":
            messagebox.showerror("Empty Field!!!","Please enter your Roll Number")
        elif section=="":
            messagebox.showerror("Empty Field!!!","Please enter your Section")
        elif passw=="":
            messagebox.showerror("Empty Field!!!","Please enter your Password")
        else:  
            conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
            cur=conn.cursor()
            query=("select * from register where rollno=%s")
            value=(regno)
            cur.execute(query,(value,))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Account already created try loging in")
            else:
                cur.execute("insert into register values(%s,%s,%s,%s)",enter_into_db)
                success=Label(self.screen,text="Registeration Successfull !!!",font="10",fg="green").place(x=130,y=400)
            conn.commit()
            conn.close()


class Login_window():
    def __init__(self,screenlw):
        self.screenlw=screenlw
        self.screenlw.title("Login here")
        self.screenlw.geometry("450x500")
        self.screenlw.resizable(False,False)
        self.passw_etd=StringVar()
        self.regno_etd=StringVar()


        Label(screenlw,text="Login here",font="Times 30 bold",bg="red",fg="white").pack(fill="both")
        Label(screenlw,text="Roll number",font="20").place(x=45,y=150) 
        Label(screenlw,text="Password",font="20").place(x=45,y=250)
        self.regno_loginenter=Entry(screenlw,font="10",bd="4",textvariable=self.regno_etd)
        self.regno_loginenter.place(x=205,y=150)
        self.pass_loginenter=Entry(screenlw,font="10",bd="4",textvariable=self.passw_etd)
        self.pass_loginenter.place(x=205,y=250)
        Button(screenlw, text="Login",font="50",bg="red",fg="white",command=self.login).place(x=185,y=350)
        mainloop()

    def login(self):
        self.regno=self.regno_etd.get()
        self.passw=self.passw_etd.get()
        self.cred=(self.regno,self.passw)

        if self.regno=="" or self.passw=="":
            messagebox.showerror("Empty Field!!!","All field are required")
        else:
            conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
            cur=conn.cursor()
            cur.execute("select * from register where rollno=%s and passw=%s",self.cred)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                messagebox.showerror("Error","entered")

class Portal:
    def __init__(self,scn):
        self.scn=scn
        self.scn.geometry("300x250")
        self.scn.resizable(False,False)
        self.scn.title("Quiz")
        Button(self.scn,text="Register",font="Times 30 bold",bg="red",fg="white",command=self.register_window).place(x=60,y=10)
        Button(self.scn,text="Login",font="Times 30 bold",bg="red",fg="white",command=self.login_window).place(x=80,y=100)   


    def register_window(self):
        self.reg_screen=Toplevel(self.scn)
        self.reg_scn=Register_window(self.reg_screen)


    def login_window(self):
        self.lgn_screen=Toplevel(self.scn)
        self.lgn_scn=Login_window(self.lgn_screen)
        self.lgn_scn.mainloop()

if __name__=="__main__":
    main()

