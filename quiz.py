from tkinter import *
import random
import tkinter.messagebox
import time as t
from cProfile import label
import sqlite3 as sq
win=Tk()
win.config(background="#ffffff")
win.geometry('520x476')

conn = sq.connect('mcqd.db')
cursor=conn.cursor()
score=0
rem='---'




questions=[ """What is output for: -'raining'. find('z') ?""",
   """How can we swap two numbers a = 10, b = 20 in python without using third variable?""",
   """Pylab is a package that combine _______,________&______ into a single namespace.""",
   """Which method is used to display a warning message in Python?""",
   """Which code can be used as an input dialog named ''Is this a character? ''""",
   """ We can create an image in canvas. Select the option to do so?""",
   """How are keyword arguments specified in the function heading?""",
   """What is the output of the code shown below?
def f1():
    x=100
    print(x)
x=+1
f1()""",
   "What happens if a local variable exists with the same name as the global variable you want to access?",
   """What is the output of the code shown below?

l1=[1, 2, 3, [4]]
l2=list(l1)
id(l1)==id(l2)""",]

option=[
        ["Type error","       ' '       ","       -1       ","  Not found" ],
        ["a = b ,b = a","  a,b = b,a  "," both a & b "," b = a,a = b " ],
        [" Numpy, scipy & matplotlib    "," Numpy, matplotlib & pandas"," Numpy, pandas & matplotlib"," Numpy, scipy & pandas        " ],
        [" Tkinter.message.showmessage('message here')     "," Tkinter.message.sshowwarning('message here')    "," Tkinter.messagebox.showwarning('message here')"," Tkinter.messagebox.showmessage('message here')" ],
        [" Tkinter.messagebox.showinfo(''showinfo'' , ''Is this a character? '')                "," Tkinter.messagebox.askyesno(''askyesno'' , ''Is this a character? '')                "," Tkinter.messagebox.showerror(''showerror'' , ''Is this a character? '')            "," Tkinter.messagebox.showwarning(''showwarning'' , ' 'Is this a character? '')" ],
        [" Image = PhotoImage(imagefilename)       "," Canvas.create_image(filename)                "," Image = Photoimage(file=imagefilename)"," Image = Photoimage(imagefilename)        " ],
        [" one star followed by a valid identifier           ","one underscore followed by a valid identifier","two stars followed by a valid identifier           ","two underscores followed by a valid identifier" ],
        [" Error "," 100   "," 101   "," 99    " ],
        [" Error                                            "," The local variable is shadowed  "," Undefined behavior                     ","  The global variable is shadowed"  ],
        [" True                  "," False                 "," Error                  "," Address of l1     " ],
        ]

ans = [2,2,0,2,1,2,2,1,3,1]

user_ans=[]
#global index
index = []
#print(index)
def exit():
    win.destroy()

def rank():
    global score,rem
    #win.geometry('600x410')
    if score==0:
        rem='Fail'
    elif score>0 and score<=30:
        rem='Average'
    elif score>30 and score<=60:
        rem='Good'
    elif score>60 and score<=100:
        rem='Excellent'    
    else:
        rem='not applicable'
    cursor.execute('UPDATE mcqdata SET Score=?,Remark=? WHERE Remark=?;',(score,rem,"---"))
    conn.commit()

    def check():
        cursor.execute('SELECT * FROM mcqdata ORDER BY Score DESC ;')
        f=cursor.fetchall()
        lstbx.delete(0,END)
        y=0
        j=1
        l='RANK'
        q='->'
        u='NAME'
        t='COURSE'
        v='SCORE'
        g='REMARKS'
        h='-'
        p=','
        for x in f:
            i=list(f[y])
            i.insert(0,l)
            i.insert(1,j)
            i.insert(2,q)
            i.insert(3,u)
            i.insert(4,h)
            i.insert(6,p)
            i.insert(7,t)
            i.insert(8,h)
            i.insert(10,p)
            i.insert(11,v)
            i.insert(12,h)
            i.insert(14,p)
            i.insert(15,g)
            i.insert(16,h)
            lstbx.insert(END,i)
            y+=1
            j+=1
    leadlb=Label(
        win,
        text="LeaderBoard",
        font=('roboto',36,'bold'),
        background="#ffffff"
        )
    leadlb.pack(pady=10)
    lstbx=Listbox(
        win,
        height=15,
        width=70,
        font=("",10,'bold'),
        border=3,
        )
    lstbx.pack(pady=10)
    chkbtn=Button(
        win,
        text='Check Rank',
        width=20,
        command=check
         )
    #chkbtn.pack(pady=10)
    exitbtn=Button(
        win,
        text="EXIT",
        width=30,
        background="#ff3300",
        foreground="#ffffff",
        command=exit,
        border=5,
        font=("",14,'bold'),
    )
    exitbtn.place(x = 200, y = 400, width=120, height=35)
    check()
    


def dele1():
    global lastlb,scorelb,rankbtn,lstbx,exitbtn,labelimage1
    lastlb.destroy()
    scorelb.destroy()
    rankbtn.destroy()
    exitbtn.destroy()
    labelimage1.destroy()
    rank()
#    leaderboard()




def showresult(score):
    #global tscore
    global lastlb,scorelb,rankbtn,exitbtn,image1
    global labelimage1
    queslbl.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    nextbtn.destroy()

#     image1=PhotoImage(file="techquiz1.png")
    labelimage1=Label(
        win,
        image=image1,
        background="#ffffff"
    )
   

    labeltext=Label(
        win,
        text=" TECHNICAL QuizZ",
        font=("forte",18,"bold"),
        background="#ffffff",
    )

    labeltext.pack()
    labelimage1.pack()
    
    lastlb=Label(
        win,
        text="""THANK YOU 
        for playing""",
        font=("open sans",16,"bold"),
        background="#ffffff",
    )   
    scorelb=Label(
        win,
        text="Your Score Is : "+str(score),
        font=("open sans",28,"bold"),
        background="#ffffff"
    )
    scorelb.pack()

    rankbtn=Button(
        win,
        text="My Rank",
        width=30,
        background="#ffffff",
        command=dele1,
        border=5,
        font=("",12,'bold'),
    )
    exitbtn=Button(
        win,
        text="EXIT",
        width=30,
        background="#ff3300",
        foreground="#ffffff",
        font=("",14,'bold'),
        command=exit,
        border=5,
    )
   # lastlb.pack()
    scorelb.pack()
    rankbtn.place(x = 100, y = 360, width=120, height=35)
    exitbtn.place(x = 280, y = 360, width=120, height=35)
def calc():
    global indexes,user_ans,ans
    x = 0
    global score 
    score=0
    for i in index:
        if user_ans[x] == ans[i]:
            score = score + 10
        x += 1
    showresult(score)

ques=1
def selected():
    global radiovar
    global user_ans
    global queslbl
    global r1,r2,r3,r4
    global ques
    global index
    global user_ans

    x=radiovar.get()
    user_ans.append(x)
    radiovar.set(-1)
    #print(user_ans)
    if ques<10:
        queslbl.config(text=questions[index[ques]])
        r1['text']=option[index[ques]][0]
        r2['text']=option[index[ques]][1]
        r3['text']=option[index[ques]][2]
        r4['text']=option[index[ques]][3]
        ques+=1
    else:
        calc()
    

index = []
def start():
    global queslbl
    global r1,r2,r3,r4
    global index
    global nextbtn
    while(len(index) < 10):
        x = random.randint(0,9)
        #print(x)
        if x in index:
            continue
        else:
            index.append(x)
    #print(index)

    queslbl=Label(
        win,
        text = questions[index[0]],
        font=("consola",18,'bold'),
        width=500,
        justify=CENTER,
        wraplength=400,
        background="#ffffff"
    )
    queslbl.pack(pady=10)
    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)
    
    r1=Radiobutton(
        win,
        text = option[index[0]][0],
        value=0,
        variable=radiovar,
        justify=LEFT,
        font=("consola",10,'bold'),
        #command=selected
        background="#ffffff"
        )
    r1.pack(pady=5)
    
    r2=Radiobutton(
        win,
        text=option[index[0]][1],
        value=1,
        variable=radiovar,
        font=("consola",10,'bold'),
        justify=LEFT,
        #command=selected
        background="#ffffff"
        )
    r2.pack(pady=5)

    r3=Radiobutton(
        win,
        text=option[index[0]][2],
        value=2,
        variable=radiovar,
        font=("consola",10,'bold'),
        justify=LEFT,
        #command=selected
        background="#ffffff"
        )
    r3.pack(pady=5)

    r4=Radiobutton(
        win,
        text=option[index[0]][3],
        value=3,
        variable=radiovar,
        font=("consola",10,'bold'),
        justify=LEFT,
        background="#ffffff"
        #command=selected
        )
    r4.pack(pady=5)
    
    nextbtn=Button(
        win,
        text="Next",
        command=selected,
        width=15,
    font=(' ', 12 ,'bold'),
    background="#5DADE2",
    foreground="#ffffff",
    border=5,
    )
    nextbtn.pack(pady=20)

#===============================================================================================================================
def next1():
    global labelimage,labeltext,ruleslabel,infolb,srtbtn
    
    infolb=Label(
        win,
        text="""Read The Rules And 
        Click Start When You are Ready""",
        background="#ffffff",
        font=("roboto",16,"bold"),
        justify=CENTER,
        )
    infolb.pack(pady=5)

    srtbtn=Button(
        win,
        text="START ",
        width=15,
        height=1,
        font=(" ",10,"bold"),
        command=Destroy,
        background="#2ECC71",
        foreground="#ffffff",
        border=5,
        )
    srtbtn.pack(pady=20)
    ruleslabel=Label(
        win,
        text="""Rules:-
        1.The questions shall be in the form of multiple choice.
        2.You will get 20 seconds to solve a question
        3.Once you select a radio button that will be the final choice.
        4.Each correct answer grant you 10 points. """,
        background="#000000",
        foreground="#ffffff",
        font=("roboto", 12,"bold"),
        justify=LEFT,
        )
    ruleslabel.pack(fill=BOTH)
#===============================================================================================================================
def Destroy():
    global labelimage,labeltext,ruleslabel,infolb,srtbtn
    labelimage.destroy()
    labeltext.destroy()
    ruleslabel.destroy()
    infolb.destroy()
    srtbtn.destroy()
    start()
    
def add():
    global rem
    name=var.get()
    cou=var1.get()
    res=0
    cursor.execute('INSERT INTO mcqdata VALUES(?,?,?,?);',(name,cou,res,rem))  
    conn.commit()

def dele():
    entrlbl.destroy()
    namelb.destroy()
    agelb.destroy()
    namentry.destroy()
    ageentry.destroy()
    savebtn.destroy()
    nextbtn1.destroy()
    next1()
           
#===============================================================================================================================
global labelimage

image1=PhotoImage(file="tech-quiz.png")
labelimage=Label(
    win,
    image=image1,
    background="#ffffff"
)
    

labeltext=Label(
    win,
    text=" TECHNICAL QuizZ",
    font=("forte",18,"bold"),
    background="#ffffff",
)

#labeltext.pack()
labelimage.pack(pady=10)

entrlbl=Label(
    win,
    text="Enter Your Information Techie ",
    font=('',18,'bold'),
    background="#ffffff",
    relief="solid",
    )
entrlbl.pack()   
namelb=Label(
    win,
    text="Name:",
    font=('',15,'bold'),
    background="#ffffff",
    )
#namelb.pack()
agelb=Label(
    win,
    text="Course:",
    font=('',15,'bold'),
    background="#ffffff",
    )
#agelb.pack()
     
var=StringVar()
namentry=Entry(
    win,
    text=var,
    font=('roboto', 12 ,'bold'),
    background="#FCF3CF",
    border=4,
    )

    
var1=StringVar()
ageentry=Entry(
    win,
    text=var1,
    #background="#ffffff",
    border=4,
    background="#FCF3CF",
    font=('roboto', 12 ,'bold'),
    )

 
savebtn=Button(
    win,
    text='Save',
    width=15,
    command=add,
    font=(' ', 12 ,'bold'),
    background="#2ECC71",
    foreground="#ffffff",
    border=5,
    )

    
nextbtn1=Button(
    win,
    text='Next',
    width=15,
    height=10,
    command=dele,
    font=(' ', 12 ,'bold'),
    background="#5DADE2",
    foreground="#ffffff",
    border=5,
    )
namelb.place(x = 100, y = 290, width=120, height=25)
namentry.place(x = 200, y = 290, width=140, height=25)
agelb.place(x = 100, y = 330, width=120, height=25) 
ageentry.place(x = 200, y = 330, width=140, height=25)
savebtn.place(x = 100, y = 390, width=120, height=35)
nextbtn1.place(x = 280, y = 390, width=120, height=35)
#==============================================================================================================================


win.mainloop()