# from tkinter import *

# bd = Tk()
# bd.title("Menghitung Luas Bangun 2D")
# bd.geometry("200x150")

# a,b,triangle3 = IntVar(),IntVar(),DoubleVar()

# def triangle_area():
#     try:
#         triangle3.set(round(float((a.get()*b.get())/2),2))
#         Label(text = "L.Segitiga:").grid(row = 4, column = 0)
#         Label(bd, textvariable = triangle3).grid(row = 4, column = 1)
#     except ValueError:
#         pass

# #display
# Label(bd, text ="Luas Segitiga").grid(row = 0, column = 1)
# Label(bd, text = "Alas\t:").grid(row = 1, column = 0)
# Entry(bd, textvariable = a).grid(row= 1, column = 1)
# Label(bd, text = "Tinggi\t:").grid(row = 2, column = 0)
# Entry(bd, textvariable = b).grid(row = 2, column = 1)
# Button(bd, text = "Hasil",command = triangle_area).grid(row = 3, column = 1)

# bd.mainloop()

"Menggunakan PBO"

from tkinter import *

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

def main_program():
    bd = Tk()
    Triangle(bd)
    bd.mainloop()

main_program()