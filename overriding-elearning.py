#E-LEARNING BAB OVERRIDNG
class Kendaraan():
    def __init__(self):
        super(Kendaraan,self).__init__()
        self.jenis = "Kendaraan"
        self.nama = None
        self.mesin = None
        self.plat = None
        self.merk = None
        self.warna = None
    # def ubah(self):
    #     self.nama = None
    #     self.mesin = None
    #     self.plat = None
    #     self.merk = None
    #     self.warna = None
    def ubah_nama(self):
        self.nama = None
    def ubah_mesin(self):
        self.mesin = None
    def ubah_plat(self):
        self.plat = None
    def ubah_merk(self):
        self.merk = None
    def ubah_warna(self):
        self.warna = None
    def tampil(self):
        print("Jenis Kendaraan",self.jenis)
        print("Pemilik\t:",self.nama)
        print("Mesin\t:",self.mesin)
        print("Plat Nomor\t:",self.plat)
        print("Merk\t:",self.merk)
        print("Warna\t:",self.warna)

class Motor(Kendaraan):
    def input_data(self):
        print("==========================Input Data Motor==========================")
        self.jenis = "Motor" #overriding
        self.nama = input("masukkan nama pemilik\t: ") #overriding
        self.mesin = input("masukkan cc mesin\t: ") #overriding
        self.plat = input("masukkan plat nomer\t: ") #overriding
        self.merk = input("masukkan merk kendaraan\t: ") #overriding
        self.warna = input("masukkan warna kendaraan: ") #overriding
    # def ubah(self):
    #     print("==========================Ubah Data Motor==========================")
    #     self.nama = input("masukkan nama pemilik\t: ")
    #     self.mesin = input("masukkan cc mesin\t: ")
    #     self.plat = input("masukkan plat nomer\t: ")
    #     self.merk = input("masukkan merk kendaraan\t: ")
    #     self.warna = input("masukkan warna kendaraan: ")
    def ubah_nama(self):
        self.nama = input("masukkan nama pemilik\t: ") #overriding
    def ubah_mesin(self):
        self.mesin = input("masukkan cc mesin\t: ") #overriding
    def ubah_plat(self):
        self.plat = input("masukkan plat nomer\t: ") #overriding
    def ubah_merk(self):
        self.merk = input("masukkan merk kendaraan\t: ") #overriding
    def ubah_warna(self):
        self.warna = input("masukkan warna kendaraan: ") #overriding
    def tampil(self):
        print("==========================Data Motor==========================")
        print("Jenis Kendaraan\t:",self.jenis)
        print("Pemilik\t\t:",self.nama)
        print("Mesin\t\t:",self.mesin)
        print("Plat Nomor\t:",self.plat)
        print("Merk\t\t:",self.merk)
        print("Warna\t\t:",self.warna)

class Mobil(Kendaraan):
    def input_data(self):
        print("==========================Input Data Mobil==========================")
        self.jenis = "Mobil" #overriding
        self.nama = input("masukkan nama pemilik\t: ") #overriding
        self.mesin = input("masukkan cc mesin\t: ") #overriding
        self.plat = input("masukkan plat nomer\t: ") #overriding
        self.merk = input("masukkan merk kendaraan\t: ") #overriding
        self.warna = input("masukkan warna kendaraan: ") #overriding
    # def ubah(self):
    #     print("==========================Ubah Data Mobil==========================")
    #     self.nama = input("masukkan nama pemilik\t: ")
    #     self.mesin = input("masukkan cc mesin\t: ")
    #     self.plat = input("masukkan plat nomer\t: ")
    #     self.merk = input("masukkan merk kendaraan\t: ")
    #     self.warna = input("masukkan warna kendaraan: ")
    def ubah_nama(self):
        self.nama = input("masukkan nama pemilik\t: ") #overriding
    def ubah_mesin(self):
        self.mesin = input("masukkan cc mesin\t: ") #overriding
    def ubah_plat(self):
        self.plat = input("masukkan plat nomer\t: ") #overriding
    def ubah_merk(self):
        self.merk = input("masukkan merk kendaraan\t: ") #overriding
    def ubah_warna(self):
        self.warna = input("masukkan warna kendaraan: ") #overriding
    def tampil(self):
        print("==========================Data Mobil==========================")
        print("Jenis Kendaraan\t:",self.jenis)
        print("Pemilik\t\t:",self.nama)
        print("Mesin\t\t:",self.mesin)
        print("Plat Nomor\t:",self.plat)
        print("Merk\t\t:",self.merk)
        print("Warna\t\t:",self.warna)
mtr = Motor()
mbl = Mobil()

def option():
    print("==========================Data Kendaraan==========================")
    print("1. input data motor")
    print("2. input data mobil")
    print("3. ubah data motor")
    print("4. ubah data mobil")
    print("5. tampil data motor")
    print("6. tampil data mobil")
    print("7. Tekan 7 untuk keluar")
    n = input("pilihan anda: ")
    print()
    return n

def input_motor():
    mtr.input_data()

def input_mobil():
    mbl.input_data()

def ubah_motor():
    print("1. ubah nama")
    print("2. mesin")
    print("3. plat")
    print("4. merk")
    print("5. warna")
    print("tekan 0 untuk kembali")
    m = input("pilihan anda: ")
    print()
    return m

def ganti_nama_mtr():
    mtr.ubah_nama()
    mtr.tampil()
def ganti_mesin_mtr():
    mtr.ubah_mesin()
    mtr.tampil()
def ganti_plat_mtr():
    mtr.ubah_plat()
    mtr.tampil()
def ganti_merk_mtr():
    mtr.ubah_merk()
    mtr.tampil()
def ganti_warna_mtr():
    mtr.ubah_warna()
    mtr.tampil()

def ubah_mobil():
    print("1. ubah nama")
    print("2. mesin")
    print("3. plat")
    print("4. merk")
    print("5. warna")
    print("tekan 0 untuk kembali")
    o = input("pilihan anda")
    print()
    return o

def ganti_nama_mbl():
    mbl.ubah_nama()
    mtr.tampil()
def ganti_mesin_mbl():
    mbl.ubah_mesin()
    mtr.tampil()
def ganti_plat_mbl():
    mbl.ubah_plat()
    mtr.tampil()
def ganti_merk_mbl():
    mbl.ubah_merk()
    mtr.tampil()
def ganti_warna_mbl():
    mbl.ubah_warna()
    mtr.tampil()

# def ubah_motor():
#     mtr.ubah()
#     mtr.tampil()

# def ubah_mobil():
#     mbl.ubah()
#     mbl.tampil()

def tampil_motor():
    mtr.tampil()

def tampil_mobil():
    mbl.tampil()

while 1==1:
    print()
    opt = option()
    if opt == "1":
        input_motor()
    elif opt == "2":
        input_mobil()
    elif opt == "3":
        while 1==1:
            print()
            umtr = ubah_motor()
            if umtr == "1":
                ganti_nama_mtr()
            elif umtr == "2":
                ganti_mesin_mtr()
            elif umtr == "3":
                ganti_plat_mtr()
            elif umtr == "4":
                ganti_merk_mtr()
            elif umtr == "5":
                ganti_warna_mtr()
            else:
                break
    elif opt == "4":
        while 1==1:
            print()
            umbl = ubah_mobil()
            if umtr == "1":
                ganti_nama_mbl()
            elif umtr == "2":
                ganti_mesin_mbl()
            elif umtr == "3":
                ganti_plat_mbl()
            elif umtr == "4":
                ganti_merk_mbl()
            elif umtr == "5":
                ganti_warna_mbl()
            else:
                break
    elif opt == "5":
        tampil_motor()
    elif opt == "6":
        tampil_mobil()
    else:
        print("++++++++++++++++++++++++++Terima Kasih++++++++++++++++++++++++++++++")
        break

# while 1==1:
#     print()
#     opt = option()
#     if opt == "1":
#         input_motor()
#     elif opt == "2":
#         input_mobil()
#     elif opt == "3":
#         ubah_motor()
#     elif opt == "4":
#         ubah_mobil()
#     elif opt == "5":
#         tampil_motor()
#     elif opt == "6":
#         tampil_mobil()
#     else:
#         print("++++++++++++++++++++++++++Terima Kasih++++++++++++++++++++++++++++++")
#         break