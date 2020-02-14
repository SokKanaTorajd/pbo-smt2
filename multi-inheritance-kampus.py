# MULTI INHERITANCE
class waktu:
    def __init__(self, jam=0, menit=0, detik=0):
        self.jam = jam 
        self.menit = menit 
        self.detik = detik
    def ubahWaktu(self, jam, menit, detik=0): 
        self.jam = jam
        self.menit = menit 
        self.detik = detik

class tempat:
    def __init__(self, namaTempat, latitude, longitude):
        self.namaTempat = namaTempat 
        self.latitude = latitude 
        self.longitude = longitude

class kalender:
    def __init__(self,hari,tanggal,bulan,tahun):
        self.hari=hari
        self.tanggal=tanggal
        self.bulan=bulan
        self.tahun=tahun
    def ubahKalender(self,hari,tanggal,bulan,tahun): 
        self.hari=hari
        self.tanggal=tanggal
        self.bulan=bulan
        self.tahun=tahun

class jadwal(waktu,tempat,kalender):
    def __init__(self):
        self.namaKegiatan = 'Kuliah PBO'
        self.jenisKegiatan = 'Kuliah Teori'
        self.hari='Rabu'
        self.tanggal=6
        self.bulan=3
        self.tahun=2019
        self.jam = 11
        self.menit = 30
        self.namaTempat="Kampus 1 UNJANI"
    def tampilJadwal(self):
        print('Jadwal')
        print('-------------')
        print('Nama Kegiatan :', self.namaKegiatan)
        print('Jenis Kegiatan	:', self.jenisKegiatan)
        print('Hari/tgl	:', self.hari,',',self.tanggal,'/',self.bulan,'/',self.tahun)
        print('Waktu	:', self.jam,'.',self.menit,'WIB')
        print('Tempat	:', self.namaTempat)
    def ubahJadwal(self):
        self.namaKegiatan = input("Mata Kuliah : ")   
        self.jenisKegiatan = input("Teori/Praktek : ")   
        self.hari=input("Hari : ")   
        self.tanggal=input("masukkan tanggal : ")   
        self.bulan=input("masukkan bulan : ")   
        self.tahun=input("masukkan tahun : ")   
        self.jam = input("masukkan jam : ")   
        self.menit = input("masukkan menit : ")   
        self.namaTempat=input("masukkan nama kelas : ")
kuliah = jadwal()
kuliah.tampilJadwal()