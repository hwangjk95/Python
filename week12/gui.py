from tkinter import *
from tkinter import messagebox

def myname():
    messagebox.showinfo("너의 이름은",etname.get())


w = Tk()

lb1=Label(w,text="인천광역시")
lb2=Label(w,text="미추홀구",font=("궁서체",30),fg="red")
lb3=Label(w,text="용현동", bg="yellow",width=20, height=4, anchor=CENTER)
etname=Entry(w)
btclick=Button(w,text="클릭!!!",fg="blue",command=myname)

lb1.pack()
lb3.pack()
lb2.pack()
etname.pack()
btclick.pack()

w.mainloop()
