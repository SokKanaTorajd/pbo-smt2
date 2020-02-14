from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def bahan_bakar(self):
        pass

class Mobil(Kendaraan):
    def bahan_bakar(self):
        super().bahan_bakar()
        print("Pertamax")

class Motor(Kendaraan):
    # def fuel(self):
    def bahan_bakar(self):
        super().bahan_bakar()
        print("Pertamax Racing")

x = Mobil()
y = Motor()
x.bahan_bakar()
y.bahan_bakar()