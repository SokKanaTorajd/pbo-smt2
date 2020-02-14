from tkinter import *

new = Tk() 
Label(new, text="Sistem Informasi").pack()
#w.pack() 
new.mainloop() 

class GUIpertama:     
    def __init__(self, master):         
        self.master = master         
        master.title("BAB 10")         
        self.label = Label(master, text="Kelas PBO Python!")         
        self.label.pack()         
        self.salam_button = Button(master, text="Salam", command=self.greet)         
        self.salam_button.pack() 

        self.keluar_button = Button(master, text="Keluar", command=master.quit)         
        self.keluar_button.pack() 
 
    def greet(self):         
        print("Selamat Siang!") 
 
root = Tk() 
my_gui = GUIpertama(root) 
root.mainloop()
 

#########################################################################################


# def show_entry_fields():    
#     print("Selamat siang, %s!" % (e.get()))    
#     e.delete(0,END) 
 
# master = Tk() 
# Label(master, text="Kelas PBO Python!").grid(row=0, columnspan=2) 
# Label(master, text="Nama Lengkap").grid(row=1) 
 
# e = Entry(master) 
# e.grid(row=1, column=1) 
 
# Button(master, text='Salam', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4) 
# Button(master, text='Keluar', command=master.quit).grid(row=3, column=1, sticky=W, pady=4) 
 
# mainloop( )

##########################################################################################

# from tkinter import *

# mhs = Tk()
# mhs.geometry("200x200")
# mhs.title("Mahasiswa")
# Label(mhs, text = "Data Mahasiswa").grid(row = 0, column = 1)

# a,b,c = StringVar(),StringVar(),StringVar()

# Label(mhs,text = "Nama").grid(row = 1, column = 0)
# Label(mhs, text = "NIM").grid(row = 2,column = 0 )
# Label(mhs, text = "Prodi").grid(row = 3,column = 0 )
# Entry(mhs, text = a).grid(row = 1, column = 1)
# Entry(mhs,text = b).grid(row= 2, column =1)
# Entry(mhs, text = c).grid(row = 3, column = 1)

# def Show_tombol():
#     Label(mhs,text = "Nama\t:").grid(row = 5, column = 0)
#     Label(mhs, text = a).grid(row = 5, column = 1 )
#     Label(mhs, text = "NIM\t:").grid(row = 6,column = 0 )
#     Label(mhs, text = b).grid(row = 6, column = 1 )
#     Label(mhs, text = "NIM\t:").grid(row = 7,column = 0 )
#     Label(mhs, text = c).grid(row = 7, column =  1)
#     Button(mhs,text = "Exit", command = mhs.quit).grid(row = 8, column = 1)
#     print("Nama\t:",a.get())
#     print("NIM\t:",b.get())
#     print("Prodi\t:",c.get())

# Button(mhs,text= "Show", command = Show_tombol).grid(row =4, column = 1 )

# mhs.mainloop()