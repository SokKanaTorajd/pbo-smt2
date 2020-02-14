import tkinter as tk
from tkinter.messagebox import showinfo

class InsuffiecientError(Exception):
    pass

class BankAccount:

    def __init__(self, saldo = 500):
        self.saldo = saldo

    def tarik_tunai (self,amount):
        if ((self.saldo - amount) >= 0):
            self.saldo -= amount
        else :
            raise InsuffiecientError

    def setor_tunai(self,amount):
        self.saldo += amount

class ATM(tk.Tk):

    def __init__(self,account = None):
        tk.Tk.__init__(self)
        self.title("ATM")
        if account is None:
            self.account = BankAccount()
        else:
            self.account = account
        
        self.make_widgets()
        self.updatesaldo()

    def tarik_tunai(self):
        try:
            amount = int(self.iEntry.get())
            self.account.tarik_tunai(amount)
            showinfo(title="Transaction", message="Succesful Withdrawal!")

        except ValueError:
            showinfo(title="Transaction", message="Insert your amount")

        except InsuffiecientError:
            showinfo(title="Transaction", message="Insufficient Funds")
        
        self.iEntry.delete(0,tk.END)
        self.updatesaldo()

    def setor_tunai(self):

        try:
            amount = int(self.iEntry.get())
            self.account.setor_tunai(amount)
            showinfo(title="Transaction", message="Succesful Deposit!")
        except ValueError:
            showinfo(title="Transaction", message="Insert your amount")
        
        self.iEntry.delete(0,tk.END)
        self.updatesaldo()
    
    def updatesaldo(self):
        self.updatedsaldo.config (text=str(self.account.saldo))

    def Exit(self):
        showinfo(title="Thank You", message="You logged out")
        exit()

    def make_widgets(self):

        a = tk.Label(self, text = "Balance $")
        a.grid(row = 0, column = 0)

        self.updatedsaldo = tk.Label(self, text="")
        self.updatedsaldo.grid(row = 0, column =1)
        
        b = tk.Label(self, text = "Amount $")
        b.grid(row = 1,column = 0)

        self.iEntry = tk.Entry(self, width = 40)
        self.iEntry.grid(row = 1, column =1)

        c = tk.Button(self, text="Withdrawal", command = self.tarik_tunai)
        c.grid(row = 2, column = 0)

        d = tk.Button(self, text = "Deposit", command = self.setor_tunai)
        d.grid(row = 2, column =1)

        e = tk.Button(self, text = "Quit",command = self.Exit)
        e.grid(row = 2, column = 2)

if __name__ == "__main__":
    root = ATM()
    root.mainloop()