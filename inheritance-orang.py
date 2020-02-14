class orang:
    def nama(self):
        nama = str(input("masukkan nama: "))    
    def nik(self):
        nik = str(input("masukkan nik: "))

class dosen(orang):
    def __init_subclass__(self):
        orang.__init__(self)
    def NIP(self):
        nip = (input("masukkan nip: "))
    def matkul(self):
        mk = (input("mata kuliah yang diajar: "))


class mahasiswa(orang):
    def __init_subclass__(self):
        orang.__init__(self)
    def nim(self):
        nim = (input("masukkan nim: "))

class rektor(dosen):
    def __init_subclass__(self):
        dosen.__init__(self)
    def msjbt(self):
        masa = (input("masa jabatan:"))

class kaprodi(dosen):
    def __init_subclass__(self):
        dosen.__init__(self)
    def prodi(self):
        prodi = (input("prodi yang dipimpin: "))

def datarek():
    print("\t\tData Rektor")
    rkt = rektor()
    rkt.nama()
    rkt.nik()
    rkt.NIP()
    rkt.matkul()
    rkt.msjbt()
def datakap():
    print("\t\tData KaProdi")
    kp = kaprodi()
    kp.nama()
    kp.nik()
    kp.prodi()
    kp.NIP()
    kp.matkul()
def datados():
    print("\t\tData Dosen")
    dos = dosen()
    dos.nama()
    dos.nik()
    dos.NIP()
    dos.matkul()
def datamhs():
    print("\t\tData Mahasiswa")
    mhs = mahasiswa()
    mhs.nama()
    mhs.nik()
    mhs.nim()
def option():
    print()
    print("1. Mahasiswa")
    print("2. Dosen")
    print("3. Kaprodi")
    print("4. Rektor")
    # print("5. Ubah Nama")
    print("\tQuit")
    n = input("Input : ")
    return n
# def ubahnama():
#     u = input("Ubah Nama : ")
#     setattr(mhs,"nama",u)
#     return u
while 1==1:
    opt = option()
    if opt == "1":
        datamhs()
    elif opt == "2":
        datados()
    elif opt =="3":
        datakap()
    elif opt =="4":
        datarek()
    # elif opt =="5":
    #     ubahnama()
    else:
        break