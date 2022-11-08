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


if __name__ == '__main__':
    main()
