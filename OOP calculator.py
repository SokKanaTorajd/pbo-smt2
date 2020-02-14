from tkinter import * 
 
class Calculator(): 
 
    def __init__(self, master):         
        self.master = master         
        master.title("Calculator")         
        self.total = 0         
        self.entered_number = 0         
        self.total_label_text = IntVar()         
        self.total_label_text.set(self.total)         
        self.total_label = Label(master, textvariable=self.total_label_text)         
        self.label = Label(master, text="Total:")         
        self.label_input = Label(master, text="Input:") 
 
        vcmd = master.register(self.validate) # validasi input 
 
    # penggunaan nilai lambda untuk menjaga nilai tetap bisa dioperasikan lagi         
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))         
        self.ttambah = Button(master, text=" + ", command=lambda: self.update("tambah"))         
        self.tkurang = Button(master, text=" - ", command=lambda: self.update("kurang"))         
        self.tkali = Button(master, text=" x ", command=lambda: self.update("kali"))
        self.tbagi = Button(master, text = "/", command = lambda: self.update("bagi") )         
        self.treset = Button(master, text=" Reset ", command=lambda: self.update("reset"))         
        self.tkeluar = Button(master, text=" Keluar ", command=master.quit) 
 
    # tampilan         
        self.label_input.grid(row=0, column=0, sticky=W)         
        self.label.grid(row=3, column=0, sticky=W)         
        self.total_label.grid(row=3, column=1, columnspan=2, sticky=E)         
        self.entry.grid(row=1, column=0, columnspan=4, sticky=W+E)         
        self.ttambah.grid(row=2, column=0 )         
        self.tkurang.grid(row=2, column=1 )         
        self.tkali.grid(row=2, column=3)
        self.tbagi.grid(row =2 , column = 2 )         
        self.treset.grid(row=4, column=0)         
        self.tkeluar.grid(row=4, column=2) 
 
    # validasi agar data input hanya berupa angka     
    def validate(self, new_text):         
        if not new_text: # the field is being cleared             
            self.entered_number = 0             
            return True 
 
        try:
            self.entered_number = int(new_text)             
            return True         
        except ValueError:             
            return False 
 
    def update(self, method):         
        if method == "tambah":             
            self.total += self.entered_number         
        elif method == "kurang":             
            self.total -= self.entered_number         
        elif method == "kali":          
            self.total *= self.entered_number
        elif method == "bagi":
            self.total /= self.entered_number         
        else: # reset             
            self.total = 0  
            
        self.total_label_text.set(self.total)         
        self.entry.delete(0, END) 
 
root = Tk() 
my_gui = Calculator(root) 
root.mainloop() 