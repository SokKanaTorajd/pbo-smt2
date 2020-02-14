# from tkinter import *

# class Test(Frame):

#     def __init__(self,master = None):
#         Frame.__init__(self, master)
#         self.master =  master
#         self.win()

#     def win(self):
#         self.pack()

#         self.label = Label(self, text="hello World!").pack()
#         self.quit = Button(self, text= "quit", command = self.master.destroy).pack()

# root=Tk()
# Test()

# import Test
# class Wtf(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.btn()
#         self.test = Test()

#     def btn(self):
#         self.pack()

#         self.test = Test()

#         self.btn = Button(self, text = "Call", command = self.test.win).pack()

# root=Tk()
# app = Wtf(root)

import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()