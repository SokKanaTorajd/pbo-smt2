from tkinter import *
import tkinter as tk
from functools import partial
from tkinter import ttk

def fungsitampilharga(labelTampilHarga, pilihmenumakanan):
    menumakanan = pilihmenumakanan.get()
    if menumakanan == "sapo Tahu":
        harga = 22000
    elif menumakanan == "Kailan Ham Jamur":
        harga = 35000
    elif menumakanan == "Burger Vegetarian":
        harga = 15000
    labelTampilHarga.config(text=harga)
    return menumakanan

def masukanporsi(harga, bayar, labelTampilKembalian):
    tampungHarga = int(harga.cget("text"))
    bayarOk = int(bayar.get())
    kembalian = bayarOk-tampungHarga
    labelTampilKembalian.config(text=kembalian)
    return tampungHarga

root = tk.Tk()
root.geometry('400x250+500+200')
root.option_add('*font',('Verdana', 10, 'normal'))
root.option_add('*Label.font', ('Verdana', 10, 'bold'))
root.title('Restoran Vegetarian')

pilihmenumakanan = tk.StringVar()
bayar = tk.StringVar()

labelpilihmenumakanan = tk.Label(root, text="Pilih menu makanan")
labelHarga = tk.Label(root, text="Harga")
labelTampilHarga = tk.Label(root)
labelBayar = tk.Label(root, text="Bayar")
labelKembalian = tk.Label(root, text="Kembalian")
labelTampilKembalian = tk.Label(root)
combopilihmenumakanan = ttk.Combobox(root, values=["Sapo Tahu","Kailan Ham Jamur","Burger Vegetarian"], textvariable=pilihmenumakanan)

# combopilihmenumakanan.current(0)

tampilHarga = partial(fungsitampilharga, labelTampilHarga, pilihmenumakanan)
tombolHarga = tk.Button(root, text="Tampilkan Harga", command=tampilHarga)
tombolHarga.configure(bg="#375217", fg="#FFFF00")
bayar = tk.Entry(root, textvariable=bayar, width=22)
inputBayar = partial(fungsitampilharga, labelTampilHarga, bayar, labelTampilKembalian)
tombolBayar = tk.Button(root, text="Bayar", command=inputBayar)
tombolBayar.configure(bg="#FFF000", fg="#AADDFF")


labelpilihmenumakanan.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky="W")
combopilihmenumakanan.grid(row=0, column=1, padx=(10,10), pady=(10,10))
labelHarga.grid(row=2, column=0, padx=(10,10), pady=(0,10), sticky="W")
labelTampilHarga.grid(row=2, column=1, padx=(10,10), pady=(0,10), sticky="W")
tombolHarga.grid(row=1, column=1, sticky="WE", padx=(10,10), pady=(0,10))
labelBayar.grid(row=3, column=0, padx=(10,10), pady=(0,10), sticky="W")
bayar.grid(row=3, column=1, padx=(10,10), pady=(0,10), sticky="W")
labelKembalian.grid(row=5, column=0, padx=(10,10), pady=(0,10), sticky="W")
labelTampilKembalian.grid(row=5, column=1, padx=(10,10), pady=(0,10), sticky="W")
tombolBayar.grid(row=4, column=1, sticky="WE", padx=(10,10), pady=(0,10))


root.mainloop()