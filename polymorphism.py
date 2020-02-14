# # -*- coding: utf-8 -*-
# """
# Created on Wed Mar 27 09:56:10 2019

# @author: acer
# """
# #polymorphism

# class Shark():
#     def swim(self):
#         print("The shark is swimming.")

#     def swim_backwards(self):
#         print("The shark cannot swim backwards, but can sink backwards.")

#     def skeleton(self):
#         print("The shark's skeleton is made of cartilage.")

# class Clownfish():
#     def swim(self):
#         print("The clownfish is swimming.")

#     def swim_backwards(self):
#         print("The clownfish can swim backwards.")

#     def skeleton(self):
#         print("The clownfish's skeleton is made of bone.")
        
# sam = Shark()
# carnage = Clownfish()

# for fish in (sam, carnage):
#     fish.swim()
#     fish.swim_backwards()
#     fish.skeleton()
# print()
# print("###########################")
# def in_the_pacific(fish):
#     fish.swim()

# def bone(fish):
#     fish.skeleton()

# in_the_pacific(sam)
# in_the_pacific(carnage)

# bone(sam)
# bone(carnage)

# class pintu:     
#     def __init__(self):         
#         self.status = "tutup"     
#     def buka(self):         
#         self.status = "buka"     
#     def tutup(self):         
#         self.status = "tutup"     
#     def is_buka(self):         
#         return self.status == "buka" 
 
# class pintuBoolean:     
#     def __init__(self):         
#         self.status = False     
#     def buka(self):         
#         self.status = True     
#     def tutup(self):         
#         self.status = False     
#     def is_buka(self):         
#         return self.status 
 
# a = pintu()
# print(a.buka()) 
# print (a.is_buka())
# print(a.tutup())
# print(a.is_buka())

class Hewan():
    def suara(self):
        self.s = input("masukkan suara hewan: ")
        # print("suara hewan")
    def makan(self):
        self.m = input("masukkan makanan hewan: ")
        # print("makanan hewan")
    def show(self):
        
        print("suara hewan",self.s)
        print("makanan hewan", self.m)

class Kucing():
    def suara(self):
        self.s = input("masukkan suara kucing\t: ")
        # print("kucing mengeong : Meow...")
    def makan(self):
        self.m = input("masukkan makanan kucing\t: ")
        # print("kucing diberi makan whiskas")
    def show(self):
        print("suara kucing",self.s)
        print("kucing makan",self.m)

class Anjing():
    def suara(self):
        self.s = input("masukkan suara anjing\t: ")
        # print("anjing menggonggong : Gukk!!")
    def makan(self):
        self.m = input("masukkan makanan anjing\t: ")
        # print("Anjing makan daging")
    def show(self):
        print("suara anjing",self.s)
        print("anjing makan",self.m)

catty = Kucing()
doggo = Anjing()

# for hewan in (catty, doggo):
#     print("\t\t input data hewan")
#     hewan.suara()
#     hewan.makan()
#     print("\t\t menampilkan data hewan")
#     hewan.show()

def input_data():
    print("\t\t input data hewan")
    for hewan in (catty, doggo):
        hewan.suara()
        hewan.makan()
    # catty.suara()
    # catty.makan()
    # doggo.suara()
    # doggo.makan()

def tampil():
    print("\t\t menampilkan data hewan")
    for hewan in (catty, doggo):
        hewan.show()
    # catty.show()
    # doggo.show()

input_data()
print()
tampil()