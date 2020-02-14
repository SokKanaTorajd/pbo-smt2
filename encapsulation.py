class Queue:
  def __init__(self, contents):
    self._hiddenlist = list(contents)

  def push(self, value):
    self._hiddenlist.insert(0, value)
   
  def pop(self):
    return self._hiddenlist.pop(-1)

  def __repr__(self):
    return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

"Different Example"

# class Computer:
# #janganlupakan parameter
#     # def __init__(self):
#     def __init__(self):
#         self.__prosesor = 'Intel Core i7-6700K'
#         self.__memory = '16GB DDR4'
#         self.os = 'Windows 10 Pro'
#         self.keyboard = 'Razer'
#         self.mouse = 'Logitech'
#     def ganti(self,cpu,ram):
#         self.__prosesor = cpu
#         self.__memory = ram

#     # def tampilData(self):
#     def tampilData(self):
#         print('Prosesor\t:',self.__prosesor)
#         print('memory\t\t:',self.__memory)
#         # print('Prosesor\t:',self.__prosesor)
#         # print('memory\t\t:',self.__memory)
#         print("OS\t\t:",self.os)
#         print("keyboard\t:",self.keyboard)
#         print("mouse\t\t:",self.mouse)
#     # def __init__(self,prosesor,memory,os,keyboard,mouse):
#     #     self.__prosesor = prosesor
#     #     self.__memory = memory
#     #     self.os = os
#     #     self.keyboard = keyboard
#     #     self.mouse = mouse

#     # def tampilData(self):
#     # 	print('Prosesor: ', getattr(pc,"prosesor"))
#     # 	print('Memory: ', getattr(pc,"memory"))
#     # 	print('OS: ', getattr(pc,"os"))
#     # 	print('Keyboard: ', getattr(pc,"keyboard"))
#     # 	print('Mouse: ', getattr(pc,"mouse"))

# # pc = Computer("","","","","")
# pc =  Computer()
# pc.tampilData()
# pc.ganti((input("prosesor\t: ")),(input("memory\t\t: ")))
# pc.tampilData()

# # p = input("jenis prosesor: ")
# # m = input("kapasitas memory: ")
# # o = input("operating system: ")
# # k = input("keyboard:")
# # mo = input("mouse: ")
# # setattr(pc,"prosesor",p)
# # setattr(pc,"memory",m)
# # setattr(pc,"os",o)
# # setattr(pc,"keyboard",k)
# # setattr(pc,"mouse",mo)
# # print()
# # pc.tampilData()
# # print(pc._Computer__memory)
# # print(pc._Computer__prosesor)
# # pc.ganti("3GB")

"Different Example"

# class Computer:

#     def __init__(self):
#         self.__prosesor = 'Intel Core i7-6700K'
#         self.__memory = '16GB DDR4'
#         self.os = 'Windows 10 Pro'
#         self.keyboard = 'Razer'
#         self.mouse = 'Logitech'

#     def tampilData(self):
#     	print('Prosesor: ', self.__prosesor)
#     	print('Memory: ', self.__memory)
#     	print('OS: ', self.os)
#     	print('Keyboard: ', self.keyboard)
#     	print('Mouse: ', self.mouse)
#     def gantiram(self,ram): #mengganti private atribut
#         self.__memory = ram
#     def ganticpu(self,cpu): #mengganti private atribut
#         self.__prosesor = cpu
# pc = Computer()
# pc.tampilData()
# print()
# pc.gantiram(input("ram:"))
# pc.ganticpu(input("cpu:"))
# print()
# pc.tampilData()


# # script nomor 4 bab 4
# # ENCAPSULATION
# class computer:

#     def __init__(self):
#         self.__prosesor = None
#         self.__memory = None
#         self.os = None
#         self.keyboard = None
#         self.mouse = None

#     def __setPros(self, newPros):
#     	self.__prosesor = newPros
#     def __setMemo(self, newMemo):
#     	self.__memory = newMemo

#     def tampilData(self):
#     	print('Data PC:')
#     	print('Prosesor: ', self.__prosesor)
#     	print('Memory: ', self.__memory)
#     	print('OS: ', self.os)
#     	print('Keyboard: ', self.keyboard)
#     	print('Mouse: ', self.mouse)
#     	print()

# class modify:

# 	pc = computer()
# 	pc.tampilData()

# 	newPro = input('Prosesor: ')
# 	newMem = input('Memory: ')
# 	newOS = input('OS: ')
# 	newKB = input('Keyboard: ')
# 	newMou = input('Mouse: ')

# 	setattr(pc,'__prosesor',newPro)
# 	setattr(pc,'__memory',newMem)
# 	setattr(pc,'os',newOS)
# 	setattr(pc,'keyboard',newKB)
# 	setattr(pc,'mouse',newMou)
# 	print()

# 	pc.tampilData()