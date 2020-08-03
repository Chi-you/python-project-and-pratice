class Pet: # parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am a pet")
    def speak(self):
        print("I don't know what to say but I am a pet")
class Dog(Pet): # inherit the attribute of the class Pet
    def speak(self): # function overloading
        print("Bark")

class Cat(Pet): 
    def __init__(self, name, age, color): # if we want to add extra attribute to the child class
        super().__init__(name, age) # the super class is exactly the Pet class
        # inherit from the parent class, which functions like : 
        # self.name = name
        # self.age = age
        self.color = color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} and I am a cat")

p = Pet("Tim", 19)
p.speak()
p.show()
d = Dog("Jill", 25)
d.speak()
d.show()
c = Cat("Bill", 34, "Brown")
c.speak()
c.show()