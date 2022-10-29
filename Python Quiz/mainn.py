from tkinter import*
import random

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


def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0, 9)
        # if x not in indexes:
        #     indexes.append(x)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    questionlabel.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    labelimg = Label(
        root,
        bg="white",
        border=0
    )
    labelimg.pack()

    labelresulttext = Label(
        root,
        font=("Arial", 20),
        bg="white"
    )
    labelresulttext.pack()

    if score >= 20:
        # img = PhotoImage(file="image.png")
        # labelimg.configure(image=img)
        # labelimage.image = img
        labelresulttext.configure(
            text="You did excellent !!!!!\n\n you got "
        )

    elif score < 20 or score >= 10:
        # img = PhotoImage(file="image.png")
        # labelimg.configure(image=img)
        # labelimage.image = img
        labelresulttext.configure(
            text="You can do better !!!!!\n\n you got "
        )

    elif score < 10:
        # img = PhotoImage(file="image.png")
        # labelimg.configure(image=img)
        # labelimage.image = img
        labelresulttext.configure(
            text="you should work hard !!!!!\n\n you got "
        )


def calc():
    global indexes, user_ans, answers
    x1 = 0
    score = 0
    for i in indexes:
        # print("temp = ", x1)
        if user_ans[x1] == answers[i]:
            score += 5
        x1 += 1
    # print("score = ", score)
    showresult(score)


count = 1


def selected():
    global radiovar, user_ans, questionlabel, r1, r2, r3, r4, count
    x = radiovar.get()
    # here x will get the value which user choose as input
    # print(x)
    user_ans.append(x)
    radiovar.set(-1)
    if count < 5:
        questionlabel.config(text=questions[indexes[count]])
        r1['text'] = choice_ans[indexes[count]][0]
        r2['text'] = choice_ans[indexes[count]][1]
        r3['text'] = choice_ans[indexes[count]][2]
        r4['text'] = choice_ans[indexes[count]][3]
        count += 1
    else:
        print(indexes)
        print(user_ans)
        calc()


def start_Q():
    global questionlabel, r1, r2, r3, r4
    questionlabel = Label(
        root,
        # text="Sample Question which can be too long it will be in next line due to wrap length",
        text=questions[indexes[0]],
        font=("Arial", 16),
        width=500,
        justify="center",
        wraplength=400,
        bg="white",
    )
    questionlabel.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    # by setting radio var -1 it will not check any option automatically

    r1 = Radiobutton(
        root,
        text=choice_ans[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        bg="white",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=choice_ans[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        bg="white",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=choice_ans[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        bg="white",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=choice_ans[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        bg="white",
    )
    r4.pack(pady=5)


def Easy():
    labelinst.destroy()
    labelinstr.destroy()
    # img1label.destroy()
    txtlabel.destroy()
    E_button.destroy()
    M_button.destroy()
    H_button.destroy()
    gen()
    start_Q()


def Medium():
    labelinst.destroy()
    labelinstr.destroy()
    # img1label.destroy()
    txtlabel.destroy()
    E_button.destroy()
    M_button.destroy()
    H_button.destroy()
    gen()
    start_Q()


def Hard():
    labelinst.destroy()
    labelinstr.destroy()
    # img1label.destroy()
    txtlabel.destroy()
    E_button.destroy()
    M_button.destroy()
    H_button.destroy()
    gen()
    start_Q()


root = Tk()
# this is for a single window program in which we are going to destroy the previous things and create new things
# in multi window whole previous window is destroyed and new window is created

root.title("Quiz")
root.geometry('700x600')
root.config(bg="white")
root.resizable(0, 0)

# img1 = PhotoImage(file="terentula nebula.png")
# img1label = Label(root, image=img1, bg="white")
# img1label.pack(paddy = (40,0))

txtlabel = Label(
    root,
    text="Python Quiz",
    font=("Arial", 30, "bold"),
    bg="white"

)
txtlabel.pack(pady=(30, 50))


# img2 = PhotoImage(file="file name")

labelinst = Label(
    root,
    text="Instructions\n",
    font=(
        "Arial", 20),
    bg="white",
    justify="center"
)
labelinst.pack(pady=(10, 0))

labelinstr = Label(
    root,
    text="points",
    width=100,
    font=("Arial", 15),
    bg="black",
    foreground="yellow"
)
labelinstr.pack(pady=(0, 30))

# use image=img1 in place of text in button
E_button = Button(
    root,
    text="Easy",
    relief=FLAT,
    command=Easy
)
E_button.pack(pady=(0, 30))


M_button = Button(
    root,
    text="Medium",
    relief=FLAT,
    command=Medium
)
M_button.pack(pady=(0, 30))


H_button = Button(
    root,
    text="Hard",
    relief=FLAT,
    command=Hard
)
H_button.pack(pady=(0, 30))


root.mainloop()
