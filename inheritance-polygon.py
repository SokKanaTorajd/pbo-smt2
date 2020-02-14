class Polygon:
    #polygon adalah bangun datar segi banyak
    def __init__(self,banyak_sisi):
        self.n = banyak_sisi
        self.sisi = [0 for i in range(banyak_sisi)]
    def inputsisi(self):
        #penggunaan i+1 karena looping dimulai dari 0
        print("masukkan panjang sisi (dalam cm): ")
        self.sisi = [float(input("sisi"+str(i+1)+":"))for i in range(self.n)]
        print()
    def dispsisi(self):
        for i in range(self.n):
            print("panjang sisi",i+1,"adalah",self.sisi[i],"cm")
            print()

class segiempat(Polygon):
    def __init__ (self):
        Polygon.__init__(self,4)
        print("Segi Empat")
    def hit_kel(self):
        a,b,c,d =self.sisi
        k = a+b+c+d
        print("Keliling =",k,"cm")

poligon = Polygon(4)
poligon.inputsisi()
poligon.dispsisi()
s4 = segiempat()
s4.inputsisi()
s4.dispsisi()
s4.hit_kel()
