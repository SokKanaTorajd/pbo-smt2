from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Pembagian")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

## Calculation

def bagi(*args):
    try:
       product.set(round(float(num1.get())/float(num2.get()),2))
    except ValueError:
        print("inputan harus angka")
    except ZeroDivisionError:
        print("tidak bisa dibagi dengan 0")

## variables

num1 = IntVar()
num2 = IntVar()
product = DoubleVar()

## first number

ttk.Label(mainframe, text="angka pertama:").grid(column = 1, row = 1)
num1_entry = ttk.Entry(mainframe, width=4, textvariable=num1)
num1_entry.grid(column = 2, row = 1)
# num1_entry.bind('<KeyPress>', bagi)
# num1_entry.bind('<KeyRelease>', bagi)

## second number

ttk.Label(mainframe, text="angka kedua:").grid(column = 1, row = 2)
num2_entry = ttk.Entry(mainframe, width=4, textvariable=num2)
num2_entry.grid(column = 2, row = 2)
# num2_entry.bind('<KeyPress>',bagi)
# num2_entry.bind('<KeyRelease>',bagi)

## display results

ttk.Label(mainframe, text = "Product:").grid(column = 1, row = 3)
ttk.Label(mainframe, textvariable=product).grid(column = 2, row = 3)

ttk.Button(mainframe, text = "Hitung",command = bagi).grid(row = 4,columnspan = 2)
ttk.Button(mainframe, text = "Selesai", command = mainframe.quit).grid(row = 5, columnspan = 2 )
root.mainloop()