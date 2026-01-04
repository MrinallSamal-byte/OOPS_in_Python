"""
Example 2: Inheritance
Demonstrates how child classes inherit from parent classes.
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"{self.name} makes a sound")
    
    def info(self):
        print(f"{self.name} is a {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        print(f"{self.name} barks: Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} meows: Meow!")

# Create objects
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

# Demonstrate inheritance and polymorphism
animals = [dog, cat]
for animal in animals:
    animal.info()
    animal.make_sound()
    print()
