##Materi##

# class Hero(object): 
#     """__init__() functions as the class constructor""" 
#     def __init__(self, nama=None, alias=None, kelompok=None, listHero=None): 
#         self.nama = nama 
#         self.alias = alias 
#         self.kelompok = kelompok
#         self.listHero = listHero

# listHero = [] 
# for x in range(5):
#     nama = input("masukkan nama\t:")
#     alias = input("masukkan alias\t:")
#     kelompok = input("masukkan kelompok\t:")
#     listHero.append(Hero(nama,alias,kelompok))
 
# print ("Hero pertama:", listHero[0].nama,"\n")
# print("Daftar superhero:\n") 
# for Hero in listHero: 
#     print("Nama: {}\nAlias: {}\nKelompok: {}\n\n".format(Hero.nama, Hero.alias, Hero.kelompok))
    

##TUGAS##

from tkinter import *
from tkinter import ttk

class Hero():

    def __init__(self, parent):

        self.parent=parent
        self.view()

    def view(self):

        self.parent.title("Daftar Super Hero")       
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)

        self.nama_label = Label(self.parent, text = "Nama")
        self.nama_entry = Entry(self.parent)
        self.nama_label.grid(row = 0, column = 0, sticky = "W")
        self.nama_entry.grid(row = 0, column = 1)

        self.alias_label = Label(self.parent, text = "Alias")
        self.alias_entry = Entry(self.parent)
        self.alias_label.grid(row = 1, column = 0, sticky = "W")
        self.alias_entry.grid(row = 1, column = 1)

        self.group_label = Label(self.parent, text = "Kelompok")
        self.group_entry = Entry(self.parent)
        self.group_label.grid(row = 2, column = 0, sticky = "W")
        self.group_entry.grid(row = 2, column = 1)

        self.submit_button = Button(self.parent, text = "Insert", command = self.insert_data)
        self.submit_button.grid(row = 3, column = 1, sticky ="W")
        self.exit_button = Button(self.parent, text = "Exit", command = self.parent.quit)
        self.exit_button.grid(row = 0, column = 3)

        self.tree = ttk.Treeview( self.parent, columns=('nama', 'alias','Group'))
        self.tree.heading('#0', text='Nomor')
        self.tree.heading('#1', text='Nama')
        self.tree.heading('#2', text='Alias')
        self.tree.heading('#3', text='Group')
        self.tree.column('#0',stretch=YES)
        self.tree.column('#1', stretch=YES)
        self.tree.column('#2', stretch=YES)
        self.tree.column('#3',stretch=YES)
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        self.i = 1

    def insert_data(self):
        self.treeview.insert('', 'end', text=str(self.i), values=(self.nama_entry.get(), self.alias_entry.get(),self.group_entry.get()))
        self.i += 1         

def main():
    hiro=Tk()
    Hero(hiro)
    hiro.mainloop()

if __name__=="__main__":
    main()
