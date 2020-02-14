class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
class carnivora(Animal):
    def __init_subclass__(self):
        Animal.__init__(self)
    def food(self):
        print(fido.name, "is eating meat")
class herbivora(Animal):
    def __init_subclass__(self):
        Animal.__init__(self)
    def food2(self):
        print("I'm eating plant")
class insectivora(Animal):
    def __init_subclass__(self):
        Animal.__init__(self)
    def food3(self):
        print("I'm eating insect")
class omnivora(Animal):
    def __init_subclass__(self):
        Animal.__init__(self)
    def food4(self):
        print("I'm going to eat you!")

fido = carnivora("Fido","Brown")
print(fido.name,"has",fido.color,"fur")
fido.food()

catty = carnivora("Catty","Blonde")
print(catty.name,"has",catty.color,"fur")
catty.food()

