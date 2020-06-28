from tkinter import *
import tkinter.ttk as ttk
import serial

window = Tk()
window.geometry('480x300')
window.title("Программа управления")
window.resizable(False, False)

txtX = 0
txtY = 1


def mhome():
    outText.insert(END, 'Home\n')


def mleft():
    outText.insert(END, 'Left_'+steps.get()+'\n')


def mright():
    outText.insert(END, 'Right_'+steps.get()+'\n')


def mdown():
    outText.insert(END, 'Down_'+steps.get()+'\n')


def mup():
    outText.insert(END, 'Up_'+steps.get()+'\n')


def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


# for variables
steps = StringVar()


# first frame with command panel
frameCmm = ttk.LabelFrame(window, text="Main")
prt_lb = Label(frameCmm, text="Set port")
port_Comb = ttk.Combobox(frameCmm, values=serial_ports())
sep1 = ttk.Separator(frameCmm, orient=HORIZONTAL)
btnUp = Button(frameCmm, text="Up", command=mup)
btnHome = Button(frameCmm, text="Home", command=mhome)
btnDown = Button(frameCmm, text="Down", command=mdown)
btnLeft = Button(frameCmm, text="Left", command=mleft)
btnRight = Button(frameCmm, text="Right", command=mright)
sep2 = ttk.Separator(frameCmm, orient=HORIZONTAL)
stpLb = Label(frameCmm, text="Steps")
stpInp = Entry(frameCmm, width=4, textvariable=steps)
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
