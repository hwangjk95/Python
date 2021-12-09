from tkinter import *
from tkinter import messagebox
from car import Car

# 차량등록:
# 엔트리에서 차 번호를 가져온다
# -입력이되었나?
# -그렇다면 기존에 있는 차량인가?

# 차량 번호를 이용해서 생성한다.
# ex) Car('차량번호')
# 생성한 Car인트턴스는 전체관리를 위해 list등에 보관한다.


def getNumber(): #엔트리에 있는 번호 받아오기
    Num=etNum.get().strip()
    if not Num:
        messagebox.showinfo("경고","차량번호를 넣어주세요")
    return Num

def searchNumber(): #carlist 에 있는 차량인지 찾아본다.
    for car in carlist:
        if car.

def doin(): #carlist에 Num을 추가하고 입고시킨다.
    pass

def doout(): #출고시킨다 (out 시키고 carlist에서 제거한다.)
    pass

def gettime():
    pass

def getprice():
    pass


carlist=[]

w = Tk()

lbNum = Label(w, text="차량번호", )
lbNum.grid(row= 0 , column=0 ,columnspan=1 )

etNum=Entry(w, width=20)
etNum.grid(row=0, column = 1, columnspan=3)

btIn = Button(w, text="차량입고", width=8, command=None)
btOut = Button(w, text="차량출고", width=8, command=None)
btTime = Button(w, text="보관시간", width=8, command=None)
btCheck = Button(w, text="요금조회", width=8, command=None)

btIn.grid(row=1, column=0)
btOut.grid(row=1, column=1)
btTime.grid(row=1, column=2)
btCheck.grid(row=1, column=3)

lbResult = Label(w, text="", height = 10)
lbResult.grid(row =2, column=0,columnspan=4)


w.mainloop()