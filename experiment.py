from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk
import random
import time


def main():
    screen=Tk()
    app=Portal(screen)
    screen.mainloop()

class Register_window:
    def login_window(self):
        self.lgn_screen=Toplevel(self.scn)
        self.lgn_scn=Login_window(self.lgn_screen)
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
        Button(self.screen, text="Already have an account ? Login here",font="50",fg="green",command=self.login_window).place(x=150,y=450)
    
    def login_window(self):
        # self.lgn_screen=Toplevel(self.screen)
        # self.lgn_scn=Login_window(self.lgn_screen)
        self.screen.destroy()
        screen=Tk()
        app=Login_window(screen)
        screen.mainloop()

    def register(self):
        name=self.name_info.get()
        regno=self.regno_info.get()
        section=self.section_info.get()
        passw=self.passw_info.get()
        score=0
        enter_into_db=(regno,name,section,passw,score)
        if name=="":
            messagebox.showerror("Empty Field!!!","Please enter your Name")
        elif regno=="":
            messagebox.showerror("Empty Field!!!","Please enter your Roll Number")
        elif (not regno.isnumeric()):
            messagebox.showerror("Invalid Entry","Roll Number must be numeric")
        elif section=="":
            messagebox.showerror("Empty Field!!!","Please enter your Section")
        elif passw=="":
            messagebox.showerror("Empty Field!!!","Please enter your Password")
        else:  
            conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
            cur=conn.cursor()
            query=("select * from student where rollno=%s")
            value=(regno)
            cur.execute(query,(value,))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Account already created try loging in")
            else:
                cur.execute("insert into student values(%s,%s,%s,%s,%s)",enter_into_db)
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
        Button(screenlw, text="Login",font="50",bg="red",fg="white",command=self.login).place(x=175,y=350)
        mainloop()

    def login(self):
        self.regno=self.regno_etd.get()
        self.passw=self.passw_etd.get()
        self.cred=(self.regno,self.passw)
        global rollnumber
        rollnumber=self.regno

        if self.regno=="" or self.passw=="":
            messagebox.showerror("Empty Field!!!","All field are required")
        else:
            conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
            cur=conn.cursor()
            cur.execute("select * from student where rollno=%s and passw=%s",self.cred)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                # messagebox.showerror("Error","entered")
                # self.quiz=Toplevel(self.screenlw)
                # self.quiz=questions(self.quiz)
                self.screenlw.destroy()
                screen=Tk()
                app=questions(screen)
                screen.mainloop()


class Portal:
    def __init__(self,scn):
        self.scn=scn
        self.scn.geometry("450x500")
        self.scn.resizable(False,False)
        self.scn.title("Quiz")
        Rimage = Image.open("rg.jpg")
        resize_image = Rimage.resize((100, 50))
        img = ImageTk.PhotoImage(resize_image)
        Button(self.scn,text="Register",font="Times 30 bold",bg="red",fg="white",command=self.register_window).place(x=135,y=71)
        # b1=Button(self.scn,image=img,font="Times 30 bold",bg="red",fg="white",command=self.register_window)
        # b1.place(x=135,y=71)
        # b1.image=img
        # b1.pack()
        # Button(self.scn,image=img,font="Times 30 bold",bg="red",fg="white",command=self.register_window)
        Button(self.scn,text="Login",font="Times 30 bold",bg="red",fg="white",command=self.login_window).place(x=160,y=213)   
        Button(self.scn,text="Leaderboard",font="Times 30 bold",bg="red",fg="white",command=self.leaderboard_window).place(x=100,y=355)   


    def register_window(self):
        # self.reg_screen=Toplevel(self.scn)
        # self.reg_scn=Register_window(self.reg_screen)
        self.scn.destroy()
        screen=Tk()
        app=Register_window(screen)
        screen.mainloop()


    def login_window(self):
        self.scn.destroy()
        screen=Tk()
        app=Login_window(screen)
        screen.mainloop()

    def leaderboard_window(self):
        self.lgn_screen=Toplevel(self.scn)
        self.lgn_scn=Leaderboard(self.lgn_screen)




class questions:
    def __init__(self , root):
        global txtlabel ,labelinst ,labelinstr ,E_button ,M_button ,H_button
        # this is for a single window program in which we are going to destroy the previous things and create new things
        # in multi window whole previous window is destroyed and new window is created
        self.root = root
        self.root.title("Quiz")
        self.root.geometry('700x600')
        self.root.config(bg="white")
        self.root.resizable(0, 0)

        # img1 = PhotoImage(file="terentula nebula.png")
        # img1label = Label(self.root, image=img1, bg="white")
        # img1label.pack(paddy = (40,0))

        txtlabel = Label(
            self.root,
            text="Python Quiz",
            font=("Arial", 30, "bold"),
            bg="white"

        )
        txtlabel.pack(pady=(30, 50))


        # img2 = PhotoImage(file="file name")

        labelinst = Label(
            self.root,
            text="Instructions\n",
            font=("Arial", 20),
            bg="white",
            justify="center"
        )
        labelinst.pack(pady=(10, 0))

        labelinstr = Label(
            self.root,
            text="points",
            width=100,
            font=("Arial", 15),
            bg="black",
            foreground="yellow"
        )
        labelinstr.pack(pady=(0, 30))

        # a = questions()
        # use image=img1 in place of text in button
        E_button = Button(
            self.root,
            text="Easy",
            relief=FLAT,
            command=self.Easy
        )
        E_button.pack(pady=(0, 30))


        M_button = Button(
            self.root,
            text="Medium",
            relief=FLAT,
            command=self.Medium
        )
        M_button.pack(pady=(0, 30))


        H_button = Button(
            self.root,
            text="Hard",
            relief=FLAT,
            command=self.Hard
        )
        H_button.pack(pady=(0, 30))


    questions = [
        "1 question",
        "2 question",
        "3 question",
        "4 question",
        "5 question",
        "6 question",
        "7 question",
        "8 question",
        "9 question",
        "10 question",
    ]

    choice_ans = [
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
    ]

    # will contain the correct answers of questions
    answers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    user_ans = []
    indexes = []
    count = 1


    def gen(self):
        while(len(self.indexes) < 5):
            x = random.randint(0, 9)
            # if x not in indexes:
            #     indexes.append(x)
            if x in self.indexes:
                continue
            else:
                self.indexes.append(x)

    def showresult(self,score):
        global questionlabel ,r1 ,r2 , r3 , r4 
        # print("roll number is: ")
        # print(rollnumber)
        # print(score)
        valinp=(score,rollnumber)
        conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
        ask_cur=conn.cursor()
        ask_query=("select score from student where rollno=%s")
        ask_cur.execute(ask_query,(rollnumber,))
        row=ask_cur.fetchone()
        prev_score=row[0]
        if(prev_score<score):
            #write here that congragulations you score better than previous attempt
            cur=conn.cursor()
            query=("update student set score=%s where rollno=%s")
            cur.execute(query,valinp)
            conn.commit()
            conn.close()
        else:
            pass
            #write here that your previous score was better so your score is not appeared
        questionlabel.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()

        labelimg = Label(
            self.root,
            bg="white",
            border=0
        )
        labelimg.pack()

        labelresulttext = Label(
            self.root,
            font=("Arial", 20),
            bg="white"
        )
        labelresulttext.pack()

        if score >= 20:
            # img = PhotoImage(file="image.png")
            # labelimg.configure(image=img)
            # labelimage.image = img
            labelresulttext.configure(
                text="You did excellent !!!!!\n\n you got " + str(score)
            )

        elif score < 20 or score >= 10:
            # img = PhotoImage(file="image.png")
            # labelimg.configure(image=img)
            # labelimage.image = img
            labelresulttext.configure(
                text="You can do better !!!!!\n\n you got " + str(score)
            )

        elif score < 10:
            # img = PhotoImage(file="image.png")
            # labelimg.configure(image=img)
            # labelimage.image = img
            labelresulttext.configure(
                text="you should work hard !!!!!\n\n you got " + str(score)
            )

        return score

    def calc(self):
        # global indexes, user_ans, answers
        x1 = 0
        score = 0
        for i in self.indexes:
            # print("temp = ", x1)
            if self.user_ans[x1] == self.answers[i]:
                score += 5
            x1 += 1
        # print("score = ", score)
        self.showresult(score)

    def selected(self):
        global questionlabel ,r1 ,r2 , r3 , r4
        x = self.radiovar.get()
        # here x will get the value which user choose as input
        # print(x)
        self.user_ans.append(x)
        self.radiovar.set(-1)
        if self.count < 5:
            questionlabel.config(text=self.questions[self.indexes[self.count]])
            r1['text'] = self.choice_ans[self.indexes[self.count]][0]
            r2['text'] = self.choice_ans[self.indexes[self.count]][1]
            r3['text'] = self.choice_ans[self.indexes[self.count]][2]
            r4['text'] = self.choice_ans[self.indexes[self.count]][3]
            self.count += 1
        else:
            print(self.indexes)
            print(self.user_ans)
            self.calc()

    def start_Q(self):
        global questionlabel ,r1 ,r2,r3,r4
        questionlabel = Label(
            self.root,
            # text="Sample Question which can be too long it will be in next line due to wrap length",
            text=self.questions[self.indexes[0]],
            font=("Arial", 16),
            width=500,
            justify="center",
            wraplength=400,
            bg="white",
        )
        questionlabel.pack(pady=(100, 30))

        self.radiovar = IntVar()
        self.radiovar.set(-1)
        # by setting radio var -1 it will not check any option automatically

        r1 = Radiobutton(
            self.root,
            text=self.choice_ans[self.indexes[0]][0],
            font=("Times", 12),
            value=0,
            variable=self.radiovar,
            command=self.selected,
            bg="white",
        )
        r1.pack(pady=5)

        r2 = Radiobutton(
            self.root,
            text=self.choice_ans[self.indexes[0]][1],
            font=("Times", 12),
            value=1,
            variable=self.radiovar,
            command=self.selected,
            bg="white",
        )
        r2.pack(pady=5)

        r3 = Radiobutton(
            self.root,
            text=self.choice_ans[self.indexes[0]][2],
            font=("Times", 12),
            value=2,
            variable=self.radiovar,
            command=self.selected,
            bg="white",
        )
        r3.pack(pady=5)

        r4 = Radiobutton(
            self.root,
            text=self.choice_ans[self.indexes[0]][3],
            font=("Times", 12),
            value=3,
            variable=self.radiovar,
            command=self.selected,
            bg="white",
        )
        r4.pack(pady=5)

    def Easy(self):
        labelinst.destroy()
        labelinstr.destroy()
        # img1label.destroy()
        txtlabel.destroy()
        E_button.destroy()
        M_button.destroy()
        H_button.destroy()
        self.gen()
        self.start_Q()

    def Medium(self):
        labelinst.destroy()
        labelinstr.destroy()
        # img1label.destroy()
        txtlabel.destroy()
        E_button.destroy()
        M_button.destroy()
        H_button.destroy()
        self.gen()
        self.start_Q()

    def Hard(self):
        labelinst.destroy()
        labelinstr.destroy()
        # img1label.destroy()
        txtlabel.destroy()
        E_button.destroy()
        M_button.destroy()
        H_button.destroy()
        self.gen()
        self.start_Q()

class Leaderboard:
    def __init__(self,scn):
        self.scn=scn
        self.scn.geometry("900x500")
        self.scn.resizable(False,False)
        self.scn.title("Leaderboard") 
            
        self.tree = ttk.Treeview(self.scn, column=("c1", "c2", "c3","c4"), show='headings')

        self.tree.column("#1", anchor=CENTER)

        self.tree.heading("#1", text="Roll no.")

        self.tree.column("#2", anchor=CENTER)

        self.tree.heading("#2", text="Name")

        self.tree.column("#3", anchor=CENTER)

        self.tree.heading("#3", text="Section")

        self.tree.column("#4", anchor=CENTER)

        self.tree.heading("#4", text="Score")

        self.tree.pack()
        self.viewsb()
        # Button(text="Show Leaderboard", command=self.viewsb).place(x=300,y=300)



    def viewsb(self):
        conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
        cur=conn.cursor()
        query=("select rollno,name,section,score from student order by score desc")
        cur.execute(query)
        rows=cur.fetchall()
        for row in rows:
            # print(row) 
            self.tree.insert("", END, values=row)        
            conn.close()


if __name__=="__main__":
    main()

