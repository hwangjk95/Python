from tkinter import *
from tkinter import messagebox

def getNumber():
    opr1 = etOpr1.get().strip()
    opr2 = etOpr2.get().strip()
    if not opr1 or not opr2:
        messagebox.showinfo("경고","두 숫자는 반드시 넣어!")
        return None
    else:
        try:
            opr1 = float(opr1)
            opr2 = float(opr2)
            return opr1, opr2
        except:
            messagebox.showinfo("경고","반드시 숫자를 넣어!")
            return None
        
def setresult(data):
    etResult.delete(0,END)
    etResult.insert(0,data)
    
def doadd():
    oprs = getNumber()
    result = ""
    if oprs:
        result = f"{oprs[0]+oprs[1]}" #oprs는 튜플
    setresult(result)
        
def dosub():
    oprs = getNumber()
    result = ""
    if oprs:
        result = f"{oprs[0]-oprs[1]}" #oprs는 튜플
    setresult(result)
def domul():
    oprs = getNumber()
    result = ""
    if oprs:
        result = f"{oprs[0]*oprs[1]}" #oprs는 튜플
    setresult(result)
def dodiv():
    oprs = getNumber()
    result = ""
    if oprs:
        result = f"{oprs[0]/oprs[1]}" #oprs는 튜플
    setresult(result)

w = Tk()
lbTitle1 = Label(w, text="숫자1")
lbTitle2 = Label(w, text="숫자2")

etOpr1=Entry(w, width=10)
etOpr2=Entry(w, width=10)
etResult = Entry(w)

btAdd = Button(w, text="+", width=4, command=doadd)
btSub = Button(w, text="-", width=4, command=dosub)
btMul = Button(w, text="*", width=4, command=domul)
btDiv = Button(w, text="/", width=4, command=dodiv)

lbTitle1.grid(row= 0 , column=0, columnspan=2)
etOpr1.grid(row=0, column=2, columnspan=2)

lbTitle2.grid(row= 1 , column=0, columnspan=2)
etOpr2.grid(row=1, column=2, columnspan=2)

btAdd.grid(row=2, column=0)
btSub.grid(row=2, column=1)
btMul.grid(row=2, column=2)
btDiv.grid(row=2, column=3)

etResult.grid(row=3, column=0, columnspan=4)

w.mainloop()