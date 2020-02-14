class mahasiswa:
    'dasar kelas untuk semua mahasiswa'
    jmlmhs = 0

    def __init__ (self,nama,prodi,nim,sex):
        self.nama=nama
        self.prodi=prodi
        self.nim = nim
        self.sex = sex
        mahasiswa.jmlmhs+=1
    def tampiljml(self):
        print("total mahasiswa: ",mahasiswa.jmlmhs)
    def tampilprofil(self):
        print("nama\t:",self.nama)
        print("prodi\t:",self.prodi)
        print("nim\t:",self.nim)
        print("kelamin\t:",self.sex)

mhs1=mahasiswa("","","","")
#mhs2=mahasiswa("","","")

name = input("nama\t:")
sp = input("prodi\t:")
sn = input("nim\t:")
se = input("kelamin\t:")
print()
# na = input("nama\t:")
# p = input("prodi\t:")
# n = input("nim\t:")
# ex = input("kelamin\t:")
setattr(mhs1,"nama",name)
setattr(mhs1,"prodi",sp)
setattr(mhs1,"nim",sn)
setattr(mhs1,"sex",se)
# setattr(mhs2,"nama",na)
# setattr(mhs2,"prodi",p)
# setattr(mhs2,"nim",n)
# setattr(mhs2,"sex","lanang")
print("\t\t##########################################\t\t")
mhs1.tampilprofil()
print()
# mhs2.tampilprofil()
# getattr(mhs1,"nama")