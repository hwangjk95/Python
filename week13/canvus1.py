from tkinter import *

penWidth = 5 #펜 두께 설정
def dothick():
    global penWidth
    penWidth = 10

def dothin():
    global penWidth
    penWidth = 5

def doclear():
    cv.delete("all")  # delete("all" | "항목명")

def doexit():
    root.destroy()

def dodraw(event):
    global penWidth
    x = event.x  # 마우스 현재 좌표
    y = event.y
    cv.create_oval(x, y, x+1, y+1, width=penWidth) #타원그리기기


root = Tk()
root.title("그림판")
cv = Canvas(root, width=800, height=600, background="lightblue")
cv.pack()

cv.bind("<B1-Motion>", dodraw)
frButtonGroup = Frame(root)
frButtonGroup.pack()

btThick = Button(frButtonGroup, text="두껍게", font="굴림", command=dothick)
btThin = Button(frButtonGroup, text="가늘게", font="굴림", command=dothin)
btClear = Button(frButtonGroup, text="지우기", font="굴림", command=doclear)
btExit = Button(frButtonGroup, text="나가기", font="굴림", command=doexit)

btThick.grid(row=0, column=0)
btThin.grid(row=0, column=1)
btClear.grid(row=0, column=2)
btExit.grid(row=0, column=3)

root.mainloop()
