try:
    class laboratorium:
        'laboratorium komputer'
    
        def __init__ (self,kode,komputer,meja,kursi,keg):
            self.kode = kode
            self.komputer = komputer
            self.meja = meja
            self.kursi = kursi
            self.keg = keg
        def inventory(self):
            print("\tInventaris Laboratorium")
            print("Kode Lab\t:",getattr(lab,'kode'))
            print("Jumlah komputer\t:",getattr(lab,"komputer"))
            print("Jumlah meja\t:",getattr(lab,"meja"))
            print("Jumlah kursi\t:",getattr(lab,"kursi"))
        def kegiatan(self):
            print("Kegiatan saat ini",getattr(lab,"keg"))
    lab = laboratorium("","","","","")
    setattr(lab,"kode","3A")
    setattr(lab,"komputer","50")
    setattr(lab,"meja","50")
    setattr(lab,"kursi","50")
    k = input("kegiatan\t: ")
    setattr(lab,"keg",k)
    lab.kegiatan()
    print()
    lab.inventory()
    print()
    print("laboratorium memiliki atribut kode :",hasattr(lab,"kode"))
    print("hapus kode lab!")
    delattr(lab,"kode")
    lab.inventory()
except AttributeError:
    print("Atribut sudah dihapus")