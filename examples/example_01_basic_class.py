"""
Example 1: Basic Class and Objects
Demonstrates creating a simple class and instantiating objects.
"""

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def description(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"

# Create dog objects
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "Bulldog")

# Use the objects
print(dog1.description())
dog1.bark()

print(dog2.description())
dog2.bark()
