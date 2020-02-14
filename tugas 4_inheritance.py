#inheritance
class buku():
    def data(self):
        self.pengarang = input("masukkan nama pengarang\t\t:")
        self.tahun = input("masukkan tahun diterbitkan\t:")
        self.judul = input("masukkan judul\t\t\t:")
        self.kota = input("masukkan kota penerbit\t\t:")
        self.penerbit = input("masukkan penerbit\t\t:")
    def tampil(self):
        print("Pengarang\t:",self.pengarang)
        print("Tahun\t\t:",self.tahun)
        print("Judul\t\t:",self.judul)
        print("Kota\t\t:",self.kota)
        print("Penerbit\t:",self.penerbit)
class komik(buku):
    def __init_subclass__(self):
        buku.__init__(self)
    def episode(self):
        self.episode = input("jumlah episode\t\t\t:")
    def show_com(self):
        print("Jumlah Episode\t:",self.episode)    
class majalah(buku):
    def __init_subclass__(self):
        buku.__init__(self)
    def edition(self):
        self.edisi = input("edisi ke\t\t\t:")
    def show_mag(self):
        print("Edisi \t\t:",self.edisi)
class novel(buku):
    def __init_subclass__(self):
        buku.__init__(self)
    def chapter(self):
        self.chapter = input("masukkan jumlah bab\t\t:")
    def show_nov(self):
        print("Jumlah Bab\t:",self.chapter)

k = komik()
print("\t\tInput Data Komik")
k.data()
k.episode()
print("\t\tData Komik")
k.tampil()
k.show_com()

m = majalah()
print("\t\tInput Data Majalah")
m.data()
m.edition()
print("\t\tData Majalah")
m.tampil()
m.show_mag()

n = novel()
print("\t\tInput Data Novel")
n.data()
n.chapter()
print("\t\tData Novel")
n.tampil()
n.show_nov()