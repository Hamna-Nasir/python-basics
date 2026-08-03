class Animal:
    def sound(self):
        print("some sound")

class Cat(Animal):
    def sound(self):
        print("Meow")
        
Cat = Cat()
Cat.sound()