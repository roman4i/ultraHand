from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.geometry('480x300')
window.title("Программа управления")
window.resizable(False, False)

# first frame with command panel
frameCmm = ttk.LabelFrame(window, text="Main")
prt_lb = Label(frameCmm, text="Set port")
port_listArr = ["Com1", "Com2", "Com3"]
port_Comb = ttk.Combobox(frameCmm, values=port_listArr)
sep1 = ttk.Separator(frameCmm, orient=HORIZONTAL)
btnUp = Button(frameCmm, text="Up")
btnHome = Button(frameCmm, text="Home")
btnDown = Button(frameCmm, text="Down")
btnLeft = Button(frameCmm, text="Left")
btnRight = Button(frameCmm, text="Right")
sep2 = ttk.Separator(frameCmm, orient=HORIZONTAL)
stpLb = Label(frameCmm, text="Steps")
stpInp = Entry(frameCmm, width=4)
prt_lb.grid(row=0, column=0, columnspan=3)
port_Comb.grid(row=1, column=0, columnspan=3)
sep1.grid(row=2, column=0, columnspan=3)
btnUp.grid(row=3, column=1)
btnLeft.grid(row=4, column=0)
btnHome.grid(row=4, column=1)
btnRight.grid(row=4, column=2)
btnDown.grid(row=5, column=1)
sep2.grid(row=6, column=0, columnspan=3)
stpLb.grid(row=7, column=0, columnspan=2)
stpInp.grid(row=7, column=2)
frameCmm.grid(row=0, column=0, sticky="n")

# second panel with
textFrm = ttk.LabelFrame(window, text="Commands")
outText = Text(textFrm, height=15, width=40)
outText.pack()
sndBtn = Button(textFrm, text="Send commands")
sndBtn.pack()
textFrm.grid(row=0, column=1)

window.mainloop()
