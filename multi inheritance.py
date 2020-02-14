
#kuis_smt2
#multi inheritance
class dosen:
    def __init__(self,nip,namadsn):
        self.nip = nip 
        self.namadsn = namadsn
    def ubahDosen(self): 
        self.nip = input("masukkan nip: ") 
        self.namadsn = input("masukkan nama: ")

class mahasiswa:
    def __init__(self, namamhs, nim, semester):
        self.nim = nim
        self.namamhs = namamhs
        self.semester = semester
    def ubahMhs(self):
        self.namamhs = input("masukkan nama: ") 
        self.nim = input("masukkan nim: ") 
        self.semester = input("masukkan semester: ")

class kelas:
    def __init__(self,kodekls,lantai,gedung):
        self.kodekls=kodekls
        self.lantai=lantai
        self.gedung=gedung
    def ubahKelas(self): 
        self.kodekls=input("masukkan kode kelas: ")
        self.lantai=input("masukkan lantai: ")
        self.gedung=input("masukkan gedung: ")

class jadwal(dosen,mahasiswa,kelas):
    def __init__(self):
        self.kodejdw = input("masukkan kode jadwal : ")
        self.tanggal = input("masukkan tanggal : ")
        self.waktu=input("masukkan waktu : ")
        self.namadsn=input("masukkan nama dosen: ")
        self.nip=input("masukkan nip: ")
        self.namamhs=input("masukkan nama mahasiswa: ")
        self.nim = input("masukkan nim: ")
        self.semester = input("masukkan semester: ")
        self.kodekls=input("masukkan kode kelas: ")
        self.lantai=input("masukkan lantai: ")
        self.gedung=input("masukkan gedung: ")
    def tampilJadwal(self):
        print("==========================Jadwal=========================")
        print()
        print('Kode Jadwal\t:', self.kodejdw)
        print('Tanggal\t\t:', self.tanggal)
        print('Waktu\t\t:', self.waktu)
        print('Nama Dosen\t:', self.namadsn)
        print('NIP\t\t:', self.nip)
        print("Nama Mahasiswa\t:",self.namamhs)
        print('NIM\t\t:', self.nim)
        print("Semester\t:",self.semester)
        print("Kode Kelas\t:",self.kodekls)
        print("Lantai\t\t:",self.lantai)
        print("Gedung\t\t:",self.gedung)
    def ubahJadwal(self):
        self.kodejdw = input("masukkan kode jadwal : ")
        self.tanggal = input("masukkan tanggal : ")
        self.waktu=input("masukkan waktu : ")
print("==========================input jadwal==========================")
kuliah = jadwal()
def option():
    print("==========================Jadwal Kuliah==========================")
    print("1. Tampil Jadwal")
    print("2. Ubah Dosen")
    print("3. Ubah Mahasiswa")
    print("4. Ubah Kelas")
    print("5. Ubah Jadwal")
    print("Tekan apa saja untuk keluar kemudian Enter")
    n = input("pilihan anda: ")
    return n
def gantidosen():
    kuliah.ubahDosen()
def gantimhs():
    kuliah.ubahMhs()
def gantikls():
    kuliah.ubahKelas()
def gantijdw():
    kuliah.ubahJadwal()
while 1==1:
    opt = option()
    if opt == "1":
        kuliah.tampilJadwal()
    elif opt == "2":
        gantidosen()
    elif opt == "3":
        gantimhs()
    elif opt == "4":
        gantikls()
    elif opt == "5":
        gantijdw()
    else:
        kuliah.tampilJadwal()
        print("Terima Kasih")
        break