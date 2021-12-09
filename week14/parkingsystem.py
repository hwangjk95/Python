from tkinter import *
from tkinter import messagebox
from car import Car
from datetime import datetime
import os
import common as cm

def isfile(filename):
    return os.path.isfile(filename)

def isbasefolder():
    return os.path.isdir(cm.curpath)

def makebasefolder():
    if not isbasefolder():
        os.mkdir(cm.curpath)

def carfilename(car):
    return cm.curpath + "/" +car.number + ".txt"

def existcarfilenames():
    return [cm.curpath + "/" +file for file in os.listdir(cm.curpath)]
    # 위 코드는 다음과 같다
    # list = []
    # for file in os.listdir(cm.curpath):
    #     list.append(cm.curpath + "/" + file)
    # return list

def writefile(car):
    makebasefolder()
    filename = carfilename(car)
    with open(filename, 'w')as f:
        f.write(car.filecontent())

def deletefile(car):
    filename = carfilename(car)
    if isfile(filename):
        os.remove(filename)

def readfile():
    if isbasefolder():
        filelist = existcarfilenames()
        for file in filelist:
            with open(file,'r') as f:
                lines = f.readlines()
                if len(lines)==2:
                    try:
                        number = lines[0].strip()
                        intime = lines[1].strip()
                        intime = datetime.strptime(intime, cm.datetimeformat) #문자열을 시간으로 바꿔주는 거
                        car = Car(number, intime)
                        carlist.append(car)
                    except:
                        continue



def getnumber():
    number = etNumber.get().strip()
    if not number:
        messagebox.showinfo("안내", "차량 번호를 넣어주세요.")
        return None
    else:
        return number

def searchnumber(number):
    for car in carlist:
        if car.number == number:
            return car
    return None

def doin():
    number = getnumber()
    if number:
        car = searchnumber(number);
        if None != car:
            messagebox.showinfo("안내", "이미 입고한 차량입니다.")
        else:
            car = Car(number)
            carlist.append(car)
            writefile(car)
            messagebox.showinfo("안내", number +" 입고 완료했습니다.")

def doout():
    number = getnumber()
    if number:
        car = searchnumber(number);
        if None == car:
            messagebox.showinfo("안내", "입고한 차량이 아닙니다.")
        else:
            car.out()
            message = f"차량번호:{car.number}\n" \
                      f"입고시간:{car.intime}\n" \
                      f"출고시간:{car.outtime}\n" \
                      f"총 보관 시간:{car.gettime()}\n" \
                      f"총 보관 요금:{car.calprice()}\n"
            lbResult.config(text=message)
            carlist.remove(car)
            deletefile(car)

def gettime():
    number = getnumber()
    if number:
        car = searchnumber(number);
        if None == car:
            messagebox.showinfo("안내", "입고한 차량이 아닙니다.")
        else:
            messagebox.showinfo("안내", f"현재까지 {car.gettime()}분 보관했습니다.")

def getprice():
    number = getnumber()
    if number:
        car = searchnumber(number);
        if None == car:
            messagebox.showinfo("안내", "입고한 차량이 아닙니다.")
        else:
            messagebox.showinfo("안내", f"현재까지의 보관요금은 {car.calprice()}원 입니다.")

carlist=[]

readfile()

w = Tk()

lbTitle = Label(w, text="차량번호")
etNumber = Entry(w)
btIn    = Button(w, text="차량입고", width=8, command=doin)
btOut   = Button(w, text="차량출고", width=8, command=doout)
btTime  = Button(w, text="보관시간", width=8, command=gettime)
btPrice = Button(w, text="요금조회", width=8, command=getprice)
lbResult = Label(w, text="", height="10")

lbTitle.grid(row=0, column=0)
etNumber.grid(row=0, column=1, columnspan=3)
btIn.grid(row=1, column=0)
btOut.grid(row=1, column=1)
btTime.grid(row=1, column=2)
btPrice.grid(row=1, column=3)
lbResult.grid(row=2, column=0, columnspan=4)

w.mainloop()