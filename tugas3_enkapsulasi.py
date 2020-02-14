#enkapsulasi
class computer:

    def __init__(self):
        self.__prosesor = None
        self.__memory = None
        self.os = None
        self.keyboard = None
        self.mouse = None

    def __setPros(self, newPros):
    	self.__prosesor = newPros
    def __setMemo(self, newMemo):
    	self.__memory = newMemo

    def tampilData(self):
    	print('Data PC:')
    	print('Prosesor: ', self.__prosesor)
    	print('Memory: ', self.__memory)
    	print('OS: ', self.os)
    	print('Keyboard: ', self.keyboard)
    	print('Mouse: ', self.mouse)
    	print()

class modify:

	pc = computer()
	pc.tampilData()

	newPro = input('Prosesor: ')
	newMem = input('Memory: ')
	newOS = input('OS: ')
	newKB = input('Keyboard: ')
	newMou = input('Mouse: ')

	setattr(pc,"__prosesor",pc._computer__setPros(newPro))
	setattr(pc,"__memory",pc._computer__setMemo(newMem))
	setattr(pc,'os',newOS)
	setattr(pc,'keyboard',newKB)
	setattr(pc,'mouse',newMou)
	print()

	pc.tampilData()