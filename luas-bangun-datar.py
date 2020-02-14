###versi 1

# from tkinter import *
# from functools import partial
# import math

# bd = Tk()
# bd.title("Menghitung Luas Bangun 2D")
# bd.geometry("750x200")

# a,b,c,s3,triangle3 = IntVar(),IntVar(),IntVar(),DoubleVar(),DoubleVar()
# sisi,square = IntVar(),IntVar()
# r,circle_a = IntVar(),DoubleVar()

# def triangle_area():
#     try:
#         triangle3.set(round(float((a.get()*b.get())/2),2))
#         Label(bd, text = "Luas Segitiga\t:").grid(row = 5, column = 0)
#         Label(bd, textvariable = triangle3).grid(row = 5, column = 1)
#     except ValueError:
#         pass

# def square_area():
#     try:
#         square.set(sisi.get()**2)
#         Label(bd,text = "Luas Persegi\t:").grid(row = 2, column = 2  )
#         Label(bd,textvariable = square).grid(row = 2,column = 3 )
#     except ValueError:
#         pass

# def circle_area():
#     try:
#         circle_a.set(round(float(math.pi*(r.get()**2)),2))
#         Label(bd, text = "Luas Lingkaran\t:").grid(row = 2 ,column = 4)
#         Label(bd, textvariable = circle_a).grid(row = 2, column = 5)

#     except ValueError:
#         pass

# #display segi3
# Label(bd, text="Luas Segitiga").grid(row = 0, column = 1)
# Label(bd, text = "Alas\t:").grid(row = 1, column = 0)
# Entry(bd, textvariable = a).grid(row= 1, column = 1)
# Label(bd, text = "Tinggi\t:").grid(row = 2, column = 0)
# Entry(bd, textvariable = b).grid(row = 2, column = 1)
# # Label(bd, text = "Sisi C\t:").grid(row = 3, column = 0)
# # Entry(bd, textvariable = c).grid(row = 3, column = 1)

# #display segi4
# Label(bd, text = "Luas Persegi").grid(row = 0, column = 3)
# Label(bd, text = "Sisi Persegi").grid(row = 1, column  = 2)
# Entry(bd, textvariable = sisi).grid(row = 1, column = 3)

# #display lingkaran
# Label(bd, text = "Luas Lingkaran").grid(row = 0, column = 5)
# Label(bd, text = "Luas Lingkaran").grid(row = 1, column  = 4)
# Entry(bd, textvariable = r).grid(row = 1, column = 5)

# Button(bd, text = "Hasil",command = triangle_area).grid(row = 4, column = 1)    #button hasil luas segi3
# Button(bd, text="Hasil", command = square_area).grid(row = 4, column = 3) #button hasil luas segi4
# Button(bd, text="Hasil",command = circle_area).grid(row = 4,column  = 5) #button hasil luas lingkaran

# bd.mainloop()

###########################################################################
###versi 2.1


# from tkinter import *
# import math

# global bd
# bd = Tk()
# bd.title("Bangun Datar")
# bd.geometry("200x200")

# def segitiga():
#     global bd1
#     bd1 = Toplevel(bd)
#     bd1.title("SEGITIGA")
#     bd1.geometry("200x200")

#     a,t,luas3 = DoubleVar(),DoubleVar(),DoubleVar()    

#     Label(bd1,text = "Nilai Alas:").grid(row= 0,column = 0)
#     Entry(bd1,textvariable = a).grid(row = 0,column = 1)    
#     Label(bd1,text = "Nilai Tinggi:").grid(row= 1)    
#     Entry(bd1,textvariable = t).grid(row = 1,column = 1)    

#     def hitung_luas3():
#         try:
#             luas3.set(round(float((a.get()*t.get())/2),2))
#             Label(bd1,text = "L.Segi3 = ").grid(row = 3,column = 0)
#             Label(bd1, textvariable = luas3).grid(row = 3, column = 1)
#         except ValueError:
#             pass

#     Button(bd1, text = "Hitung",command = hitung_luas3).grid(row = 2, column =1)
#     Button(bd1, text = "Selesai",command = bd1.destroy).grid(row = 2,column = 0)
        
# def persegi():
#     global bd2
#     bd2 = Toplevel(bd)
#     bd2.title("PERSEGI")
#     bd2.geometry("200x200")

#     s,luas4 = IntVar(),IntVar()

#     Label(bd2,text = "Nilai Sisi:").grid(row= 0,column = 0)
#     Entry(bd2,textvariable = s).grid(row = 0,column = 1)

#     def hitung_luas4():
#         try:
#             luas4.set(s.get()**2) 
#             Label(bd2,text = "L.Segi4 = ").grid(row = 3,column = 0)
#             Label(bd2, textvariable = luas4).grid(row = 3, column = 1)
#         except ValueError:
#             pass

#     Button(bd2, text = "Hitung",command = hitung_luas4).grid(row = 2, column =1)
#     Button(bd2, text = "Selesai",command = bd2.destroy).grid(row = 2,column =0)

# def lingkaran():
#     global bd3
#     bd3 = Toplevel(bd)
#     bd3.title("LINGKARAN")
#     bd3.geometry("200x200")

#     r,luas0 = DoubleVar(),DoubleVar()

#     Label(bd3,text = "Jari-Jari:").grid(row= 0,column = 0)
#     Entry(bd3,textvariable = r).grid(row = 0,column = 1)


#     def hitung_luas0():
#         try:
#             luas0.set(round(float(math.pi*(r.get()**2)),2))
#             Label(bd3,text = "L.Lingkaran = ").grid(row = 3,column = 0)
#             Label(bd3, textvariable = luas0).grid(row = 3, column = 1)
#         except ValueError:
#             pass

#     Button(bd3, text = "Hitung",command = hitung_luas0).grid(row = 2, column =1)
#     Button(bd3, text = "Selesai",command = bd3.destroy).grid(row = 2,column = 0)

# Button(bd, text = "Segitiga",command = segitiga).pack()
# Button(bd, text = "Persegi",command = persegi).pack()
# Button(bd, text = "Lingkaran",command = lingkaran).pack()
# Button(bd, text = "Keluar", command = bd.quit).pack()

# bd.mainloop()


#####################################################################################
"""versi 2.2"""

from tkinter import *
import math

class Menu:
    def __init__(self,master):
        self.master = master
        self.master.title("Bangun Datar")
        self.master.geometry("200x200")
        self.frame = Frame(self.master)
        self.frame.pack()
        Button(self.frame, text = "Segitiga",command = self.segitiga).pack()
        Button(self.frame, text = "Persegi",command = self.persegi).pack()
        Button(self.frame, text = "Lingkaran",command = self.lingkaran).pack()
        Button(self.frame, text = "Keluar", command = self.master.quit).pack()

    def segitiga(self):
        segi3 = Toplevel(self.master)
        self.window = Triangle(segi3)

    def persegi(self):
        segi4 = Toplevel(self.master)
        self.window = Square(segi4)

    def lingkaran(self):
        segi0 = Toplevel(self.master)
        self.window = Circle(segi0)

class Triangle:
    
    def __init__(self,sub_master):
        self.sub_master = sub_master
        self.sub_frame = Frame(self.sub_master)
        self.sub_frame.pack()
        self.sub_master.title("SEGITIGA")
        self.sub_master.geometry("200x200")
            
        self.a = DoubleVar()
        self.t = DoubleVar()
        self.luas3 = DoubleVar()

        self.label1 = Label(self.sub_frame,text = "Nilai Alas:")
        self.label1.grid(row= 0,column = 0)
        self.entry1 = Entry(self.sub_frame,textvariable = self.a)
        self.entry1.grid(row = 0,column = 1)    
        self.label2 =  Label(self.sub_frame,text = "Nilai Tinggi:")
        self.label2.grid(row= 1,column = 0)    
        self.entry2 = Entry(self.sub_frame,textvariable = self.t)
        self.entry2.grid(row = 1,column = 1)
        self.hitung = Button(self.sub_frame, text = "Hitung",command = self.hitung_luas3)
        self.hitung.grid(row = 2, column =1)
        self.selesai = Button(self.sub_frame, text = "Selesai",command = self.sub_master.destroy)
        self.selesai.grid(row = 2,column = 0)

    def hitung_luas3(self):
        try:
            self.luas3.set(round(float((self.a.get()*self.t.get())/2),2))
            self.label3 = Label(self.sub_frame,text = "L.Segi3 = ")
            self.label3.grid(row = 3,column = 0)
            self.label4 = Label(self.sub_frame, textvariable = self.luas3)
            self.label4.grid(row = 3, column = 1)
        except ValueError:
            pass

class Square:
    
    def __init__(self,sub_master):
        self.sub_master = sub_master
        self.sub_frame = Frame(self.sub_master)
        self.sub_frame.pack()
        self.sub_master.title("PERSEGI")
        self.sub_master.geometry("200x200")
            
        self.s = IntVar()
        self.luas4 = IntVar()

        self.label1 = Label(self.sub_frame,text = "Nilai Sisi:")
        self.label1.grid(row= 0,column = 0)
        self.entry1 = Entry(self.sub_frame,textvariable = self.s)
        self.entry1.grid(row = 0,column = 1)
        self.hitung = Button(self.sub_frame, text = "Hitung",command = self.hitung_luas4)
        self.hitung.grid(row = 2, column =1)
        self.selesai = Button(self.sub_frame, text = "Selesai",command = self.sub_master.destroy)
        self.selesai.grid(row = 2,column = 0)

    def hitung_luas4(self):
        try:
            self.luas4.set(self.s.get()**2)
            self.label2 = Label(self.sub_frame,text = "L.Persegi = ")
            self.label2.grid(row = 3,column = 0)
            self.label3 = Label(self.sub_frame, textvariable = self.luas4)
            self.label3.grid(row = 3, column = 1)
        except ValueError:
            pass

class Circle:
    
    def __init__(self,sub_master):
        self.sub_master = sub_master
        self.sub_frame = Frame(self.sub_master)
        self.sub_frame.pack()
        self.sub_master.title("LINGKARAN")
        self.sub_master.geometry("200x200")
            
        self.r = DoubleVar()
        self.luas0 = DoubleVar()

        self.label1 = Label(self.sub_frame,text = "Jari - jari:")
        self.label1.grid(row= 0,column = 0)
        self.entry1 = Entry(self.sub_frame,textvariable = self.r)
        self.entry1.grid(row = 0,column = 1)    
        self.hitung = Button(self.sub_frame, text = "Hitung",command = self.hitung_luas0)
        self.hitung.grid(row = 2, column =1)
        self.selesai = Button(self.sub_frame, text = "Selesai",command = self.sub_master.destroy)
        self.selesai.grid(row = 2,column = 0)

    def hitung_luas0(self):
        try:
            self.luas0.set(round(float(math.pi*(self.r.get()**2)),2))
            self.label3 = Label(self.sub_frame,text = "L.Lingkaran = ")
            self.label3.grid(row = 3,column = 0)
            self.label4 = Label(self.sub_frame, textvariable = self.luas0)
            self.label4.grid(row = 3, column = 1)
        except ValueError:
            pass


def main_program():
    bd = Tk()
    b_datar = Menu(bd)
    bd.mainloop()

main_program()