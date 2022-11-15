from tkinter import*
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import random


class Portal:
    def __init__(self,scn):
        self.scn=scn
        self.scn.geometry("450x500")
        self.scn.resizable(False,False)
        self.scn.title("Quiz")
        background = Image.open("back5.jpg")
        resize_background = background.resize((450, 500))
        bgimg = ImageTk.PhotoImage(resize_background)
        bg1=Label(self.scn,image=bgimg)
        bg1.image=bgimg
        bg1.place(x=0,y=0)

  
        Button(self.scn,text="Register",font="Times 30 bold",bg="red",fg="white",command=self.register_window).pack(pady=40)
        Button(self.scn,text="Login",font="Times 30 bold",bg="red",fg="white",command=self.login_window).pack(pady=40)
        Button(self.scn,text="Leaderboard",font="Times 30 bold",bg="red",fg="white",command=self.leaderboard_window).pack(pady=40) 


    def register_window(self):

        self.scn.destroy()
        screen=Tk()
        Register_window(screen)
        screen.mainloop()


    def login_window(self):
        self.scn.destroy()
        screen=Tk()
        Login_window(screen)
        screen.mainloop()

    def leaderboard_window(self):
        self.lgn_screen=Toplevel(self.scn)
        self.lgn_scn=Leaderboard(self.lgn_screen)

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
        Button(self.screen, text="Already have an account ? Login here",font="50",fg="green",command=self.login_window).place(x=150,y=450)
    
    def login_window(self):
        self.screen.destroy()
        screen=Tk()
        Login_window(screen)
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

class Login_window:
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
        cred=(self.regno,self.passw)
        global rollnumber
        rollnumber=self.regno

        if self.regno=="" or self.passw=="":
            messagebox.showerror("Empty Field!!!","All field are required")
        else:
            conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
            cur=conn.cursor()
            cur.execute("select * from student where rollno=%s and passw=%s",cred)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                self.screenlw.destroy()
                screen=Tk()
                questions(screen)
                screen.mainloop()

class questions:
    def __init__(self , root):
        global txtlabel ,labelinst ,labelinstr ,E_button ,M_button ,H_button
        # this is for a single window program in which we are going to destroy the previous things and create new things
        # in multi window whole previous window is destroyed and new window is created
        self.root = root
        self.root.title("Quiz")
        self.root.geometry('700x600')
        self.root.config(bg="#7876FD")
        self.root.resizable(0, 0)
        self.root.configure(bg='#7876FD')
        
        conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
        ask_cur=conn.cursor()
        ask_query=("select name from student where rollno=%s")
        ask_cur.execute(ask_query,(rollnumber,))
        row=ask_cur.fetchone()
        name=row[0]
        conn.commit()
        conn.close()

        labelinst1 = Label(
            self.root,
            text= name,
            font=("impact",20),
            bg='#20b2aa',
        )
        labelinst1.pack(fill="both")


        txtlabel = Label(
            self.root,
            text="Python Quiz",
            font=("montserrat", 40  , "bold"),
            bg="#7876FD",
            fg='#191835',
        )
        txtlabel.pack(pady=(15,25))
        
        labelinst = Label(
            self.root,
            text="Instructions",
            font=("calibri", 25,"bold"),
            bg="#7876FD",
            justify="center",
            foreground="#fbfd76"
        )
        labelinst.pack()

        labelinstr = Label(
            self.root,
            text="1.Can not jump to previous question\n2.",
            width=100,
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            foreground="#fbfd76"
        )
        labelinstr.pack(pady=(0, 10))

        # Eimg = Image.open("EASYimg.png")
        # EEimg = ImageTk.PhotoImage(Eimg)
        E_button = Button(
            self.root,
            text="Easy",
            font=("impact",20),
            # image=EEimg,
            bg='#7876FD',
            relief=FLAT,
            activebackground="#7876FD",
            command=self.Easy
        )
        # E_button.img = EEimg
        E_button.pack(pady=(0, 30))

        # Mimg = Image.open("MEDimg.png")
        # MMimg = ImageTk.PhotoImage(Mimg)
        M_button = Button(
            self.root,
            text="Medium",
            font=("impact",20),
            # image=MMimg,
            bg="#7876FD",
            relief=FLAT,
            activebackground="#7876FD",
            command=self.Medium
        )
        # M_button.img = MMimg
        M_button.pack(pady=(0, 30))


        # Himg = Image.open("HARDimg.png")
        # HHimg = ImageTk.PhotoImage(Himg)
        H_button = Button(
            self.root,
            text="HARD",
            font=("impact",20),
            # image=HHimg,
            bg="#7876FD",
            relief=FLAT,
            activebackground="#7876FD",
            command=self.Hard
        )
        # H_button.img = HHimg
        H_button.pack(pady=(0, 30))
        
    #EASY QUESTIONS 1-10
    questionsEASY = [
        "Who developed Python Programming Language?",
        "Which type of Programming does Python support?",
        "Which of the following is the correct extension of the Python file?",
        "All keywords in Python are in _________",
        "Which of the following character is used to give single-line comments in Python?",
        "Which of the following functions is a built-in function in python?",
        "Which of the following is not a core data type in Python programming?",
        "What is the maximum length of a Python identifier?",
        "What is output of print(math.pow(3, 2))?",
        "Which of the following is a Python tuple?",
    ]
    #EASY QUESTIONS OPTIONS
    choice_ansEASY = [
        ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
        ["object-oriented program", "structured program", "functional program", "all of the mentioned"],
        [".python", ".pl", ".py", ".p"],
        ["Capitalized", "lower case", "UPPER CASE", "None of the mentioned"],
        ["//", "#", "!", "/*"],
        ["factorial()", "print()", "seed()", "sqrt()"],
        ["Tuples", "Lists", "Class", "Dictionary"],
        ["32", "16", "128", "No fixed length is specified"],
        ["9", "Error", "9.0", "None of the mentioned"],
        ["{1, 2, 3}", "{}", "[1, 2, 3]", "(1, 2, 3)"],
    ]
    
    #MEDIUM QUESTIONS 1-10
    questionsMED = [
        "What is the maximum length of a Python identifier?",
        "Which of the following concepts is not a part of Python?",
        "As what datatype are the *args stored, when passed into a function?",
        "As what datatype are the *kwargs stored, when passed into a function?",
        "What keyword is used in Python to raise exceptions?",
        "Which of the following is not a valid set operation in python?",
        "Which of the following modules need to be imported to handle date time computations in Python?",
        "In which language is Python written?",
        "What will be the result of the following expression in Python “2 ** 3 + 5 ** 2”?",
        "Which of the following are valid string manipulation functions in Python?",
    ]
    #MEDIUM QUESTIONS OPTIONS
    choice_ansMED = [
        ["32", "16", "128", "No fixed length is specified"],
        ["Pointers", "Loops", "Dynamic Typing", "All of the above"],
        ["List", "Tuple", "Dictionary", "None of the above"],
        ["Lists", "Tuples", "Dictionary", "None of the above"],
        ["raise", "try", "goto", "except"],
        ["Union", "Intersection", "Difference", "None of the above"],
        ["datetime", "date", "time", "timedate"],
        ["C++", "C", "Java", "None of these"],
        ["65536", "33", "169", "None of these"],
        ["count()", "upper()", "strip()", "All of the above"],
    ]
    
    #HARD QUESTIONS 1-10
    questionsHARD = [
        "What will be the output of the following code : 'print type(type(int))'",
        "What is the output of the following segment : 'chr(ord('A'))'",
        "What is the output of the following program : \ny = 8\nz = lambda x : x * y\nprint (z(6))",
        "What is called when a function is defined inside a class?",
        "Which of the following concepts is not a part of Python?",
        "Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.pop(1)?",
        "Which of the following are valid string manipulation functions in Python?",
        "Which function overloads the >> operator?",
        "Given a function that does not return any value, what value is shown when executed at the shell?",
        "In which language is Python written?",
    ]
    #HARD QUESTIONS OPTIONS
    choice_ansHARD = [
        ["type 'int'", "type 'type'", "Error", "0"],
        ["A", "B", "a", "Error"],
        ["48", "14", "64", "None of the above"],
        ["Module", "Class", "Another Fuction", "Method"],
        ["Pointers", "Loops", "Dynamic Typing", "All of the above"],
        ["[3, 4, 5, 20, 5, 25, 1, 3]", "[1, 3, 3, 4, 5, 5, 20, 25]", "[3, 5, 20, 5, 25, 1, 3]", "[1, 3, 4, 5, 20, 5, 25]"],
        ["count()", "upper()", "strip()", "All of the above"],
        ["more()", "gt()", "ge()", "None of the above"],
        ["int", "bool", "void", "None"],
        ["C++", "C", "Java", "None of these"],
    ]
    
    # will contain the correct answers of questions
    answersE = [2, 3, 2, 3, 1, 1, 2, 3, 2, 3]
    answersMED = [3, 0, 1, 2, 0, 3, 0, 1, 1, 3]
    answersHARD = [1, 0, 0, 3, 1, 2, 3, 3, 3, 2]
    
    user_ans = []
    indexes = []
    count = 1

    def gen(self):
        while(len(self.indexes) < 10):
            x = random.randint(0, 9)
            if x in self.indexes:
                continue
            else:
                self.indexes.append(x)
    
    def leaderboard_window(self):
        self.root=Toplevel(self.root)
        self.lgn_scn=Leaderboard(self.root)

    def showresult(self,score):
        global questionlabel, labelinst1,r1 ,r2 , r3 , r4
        valinp=(score,rollnumber)
        conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
        ask_cur=conn.cursor()
        ask_query=("select score from student where rollno=%s")
        ask_cur.execute(ask_query,(rollnumber,))
        row=ask_cur.fetchone()
        prev_score=row[0]
        if(prev_score<score):
            cur=conn.cursor()
            query=("update student set score=%s where rollno=%s")
            cur.execute(query,valinp)
            conn.commit()
            conn.close()
        
        questionlabel.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()


        labelimg = Label(
            self.root,
            bg="#7876FD",
            border=0
        )
        labelimg.pack()

        labelresulttext = Label(
            self.root,
            font=("impact", 20),
            bg="#7876FD",
            justify=CENTER,
        )
        labelresulttext.pack(pady=200)

        if score >= 15:
            labelresulttext.configure(
                text="You did excellent !!!!!\n you got " + str(score)
            )

        elif score < 10 or score >= 8:
            labelresulttext.configure(
                text="You can do better !!!!!\n you got " + str(score)
            )

        elif score < 8:
            labelresulttext.configure(
                text="you should work hard !!!!!\n you got " + str(score)
            )

        Button(
            self.root,
            text="Leaderboard",
            font=("calibri", 20,"bold"),
            bg="#7876FD", 
            activebackground="#7876FD",
            command =self.leaderboard_window
        ).place(x=500,y=500)
        return score

    def calc_E(self):
        x1 = 0
        score = 0
        for i in self.indexes:
            if self.user_ans[x1] == self.answersE[i]:
                score += 2
            x1 += 1
        self.showresult(score)
    
    def calc_M(self):
        x1 = 0
        score = 0
        for i in self.indexes:
            if self.user_ans[x1] == self.answersMED[i]:
                score += 3
            x1 += 1
        self.showresult(score)
    
    def calc_H(self):
        x1 = 0
        score = 0
        for i in self.indexes:
            if self.user_ans[x1] == self.answersHARD[i]:
                score += 5
            x1 += 1
        self.showresult(score)
    
    def selectedE(self):
        global questionlabel ,labelinst1,r1 ,r2 , r3 , r4
        x = self.radiovar.get()

        self.user_ans.append(x)
        self.radiovar.set(-1)
        if self.count < 10:
            questionlabel.config(text=self.questionsEASY[self.indexes[self.count]])

            r1['text'] = self.choice_ansEASY[self.indexes[self.count]][0]
            r2['text'] = self.choice_ansEASY[self.indexes[self.count]][1]
            r3['text'] = self.choice_ansEASY[self.indexes[self.count]][2]
            r4['text'] = self.choice_ansEASY[self.indexes[self.count]][3]

            self.count += 1
        else:
            self.calc_E()
    
    def selectedM(self):
        global questionlabel ,labelinst1,r1 ,r2 , r3 , r4
        x = self.radiovar.get()
        self.user_ans.append(x)

        self.radiovar.set(-1)
        if self.count < 10:
            questionlabel.config(text=self.questionsMED[self.indexes[self.count]])
            r1['text'] = self.choice_ansMED[self.indexes[self.count]][0]
            r2['text'] = self.choice_ansMED[self.indexes[self.count]][1]
            r3['text'] = self.choice_ansMED[self.indexes[self.count]][2]
            r4['text'] = self.choice_ansMED[self.indexes[self.count]][3]
            self.count += 1
        else:
            self.calc_M()
    
    def selectedH(self):
        global questionlabel ,labelinst1,r1 ,r2 , r3 , r4
        x = self.radiovar.get()
        self.user_ans.append(x)

        self.radiovar.set(-1)
        if self.count < 10:
            questionlabel.config(text=self.questionsHARD[self.indexes[self.count]])
            r1['text'] = self.choice_ansHARD[self.indexes[self.count]][0]
            r2['text'] = self.choice_ansHARD[self.indexes[self.count]][1]
            r3['text'] = self.choice_ansHARD[self.indexes[self.count]][2]
            r4['text'] = self.choice_ansHARD[self.indexes[self.count]][3]
            self.count += 1
        else:
            self.calc_H()
    
    def start_QE(self):
        global questionlabel ,r1,r2,r3,r4
        questionlabel = Label(
            self.root,
            text=self.questionsEASY[self.indexes[0]],
            font=("Times", 20, "bold"),
            width=500,
            justify="center",
            # text="Sample Question which can be too long it will be in next line due to wrap length",
            wraplength=400,
            bg="#7876FD",
        )
        questionlabel.pack(pady=(100, 30))

    
        self.radiovar = IntVar()
        self.radiovar.set(-1)
        # by setting radio var -1 it will not check any option automatically

        r1 = Radiobutton(
            self.root,
            text=self.choice_ansEASY[self.indexes[0]][0],
            font=("Times", 16),
            value=0,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
            justify=LEFT,
        )
        r1.place(x=150, y=300)

        r2 = Radiobutton(
            self.root,
            text=self.choice_ansEASY[self.indexes[0]][1],
            font=("Times", 16),
            value=1,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r2.place(x=150, y=400)

        r3 = Radiobutton(
            self.root,
            text=self.choice_ansEASY[self.indexes[0]][2],
            font=("Times", 16),
            value=2,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r3.place(x=400, y=300)

        r4 = Radiobutton(
            self.root,
            text=self.choice_ansEASY[self.indexes[0]][3],
            font=("Times", 16),
            value=3,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r4.place(x=400, y=400)

        Button(
            self.root,
            text="NEXT",
            command=self.selectedE,
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            activebackground="#7876FD",

        ).place(x=550,y=500)
    
    def start_QM(self):
        global questionlabel ,r1,r2,r3,r4
        questionlabel = Label(
            self.root,
            # text="Sample Question which can be too long it will be in next line due to wrap length",
            text=self.questionsMED[self.indexes[0]],
            font=("Times", 20, "bold"),
            width=500,
            justify="center",
            wraplength=400,
            bg="#7876FD",
        )
        questionlabel.pack(pady=(100, 30))

    
        self.radiovar = IntVar()
        self.radiovar.set(-1)
        # by setting radio var -1 it will not check any option automatically

        r1 = Radiobutton(
            self.root,
            text=self.choice_ansMED[self.indexes[0]][0],
            font=("Times", 16),
            value=0,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r1.place(x=150, y=300)

        r2 = Radiobutton(
            self.root,
            text=self.choice_ansMED[self.indexes[0]][1],
            font=("Times", 16),
            value=1,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r2.place(x=150, y=400)

        r3 = Radiobutton(
            self.root,
            text=self.choice_ansMED[self.indexes[0]][2],
            font=("Times", 16),
            value=2,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r3.place(x=400, y=300)

        r4 = Radiobutton(
            self.root,
            text=self.choice_ansMED[self.indexes[0]][3],
            font=("Times", 16),
            value=3,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r4.place(x=400, y=400)

        Button(
            self.root,
            text="NEXT",
            command=self.selectedM,
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            activebackground="#7876FD",

        ).place(x=550,y=500)
    
    def start_QH(self):
        global questionlabel ,r1,r2,r3,r4
        questionlabel = Label(
            self.root,
            # text="Sample Question which can be too long it will be in next line due to wrap length",
            text=self.questionsHARD[self.indexes[0]],
            font=("Times", 20, "bold"),
            width=500,
            justify="center",
            wraplength=400,
            bg="#7876FD",
        )
        questionlabel.pack(pady=(100, 30))

    
        self.radiovar = IntVar()
        self.radiovar.set(-1)
        # by setting radio var -1 it will not check any option automatically

        r1 = Radiobutton(
            self.root,
            text=self.choice_ansHARD[self.indexes[0]][0],
            font=("Times", 16),
            value=0,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r1.place(x=150, y=300)

        r2 = Radiobutton(
            self.root,
            text=self.choice_ansHARD[self.indexes[0]][1],
            font=("Times", 16),
            value=1,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r2.place(x=150, y=400)

        r3 = Radiobutton(
            self.root,
            text=self.choice_ansHARD[self.indexes[0]][2],
            font=("Times", 16),
            value=2,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r3.place(x=400, y=300)

        r4 = Radiobutton(
            self.root,
            text=self.choice_ansHARD[self.indexes[0]][3],
            font=("Times", 16),
            value=3,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r4.place(x=400, y=400)

        Button(
            self.root,
            text="NEXT",
            command=self.selectedH,
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            activebackground="#7876FD",

        ).place(x=550,y=500)
    
    def Easy(self):
        labelinst.destroy()
        labelinstr.destroy()
        txtlabel.destroy()
        E_button.destroy()
        M_button.destroy()
        H_button.destroy()
        self.gen()
        self.start_QE()

    def Medium(self):
        labelinst.destroy()
        labelinstr.destroy()
        # img1label.destroy()
        txtlabel.destroy()
        E_button.destroy()
        M_button.destroy()
        H_button.destroy()
        self.gen()
        self.start_QM()

    def Hard(self):
        labelinst.destroy()
        labelinstr.destroy()
        # img1label.destroy()
        txtlabel.destroy()
        E_button.destroy()
        M_button.destroy()
        H_button.destroy()
        self.gen()
        self.start_QH()


class Leaderboard:
    def __init__(self,scn):
        self.scn=scn
        self.scn.geometry("600x300")
        self.scn.resizable(False,False)
        self.scn.title("Leaderboard")
        self.scn.configure(bg="white")


        conn=mysql.connector.connect(host='localhost',password='1234',user='root',database="sys")
        cur=conn.cursor()
        query=("select rollno,name,section,score from student order by score desc")
        cur.execute(query)
        rows=cur.fetchall()
        headings=("RANK","Roll Number","Name","Section","Score")
        for n in range(len(headings)):
            h=Label(self.scn,width=10,font="Times 14 bold",fg="white",text=headings[n],bg="red",)
            h.grid(row=0,column=n)

        i=1
        for student in rows:
            temp=(i,)
            complete=temp+student
            e=Label(self.scn,width=10,fg="blue",text=i,bg="red",font="Times 14 bold")
            for j in range(len(student)+1):
                e=Label(self.scn,width=10,fg="blue",text=complete[j],bg="white",font="Times 14 bold")
                e.grid(row=i,column=j)
            i=i+1
        conn.close()



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



screen=Tk()
Portal(screen)
screen.mainloop()


