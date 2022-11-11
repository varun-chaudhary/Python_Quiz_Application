from PIL import Image , ImageTk
from tkinter import*
import random

def main():
    root = Tk()
    quiz = questions(root)
    root.mainloop()


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
        # img1 = PhotoImage(file="terentula nebula.png")
        # img1label = Label(self.root, image=img1, bg="#7876FD")
        # img1label.pack(paddy = (40,0))

        labelinst1 = Label(
            self.root,
            text='Hello',
            font=("impact",20,"bold"),
            bg='#20b2aa', #7876FD
            # fg='#4DB1FF',
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
        

        # img2 = PhotoImage(file="file name")

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

        # a = questions()
        # use image=img1 in place of text in button
        Eimg = Image.open("EASYimg.png")
        EEimg = ImageTk.PhotoImage(Eimg)
        E_button = Button(
            self.root,
            text="Easy",
            image=EEimg,
            bg='#7876FD',
            relief=FLAT,
            activebackground="#7876FD",
            command=self.Easy
        )
        E_button.img = EEimg
        E_button.pack(pady=(0, 30))

        Mimg = Image.open("MEDimg.png")
        MMimg = ImageTk.PhotoImage(Mimg)
        M_button = Button(
            self.root,
            text="Medium",
            image=MMimg,
            bg="#7876FD",
            relief=FLAT,
            activebackground="#7876FD",
            command=self.Medium
        )
        M_button.img = MMimg
        M_button.pack(pady=(0, 30))


        Himg = Image.open("HARDimg.png")
        HHimg = ImageTk.PhotoImage(Himg)
        H_button = Button(
            self.root,
            text="HARD",
            image=HHimg,
            bg="#7876FD",
            relief=FLAT,
            activebackground="#7876FD",
            command=self.Hard
        )
        H_button.img = HHimg
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
    answersM = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    answersH = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    user_ans = []
    indexes = []
    count = 1

    def gen(self):
        while(len(self.indexes) < 10):
            x = random.randint(0, 9)
            # if x not in indexes:
            #     indexes.append(x)
            if x in self.indexes:
                continue
            else:
                self.indexes.append(x)

    def showresult(self,score):
        global questionlabel, labelinst1,r1 ,r2 , r3 , r4
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
            # img = PhotoImage(file="image.png")
            # labelimg.configure(image=img)
            # labelimage.image = img
            labelresulttext.configure(
                text="You did excellent !!!!!\n you got " + str(score)
            )

        elif score < 10 or score >= 8:
            # img = PhotoImage(file="image.png")
            # labelimg.configure(image=img)
            # labelimage.image = img
            labelresulttext.configure(
                text="You can do better !!!!!\n you got " + str(score)
            )

        elif score < 8:
            # img = PhotoImage(file="image.png")
            # labelimg.configure(image=img)
            # labelimage.image = img
            labelresulttext.configure(
                text="you should work hard !!!!!\n you got " + str(score)
            )

        Button(
            self.root,
            text="Leaderboard",
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            # relief=FLAT,  
            activebackground="#7876FD",
            #command =
        ).place(x=500,y=500)
        return score

    def calc(self):
        # global indexes, user_ans, answers
        x1 = 0
        score = 0
        for i in self.indexes:
            # print("temp = ", x1)
            if self.user_ans[x1] == self.answers[i]:
                score += 2
            x1 += 1
        # print("score = ", score)
        self.showresult(score)

    def selected(self):
        global questionlabel ,labelinst1,r1 ,r2 , r3 , r4
        x = self.radiovar.get()
        
        # here x will get the value which user choose as input
        # print(x)
        self.user_ans.append(x)
        self.radiovar.set(-1)
        if self.count < 10:
            questionlabel.config(text=self.questions[self.indexes[self.count]])
            r1['text'] = self.choice_ans[self.indexes[self.count]][0]
            r2['text'] = self.choice_ans[self.indexes[self.count]][1]
            r3['text'] = self.choice_ans[self.indexes[self.count]][2]
            r4['text'] = self.choice_ans[self.indexes[self.count]][3]
            self.count += 1
        else:
            # print(self.indexes)
            # print(self.user_ans)
            self.calc()

    def start_Q(self):
        global questionlabel ,r1,r2,r3,r4
        questionlabel = Label(
            self.root,
            # text="Sample Question which can be too long it will be in next line due to wrap length",
            text=self.questions[self.indexes[0]],
            font=("impact", 16),
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
            text=self.choice_ans[self.indexes[0]][0],
            font=("Times", 12),
            value=0,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
            justify=LEFT,
        )
        r1.pack(pady=5)

        r2 = Radiobutton(
            self.root,
            text=self.choice_ans[self.indexes[0]][1],
            font=("Times", 12),
            value=1,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r2.pack(pady=5)

        r3 = Radiobutton(
            self.root,
            text=self.choice_ans[self.indexes[0]][2],
            font=("Times", 12),
            value=2,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r3.pack(pady=5)

        r4 = Radiobutton(
            self.root,
            text=self.choice_ans[self.indexes[0]][3],
            font=("Times", 12),
            value=3,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r4.pack(pady=5)

        Button(
            self.root,
            text="NEXT",
            command=self.selected,
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            activebackground="#7876FD",

        ).place(x=550,y=500)

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


if __name__ == '__main__':
    main()
