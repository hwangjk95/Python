#parking.py
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from car import Car
import os
import common as cm
#추가1

# 입고 차량 정보를 저장할 리스트
carlist = []

# 메인 윈도우 생성
w = Tk()

# 필요한 컨트롤(위젯) 생성
lbTitle = Label(w, text="차량번호")
etNumber = Entry(w)
btIn = Button(w, text="차량입고", width=8, command=None)
btOut = Button(w, text="차량출고", width=8, command=None)
btTime = Button(w, text="보관시간", width=8, command=None)
btPrice = Button(w, text="요금조회", width=8, command=None)
lbResult = Label(w, text="", height="10")

# 생성한 컨트롤(위젯) Grid 방식으로 배치
lbTitle.grid(row=0, column=0)
etNumber.grid(row=0, column=1, columnspan=3)
btIn.grid(row=1, column=0)
btOut.grid(row=1, column=1)
btTime.grid(row=1, column=2)
btPrice.grid(row=1, column=3)
lbResult.grid(row=2, column=0, columnspan=4)

# 메인 윈도우 실행
w.mainloop()



