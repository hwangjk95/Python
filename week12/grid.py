from tkinter import *

mw = Tk()

lbF=Label(mw, text="화씨")
lbC=Label(mw, text="섭씨")

etF = Entry(mw)
etC = Entry(mw)

frButton =Frame(mw) #컨테이너

btFtoC = Button(frButton, text="화씨->섭씨")
btCtoF = Button(frButton, text="섭씨->화씨")

lbF.grid(row=0, column=0)
lbC.grid(row=1, column=0)

etF.grid(row=0, column=1)
etC.grid(row=1, column=1)

frButton.grid(row=2, column=1)
btFtoC.grid(row=0, column=0)
btCtoF.grid(row=0, column=1)

mw.mainloop()