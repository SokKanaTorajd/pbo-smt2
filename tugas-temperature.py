from tkinter import *
from tkinter import ttk

tmprt = Tk()
tmprt.configure(background = "light blue")
tmprt.title("Convert Temperature")

mainframe = ttk.Frame(tmprt, padding = "")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

## Calculation

def Fahrenheit(*args):
    try:
       product.set(round((float(num1.get())*float(1.8)) + float(32),2))
    except ValueError:
        pass

def Reamur(*args):
    try:
        #product2.set(round(float(4/5)*float(num1.get()),2))
        product2.set(round(float(4/5)*float(num2.get()),2))
    except ValueError:
        pass

def Kelvin(*args):
    try:
        #product3.set(round(float(num1.get())+float(273),2))
        product3.set(round(float(num3.get())+float(273),2))
    except ValueError:
        pass

## variables

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
product = DoubleVar()
product2 = DoubleVar()
product3 = DoubleVar()

#display

ttk.Label(mainframe, text="Celcius Degree\t:").grid(column = 1, row = 1)
num1_entry = ttk.Entry(mainframe, width=4, textvariable=num1)
num1_entry.grid(column = 2, row = 1)
num1_entry.bind('<KeyPress>', Fahrenheit)
num1_entry.bind('<KeyRelease>', Fahrenheit)
ttk.Label(mainframe, text = "Fahrenheit Degree:").grid(column = 1, row = 2)
ttk.Label(mainframe, textvariable=product).grid(column = 2, row = 2)

ttk.Label(mainframe, text="Celcius Degree\t:").grid(column = 1, row = 3 )
num2_entry = ttk.Entry(mainframe, width=4, textvariable=num2)
num2_entry.grid(column = 2, row = 3)
num2_entry.bind('<KeyPress>',Reamur)
num2_entry.bind('<KeyRelease>',Reamur)
ttk.Label(mainframe, text = "Reamur Degree\t:").grid(column = 1,row = 4)
ttk.Label(mainframe, textvariable=product2).grid(column = 2, row =  4)

ttk.Label(mainframe, text="Celcius Degree\t:").grid(column = 1, row = 5)
num3_entry = ttk.Entry(mainframe, width=4, textvariable=num3)
num3_entry.grid(column = 2, row = 5)
num3_entry.bind('<KeyPress>', Kelvin)
num3_entry.bind('<KeyRelease>', Kelvin)
ttk.Label(mainframe, text = "Kelvin Degree\t:").grid(column =  1, row= 6 )
ttk.Label(mainframe, textvariable = product3).grid(column =  2, row = 6)

tmprt.mainloop()