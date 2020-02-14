#OVERRIDING

# class induk(object):
#     def __init__ (self):
#         self.nilai = 5

#     def get_nilai(self):
#         return self.nilai
# class anak(induk):
#     def get_nilai(self):
#         return self.nilai + 1

# anak1=anak()
# print(anak1.get_nilai())

# induk1=induk()
# print(induk1.get_nilai())

# overriding
import math 
class bangunRuang(): 
    """docstring for bangunRuang""" 
    def __init__(self): 
        super(bangunRuang,self).__init__() 
        self.nama = 'Bangun Ruang' 
        self.tinggi = None
        self.luas = None
    def volume(self,luas,tinggi): 
        self.volume = luas*tinggi 
        return self.volume

class balok(bangunRuang):
    def __init__(self):
        self.nama = "Balok"
    def volume(self,p,l,tinggi):
        self.volume = p*l*tinggi
        return self.volume

class tabung(bangunRuang):
    def __init__(self):
        self.nama = "Tabung"
    def volume(self,jari2,tinggi):
        self.volume = math.pi * (jari2**2) * tinggi
        return self.volume

class bola(bangunRuang):
    def __init__(self):
        self.nama = "Bola"
    def volume(self,jari2):
        self.volume = 4/3 *math.pi * (jari2**3)
        return self.volume
blk=balok()
tbn=tabung()
bl=bola()

print("\t\t\tVolume Balok")
print("volume balok\t\t=",blk.volume((float(input("masukkan panjang\t: "))),(float(input("masukkan lebar\t\t: "))),(float(input("masukkan tinggi\t\t: ")))))
print("\t\t\tVolume Tabung")
print("volume tabung\t\t=",tbn.volume((float(input("masukkan jari-jari\t: "))),(float(input("masukkan tinggi\t\t: ")))))
print("\t\t\tVolume Bola")
print("volume bola\t\t=",bl.volume((float(input("masukkan jari-jari\t: ")))))

# print("volume balok =",blk.volume(10,5,2))
# print("volume tabung = ",int(tbn.volume(10,10)))
# print("volume bola = ",int(bl.volume(2)))