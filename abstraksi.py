from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    def __init__(self,value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass

class tambah42(AbstractClassExample):
    def do_something(self):
        return self.value+42

class kali42(AbstractClassExample):
    def do_something(self):
        return self.value*42

x = tambah42(10)
y = kali42(10)

print(x.do_something())
print(y.do_something())

# class Animal:
#     __metaclass__ = ABC

#     @abstractmethod
#     def say_something(self):
#           return "I'm an animal!"

# class Cat(Animal):
#     def say_something(self):
#         s = super(Cat, self).say_something()
#         return "%s - %s" % (s, "Miauuu")

# c = Cat()
# c.say_something()
