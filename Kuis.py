class Hero(object):
    def __init__(self, nama=None, iden=None, masuk=None, gapok=None):
        self.nama = nama
        self.iden = iden
        self.masuk = masuk
        self.gapok = gapok

try:
    gaji_harian = 50000
    listPgw = []
    loop = int(input("jumlah data pegawai yang akan dihitung\t:"))
    print() 
    for i in range(loop):
        nama=input("masukan nama pegawai\t:")
        idn=input("masukan nomor id\t:")
        msk=int(input("jumlah hari masuk\t:"))
        gp = msk*gaji_harian
        listPgw.append(Hero(nama,idn,msk,gp))
        print()
        print("-------------------------------------------")
except ValueError:
    print(""" 'jumlah hari masuk' dan 'data pegawai' yang dimasukkan harus angka! """)

print("Gaji Pegawai:\n")
for Hero in listPgw:
    print("Nama\t\t:",Hero.nama)
    print("Nomor identitas\t:",Hero.iden)
    print("hari masuk\t:",Hero.masuk)
    print("gapok\t\t: Rp",Hero.gapok)
    print()
    print("===========================================")

def potongan(cuti):
    assert(cuti.masuk <= 25)
    return print("Presensi <= 25 hari. Gaji dipotong 2.5 %\nTidak mendapat gaji penuh!")

try:
    potongan(listPgw[1])
except AssertionError:
    print("Semua pegawai mendapat gaji penuh!")