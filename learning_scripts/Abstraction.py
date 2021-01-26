from abc import ABC, abstractmethod

class Animal(ABC):
    def feed(self, meal):
        print("You have successfully fed it {}".format(meal))
    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Meow")

cat = Cat()
cat.feed('breakfast')
cat.sound()