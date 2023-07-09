from RS485 import *
import serial.tools.list_ports
from tkinter import *

input = ["0106000000FF"]

rs485 = RS485(input)

# if rs485.getPort() != "None":
#     ser = serial.Serial(port=rs485.getPort(), baudrate=9600)
a = Tk()
a.title("Bản điều khiển")
a.geometry('700x500')
name = Label(a, font = ('Arial', 14), text = 'Bật relay 1 ',bg = 'red')
name.place(x = 30,y = 30)
but = Button(a, text = 'Bật', width = 5, height = 1, bg = 'blue', fg = 'white', font = ('Arial', 14))
but.place(x = 250,y = 25)
a.mainloop()
