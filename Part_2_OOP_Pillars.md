# Part 2: The Four Pillars of OOP - Chapters 9-15

Welcome to Part 2! Now that you understand classes and objects, let's explore the **Four Pillars of OOP**: Inheritance, Polymorphism, Encapsulation, and Abstraction! 🏛️

---

## Chapter 9: Inheritance - Single Inheritance

### 1️⃣ WHY

**Why do we need inheritance?**

Imagine you're building a zoo management system. You need classes for:
- Dogs (with name, age, and bark() method)
- Cats (with name, age, and meow() method)
- Birds (with name, age, and chirp() method)

Without inheritance, you'd repeat the same code (name, age) in EVERY class! 😰

**What problem does inheritance solve?**

Inheritance lets you create a **parent class** (Animal) with common attributes/methods, then create **child classes** (Dog, Cat, Bird) that automatically get those features PLUS their own unique ones!

**Why is it better?**

- **DRY** (Don't Repeat Yourself) - write common code once
- **Easy maintenance** - fix bugs in one place
- **Clear hierarchy** - models real-world relationships
- **Extensibility** - easily add new types

### 2️⃣ WHEN

**When to use inheritance:**
- Multiple classes share common attributes/methods
- You have an "is-a" relationship (Dog IS-A Animal, Car IS-A Vehicle)
- You want to extend existing functionality
- Creating variations of a base class

**When NOT to use it:**
- For "has-a" relationships (Car HAS-A Engine - use composition instead)
- When classes aren't truly related
- Don't force inheritance just to reuse code

### 3️⃣ HOW

**What is inheritance?**

Inheritance is when a class (child/subclass) **inherits** attributes and methods from another class (parent/superclass). The child gets everything from the parent PLUS can add its own unique features!

**Syntax:**

```python
class ParentClass:
    # Parent class code
    pass

class ChildClass(ParentClass):  # ChildClass inherits from ParentClass
    # Child class code
    pass
```

**Example 1: Basic Inheritance**

```python
# Parent class (also called base class or superclass)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

# Child class (also called derived class or subclass)
class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):  # Cat inherits from Animal
    def meow(self):
        print(f"{self.name} says: Meow!")

# Create objects
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

# Dogs and cats can use methods from Animal class!
dog.eat()    # Output: Buddy is eating (inherited from Animal)
dog.sleep()  # Output: Buddy is sleeping (inherited from Animal)
dog.bark()   # Output: Buddy says: Woof! (defined in Dog)

cat.eat()    # Output: Whiskers is eating (inherited from Animal)
cat.sleep()  # Output: Whiskers is sleeping (inherited from Animal)
cat.meow()   # Output: Whiskers says: Meow! (defined in Cat)

# Check attributes (also inherited)
print(f"{dog.name} is {dog.age} years old")  # Output: Buddy is 3 years old
print(f"{cat.name} is {cat.age} years old")  # Output: Whiskers is 2 years old
```

**What's happening?**
- `Dog` and `Cat` inherit `__init__`, `name`, `age`, `eat()`, and `sleep()` from `Animal`
- They automatically get all of Animal's functionality
- They add their own unique methods (`bark()` and `meow()`)

**Example 2: Real-World Use Case - Employees**

```python
# Parent class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_info(self):
        print(f"ID: {self.employee_id} - {self.name} - Salary: ${self.salary}")
    
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} got a raise! New salary: ${self.salary}")

# Child classes with specific roles
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        # Call parent's __init__ first (we'll learn better way soon!)
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language
    
    def code(self):
        print(f"{self.name} is coding in {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size
    
    def hold_meeting(self):
        print(f"{self.name} is holding a meeting with {self.team_size} team members")

class Designer(Employee):
    def __init__(self, name, employee_id, salary, design_tool):
        super().__init__(name, employee_id, salary)
        self.design_tool = design_tool
    
    def design(self):
        print(f"{self.name} is designing with {self.design_tool}")

# Create employees
dev = Developer("Alice", "E001", 80000, "Python")
manager = Manager("Bob", "E002", 100000, 5)
designer = Designer("Charlie", "E003", 75000, "Figma")

# All can use Employee methods
dev.display_info()      # Output: ID: E001 - Alice - Salary: $80000
manager.display_info()  # Output: ID: E002 - Bob - Salary: $100000
designer.display_info() # Output: ID: E003 - Charlie - Salary: $75000

# All can get raises
dev.give_raise(10000)   # Output: Alice got a raise! New salary: $90000

# Each has unique methods
dev.code()              # Output: Alice is coding in Python
manager.hold_meeting()  # Output: Bob is holding a meeting with 5 team members
designer.design()       # Output: Charlie is designing with Figma
```

**Example 3: Checking Inheritance Relationships**

```python
class Vehicle:
    pass

class Car(Vehicle):
    pass

class ElectricCar(Car):
    pass

tesla = ElectricCar()

# Check if an object is an instance of a class
print(isinstance(tesla, ElectricCar))  # Output: True
print(isinstance(tesla, Car))          # Output: True (inherited!)
print(isinstance(tesla, Vehicle))      # Output: True (inherited from Car!)

# Check if a class is a subclass of another
print(issubclass(ElectricCar, Car))     # Output: True
print(issubclass(Car, Vehicle))         # Output: True
print(issubclass(ElectricCar, Vehicle)) # Output: True (multi-level!)
```

**Inheritance Hierarchy:**

```
        Animal
       /       \
     Dog       Cat
    /   \
 Puppy  GuardDog
```

**Key Concepts:**

1. **Parent/Base/Super class** - The class being inherited from
2. **Child/Derived/Sub class** - The class that inherits
3. **"is-a" relationship** - Dog IS-A Animal, Car IS-A Vehicle
4. Child gets ALL parent attributes and methods
5. Child can add its own unique features
6. You can have multi-level inheritance (grandparent → parent → child)

**What gets inherited:**
- ✅ Instance methods
- ✅ Class methods
- ✅ Static methods
- ✅ Class attributes
- ✅ Instance attributes (through `__init__`)

**What doesn't get inherited:**
- ❌ Private attributes starting with `__` (we'll learn about this in encapsulation)

### 🎯 Practice Question

Create a `Shape` parent class with an `__init__` that takes `color`. Then create two child classes:
- `Circle` with attribute `radius` and method `describe()`
- `Rectangle` with attributes `width`, `height` and method `describe()`

Both should print their color and specific properties.

<details>
<summary>Click to see solution</summary>

```python
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def describe(self):
        print(f"A {self.color} circle with radius {self.radius}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def describe(self):
        print(f"A {self.color} rectangle {self.width}x{self.height}")

circle = Circle("red", 5)
rectangle = Rectangle("blue", 10, 20)

circle.describe()     # Output: A red circle with radius 5
rectangle.describe()  # Output: A blue rectangle 10x20
```
</details>

---

## Chapter 10: Method Overriding and Using super()

### 1️⃣ WHY

**Why do we need method overriding?**

Sometimes a child class needs to do something DIFFERENTLY than its parent. For example:
- All animals eat, but Dogs eat differently than Birds
- All employees have salaries, but calculating bonuses might differ
- All shapes have areas, but calculating area differs for circles vs rectangles

**What problem does super() solve?**

`super()` lets you:
- Call the parent's method from within the child
- Avoid code duplication
- Extend parent functionality instead of completely replacing it

### 2️⃣ WHEN

**When to override methods:**
- Child needs different behavior than parent
- Need to customize inherited functionality
- Implementing abstract methods (we'll learn this in Chapter 15)

**When to use super():**
- Calling parent's `__init__` from child's `__init__`
- Extending (not replacing) parent's behavior
- Accessing parent's methods that were overridden

### 3️⃣ HOW

**What is method overriding?**

Method overriding is when a child class defines a method with the SAME NAME as one in the parent class. The child's version "overrides" (replaces) the parent's version.

**What is super()?**

`super()` is a built-in function that gives you access to methods in the parent class. It's like saying "Hey, call my parent's version of this method!"

**Example 1: Basic Method Overriding**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    # Override the speak method
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    # Override the speak method differently
    def speak(self):
        print(f"{self.name} says: Meow!")

# Create objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

animal.speak()  # Output: Generic Animal makes a sound
dog.speak()     # Output: Buddy says: Woof! (overridden!)
cat.speak()     # Output: Whiskers says: Meow! (overridden!)
```

**What's happening?**
- `Dog` and `Cat` inherit from `Animal`
- They both override the `speak()` method with their own versions
- When you call `dog.speak()`, Python uses Dog's version, not Animal's

**Example 2: Using super() to Extend Functionality**

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_details(self):
        return f"{self.name} - Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        # Call parent's __init__ using super()
        super().__init__(name, salary)
        # Then add child-specific attributes
        self.team_size = team_size
    
    def get_details(self):
        # Call parent's get_details() and ADD to it
        parent_details = super().get_details()
        return f"{parent_details} - Team Size: {self.team_size}"

class Developer(Employee):
    def __init__(self, name, salary, programming_languages):
        super().__init__(name, salary)
        self.programming_languages = programming_languages
    
    def get_details(self):
        parent_details = super().get_details()
        languages = ", ".join(self.programming_languages)
        return f"{parent_details} - Languages: {languages}"

# Create objects
manager = Manager("Alice", 100000, 5)
developer = Developer("Bob", 90000, ["Python", "JavaScript", "Go"])

print(manager.get_details())
# Output: Alice - Salary: $100000 - Team Size: 5

print(developer.get_details())
# Output: Bob - Salary: $90000 - Languages: Python, JavaScript, Go
```

**What's happening?**
- Manager and Developer call `super().__init__()` to set name and salary
- They override `get_details()` but use `super().get_details()` to get parent's info
- They EXTEND the parent's functionality instead of completely replacing it

**Example 3: Complete Override vs Partial Override**

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} is starting...")
        print("Engine starting...")

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    # Complete override - doesn't call parent's start()
    def start(self):
        print(f"{self.brand} {self.model} (Electric) is starting...")
        print("No engine sound - it's electric!")
        print(f"Battery: {self.battery_capacity}% charged")

class HybridCar(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
    
    # Partial override - extends parent's start()
    def start(self):
        super().start()  # Call parent's version first
        print(f"Running on {self.fuel_type}")  # Add extra functionality

# Test them
print("=== Regular Vehicle ===")
vehicle = Vehicle("Generic", "V100")
vehicle.start()
# Output:
# Generic V100 is starting...
# Engine starting...

print("\n=== Electric Car ===")
electric = ElectricCar("Tesla", "Model 3", 95)
electric.start()
# Output:
# Tesla Model 3 (Electric) is starting...
# No engine sound - it's electric!
# Battery: 95% charged

print("\n=== Hybrid Car ===")
hybrid = HybridCar("Toyota", "Prius", "Hybrid Electric")
hybrid.start()
# Output:
# Toyota Prius is starting...
# Engine starting...
# Running on Hybrid Electric
```

**Example 4: Common Pattern - Overriding __init__**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person __init__ called for {name}")

class Student(Person):
    def __init__(self, name, age, student_id, major):
        # ALWAYS call parent's __init__ when overriding!
        super().__init__(name, age)
        # Add child-specific initialization
        self.student_id = student_id
        self.major = major
        print(f"Student __init__ called for {name}")

student = Student("Emma", 20, "S12345", "Computer Science")
# Output:
# Person __init__ called for Emma
# Student __init__ called for Emma

print(f"{student.name}, Age: {student.age}")  # Inherited attributes work!
print(f"ID: {student.student_id}, Major: {student.major}")  # Child attributes work!
```

**Important super() Rules:**

```python
# ✅ CORRECT: Call super().__init__() in child's __init__
class Child(Parent):
    def __init__(self, parent_params, child_params):
        super().__init__(parent_params)  # Initialize parent first
        self.child_attribute = child_params  # Then child-specific stuff

# ❌ WRONG: Forgetting to call super().__init__()
class Child(Parent):
    def __init__(self, parent_params, child_params):
        # Oops! Parent's attributes won't be initialized!
        self.child_attribute = child_params

# ✅ CORRECT: Using super() to extend method
class Child(Parent):
    def some_method(self):
        super().some_method()  # Call parent's version
        # Add child-specific behavior

# ✅ CORRECT: Complete override (when you don't need parent's version)
class Child(Parent):
    def some_method(self):
        # Completely new behavior
        pass
```

**Method Resolution Order (Simple Version):**

When you call a method, Python looks for it in this order:
1. The object's class (child)
2. The parent class
3. The grandparent class (if any)
4. And so on up the hierarchy

```python
class Grandparent:
    def method(self):
        print("Grandparent's method")

class Parent(Grandparent):
    def method(self):
        print("Parent's method")

class Child(Parent):
    def method(self):
        print("Child's method")
        super().method()  # Calls Parent's method

child = Child()
child.method()
# Output:
# Child's method
# Parent's method
```

**Practical Example: Bank Accounts**

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds!")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. Balance: ${self.balance:.2f}")

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    # Override withdraw to allow overdraft
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print(f"Overdraft limit exceeded!")

# Use the accounts
savings = SavingsAccount("Alice", 1000, 0.05)
savings.deposit(500)       # Output: Deposited $500. Balance: $1500
savings.apply_interest()   # Output: Interest applied: $75.00. Balance: $1575.00

checking = CheckingAccount("Bob", 100, 500)
checking.withdraw(400)     # Output: Withdrew $400. Balance: $-300 (overdraft!)
checking.withdraw(300)     # Output: Overdraft limit exceeded!
```

### 🎯 Practice Question

Create a `Vehicle` class with a `move()` method that prints "Vehicle is moving". Then create:
- `Car` class that overrides `move()` to print "Car is driving"
- `Boat` class that overrides `move()` to print "Boat is sailing"
- `Plane` class that overrides `move()` but also calls the parent's `move()` first using `super()`

<details>
<summary>Click to see solution</summary>

```python
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing")

class Plane(Vehicle):
    def move(self):
        super().move()  # Call parent's method first
        print("Plane is flying")

car = Car()
boat = Boat()
plane = Plane()

car.move()    # Output: Car is driving
boat.move()   # Output: Boat is sailing
plane.move()  # Output: Vehicle is moving
              #         Plane is flying
```
</details>

---

## Chapter 11: Multiple Inheritance and Method Resolution Order (MRO)

### 1️⃣ WHY

**Why would we need multiple parents?**

Sometimes an object is a combination of multiple types:
- A `SmartPhone` IS-A `Phone` AND IS-A `Camera` AND IS-A `MusicPlayer`
- A `FlyingCar` IS-A `Car` AND IS-A `Aircraft`
- A `TeachingAssistant` IS-A `Student` AND IS-A `Employee`

Multiple inheritance lets one class inherit from multiple parent classes!

**What problems can it cause?**

The **Diamond Problem**: What if two parents have methods with the same name? Which one gets called? Python solves this with the Method Resolution Order (MRO).

### 2️⃣ WHEN

**When to use multiple inheritance:**
- An object truly "is-a" combination of multiple types
- Mixing in functionality (called "mixins")
- Following established patterns in frameworks

**When to avoid it:**
- If composition (has-a) makes more sense
- When it makes code confusing
- If you're just trying to reuse code (use composition instead!)

**Most Python programmers prefer composition over multiple inheritance!**

### 3️⃣ HOW

**Syntax for multiple inheritance:**

```python
class Child(Parent1, Parent2, Parent3):
    pass
```

**Example 1: Basic Multiple Inheritance**

```python
class Flyer:
    def fly(self):
        print("I can fly!")

class Swimmer:
    def swim(self):
        print("I can swim!")

class Duck(Flyer, Swimmer):  # Duck inherits from both!
    def quack(self):
        print("Quack!")

# Duck gets methods from both parents
duck = Duck()
duck.fly()    # Output: I can fly! (from Flyer)
duck.swim()   # Output: I can swim! (from Swimmer)
duck.quack()  # Output: Quack! (from Duck)
```

**Example 2: The Diamond Problem**

```python
class A:
    def method(self):
        print("Method from class A")

class B(A):
    def method(self):
        print("Method from class B")

class C(A):
    def method(self):
        print("Method from class C")

class D(B, C):  # D inherits from both B and C
    pass

# Which method() gets called?
d = D()
d.method()  # Output: Method from class B

# Why? Let's check the Method Resolution Order
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

**What's the MRO?**

The Method Resolution Order is the order Python searches for methods and attributes. It follows the **C3 linearization algorithm** (sounds scary but it's logical!).

**Simple rules:**
1. Check the class itself first
2. Check parents from left to right
3. Check grandparents (but in a smart way to avoid checking twice)

**Example 3: Understanding MRO with Mixins**

```python
class LoggerMixin:
    """Mixin to add logging capability"""
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampMixin:
    """Mixin to add timestamp capability"""
    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class SaverMixin:
    """Mixin to add save capability"""
    def save(self):
        print(f"Saving {self.__class__.__name__}...")

class Document(LoggerMixin, TimestampMixin, SaverMixin):
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.log(f"Document '{title}' created")
    
    def display(self):
        timestamp = self.get_timestamp()
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Time: {timestamp}")

# Document gets functionality from all mixins!
doc = Document("My Essay", "This is the content...")
# Output: [LOG] Document 'My Essay' created

doc.display()
# Output: Title: My Essay
#         Content: This is the content...
#         Time: 2024-01-04 10:30:45

doc.save()
# Output: Saving Document...
```

**Example 4: When Methods Overlap - Using super() with Multiple Inheritance**

```python
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person.__init__ called for {name}")

class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        print(f"Student.__init__ called for {student_id}")

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id
        print(f"Employee.__init__ called for {employee_id}")

# Teaching Assistant is both Student and Employee
class TeachingAssistant(Student, Employee, Person):
    def __init__(self, name, student_id, employee_id):
        # This is tricky! We need to call all parent __init__ methods
        Person.__init__(self, name)
        Student.__init__(self, student_id)
        Employee.__init__(self, employee_id)
        print("TeachingAssistant.__init__ completed")

ta = TeachingAssistant("Alice", "S123", "E456")
# Output:
# Person.__init__ called for Alice
# Student.__init__ called for S123
# Employee.__init__ called for E456
# TeachingAssistant.__init__ completed

print(f"Name: {ta.name}, Student: {ta.student_id}, Employee: {ta.employee_id}")
# Output: Name: Alice, Student: S123, Employee: E456
```

**Better way with super() (cooperative multiple inheritance):**

```python
class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)  # Pass remaining args up the chain
        print(f"Person.__init__ called for {name}")

class Student:
    def __init__(self, student_id, **kwargs):
        self.student_id = student_id
        super().__init__(**kwargs)
        print(f"Student.__init__ called for {student_id}")

class Employee:
    def __init__(self, employee_id, **kwargs):
        self.employee_id = employee_id
        super().__init__(**kwargs)
        print(f"Employee.__init__ called for {employee_id}")

class TeachingAssistant(Student, Employee, Person):
    def __init__(self, name, student_id, employee_id):
        super().__init__(
            name=name,
            student_id=student_id,
            employee_id=employee_id
        )
        print("TeachingAssistant.__init__ completed")

ta = TeachingAssistant("Bob", "S789", "E012")
print(TeachingAssistant.mro())  # Check the resolution order
```

**Example 5: Practical Use - Game Character with Abilities**

```python
class Attackable:
    def attack(self, target):
        print(f"{self.name} attacks {target}!")

class Defendable:
    def defend(self):
        print(f"{self.name} raises shield!")

class Healable:
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed for {amount} HP. Health: {self.health}")

class Magical:
    def cast_spell(self, spell):
        print(f"{self.name} casts {spell}!")

# Warrior can attack and defend
class Warrior(Attackable, Defendable):
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Healer can heal and cast spells
class Healer(Healable, Magical):
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Paladin can do EVERYTHING!
class Paladin(Attackable, Defendable, Healable, Magical):
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Test them
warrior = Warrior("Conan", 100)
warrior.attack("Goblin")  # Output: Conan attacks Goblin!
warrior.defend()          # Output: Conan raises shield!

healer = Healer("Elara", 80)
healer.heal(20)           # Output: Elara healed for 20 HP. Health: 100
healer.cast_spell("Heal") # Output: Elara casts Heal!

paladin = Paladin("Arthas", 120)
paladin.attack("Dragon")      # Output: Arthas attacks Dragon!
paladin.defend()              # Output: Arthas raises shield!
paladin.heal(10)              # Output: Arthas healed for 10 HP. Health: 130
paladin.cast_spell("Smite")   # Output: Arthas casts Smite!
```

**Checking Inheritance:**

```python
print(isinstance(paladin, Paladin))    # Output: True
print(isinstance(paladin, Attackable)) # Output: True
print(isinstance(paladin, Magical))    # Output: True

print(issubclass(Paladin, Attackable)) # Output: True
print(issubclass(Paladin, Magical))    # Output: True
```

**When Multiple Inheritance Gets Confusing:**

```python
# ❌ BAD: Confusing multiple inheritance
class Database:
    def connect(self): pass

class Logger:
    def log(self): pass

class Network:
    def send(self): pass

class ComplexSystem(Database, Logger, Network):
    # This is getting messy! Consider composition instead
    pass

# ✅ BETTER: Use composition
class ComplexSystemComposition:
    def __init__(self):
        self.database = Database()
        self.logger = Logger()
        self.network = Network()
```

**Key Points:**

1. Multiple inheritance: `class Child(Parent1, Parent2)`
2. MRO determines which method gets called when names overlap
3. Check MRO with `ClassName.mro()` or `ClassName.__mro__`
4. **Mixins** are small classes designed to add one specific functionality
5. Use `super()` carefully with multiple inheritance
6. **When in doubt, prefer composition over inheritance!**

### 🎯 Practice Question

Create a `Reader` class with a `read()` method and a `Writer` class with a `write()` method. Then create a `FileEditor` class that inherits from both and can both read and write. Add a method `edit()` that calls both read and write.

<details>
<summary>Click to see solution</summary>

```python
class Reader:
    def read(self):
        print("Reading content...")

class Writer:
    def write(self):
        print("Writing content...")

class FileEditor(Reader, Writer):
    def edit(self):
        print("Editing file:")
        self.read()
        self.write()
        print("Edit complete!")

editor = FileEditor()
editor.read()   # Output: Reading content...
editor.write()  # Output: Writing content...
editor.edit()   # Output: Editing file:
                #         Reading content...
                #         Writing content...
                #         Edit complete!

# Check MRO
print(FileEditor.mro())
```
</details>

---

## Chapter 12: Polymorphism - Duck Typing and Method Overriding in Action

### 1️⃣ WHY

**Why do we need polymorphism?**

Imagine you're building a zoo app where different animals make sounds. Without polymorphism:

```python
if animal_type == "dog":
    dog_bark()
elif animal_type == "cat":
    cat_meow()
elif animal_type == "duck":
    duck_quack()
# ... 100 more animals!
```

With polymorphism:
```python
animal.speak()  # Works for ANY animal!
```

**What problem does it solve?**

- **Flexibility**: Write code that works with many types
- **Extensibility**: Add new types without changing existing code
- **Simplicity**: One interface, many implementations

### 2️⃣ WHEN

**When to use polymorphism:**
- Multiple classes share a common interface
- You want to treat different objects uniformly
- Writing extensible, plugin-based systems
- Implementing strategies or behaviors

**Real-world examples:**
- Different payment methods (credit card, PayPal, crypto) but same `process_payment()` interface
- Different file formats (PDF, DOCX, TXT) but same `open()` interface
- Different shapes (circle, square, triangle) but same `calculate_area()` interface

### 3️⃣ HOW

**What is polymorphism?**

Poly = Many, Morph = Forms. **Polymorphism** means "many forms" - the ability to use a single interface to represent different types.

In Python, there are two main types:
1. **Method overriding** (inheritance-based)
2. **Duck typing** (Python's special feature)

**Python's motto: "If it walks like a duck and quacks like a duck, it's a duck!"**

You don't need inheritance for polymorphism in Python - you just need the right methods!

**Example 1: Polymorphism with Inheritance**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # Base implementation (will be overridden)

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

class Duck(Animal):
    def speak(self):
        return f"{self.name} says: Quack!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says: Moo!"

# Polymorphism in action!
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Duck("Donald"),
    Cow("Bessie")
]

# Same method call works for ALL animals!
for animal in animals:
    print(animal.speak())

# Output:
# Buddy says: Woof!
# Whiskers says: Meow!
# Donald says: Quack!
# Bessie says: Moo!
```

**What's magical here?**
- We call `speak()` on every animal
- Each animal responds differently
- The code doesn't need to know what TYPE of animal it is!

**Example 2: Duck Typing (Python's Superpower!)**

```python
# These classes are NOT related (no inheritance)
# But they all have a "fly()" method!

class Bird:
    def fly(self):
        print("Bird flies with wings")

class Airplane:
    def fly(self):
        print("Airplane flies with engines")

class Superman:
    def fly(self):
        print("Superman flies with superpowers")

class Drone:
    def fly(self):
        print("Drone flies with propellers")

# This function doesn't care WHAT type the object is
# It only cares that it HAS a fly() method!
def make_it_fly(flying_thing):
    flying_thing.fly()

# All of these work!
bird = Bird()
plane = Airplane()
superman = Superman()
drone = Drone()

make_it_fly(bird)      # Output: Bird flies with wings
make_it_fly(plane)     # Output: Airplane flies with engines
make_it_fly(superman)  # Output: Superman flies with superpowers
make_it_fly(drone)     # Output: Drone flies with propellers

# This is DUCK TYPING!
# If it has a fly() method, we can call it!
```

**Example 3: Real-World Example - Payment Processing**

```python
class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
    
    def process_payment(self, amount):
        print(f"Processing ${amount} via Credit Card {self.card_number}")
        return True

class PayPal:
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal account {self.email}")
        return True

class Cryptocurrency:
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def process_payment(self, amount):
        print(f"Processing ${amount} via Crypto wallet {self.wallet_address}")
        return True

class Cash:
    def process_payment(self, amount):
        print(f"Processing ${amount} in cash")
        return True

# E-commerce checkout system
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
        self.total += price
    
    def checkout(self, payment_method):
        # This works with ANY payment method that has process_payment()!
        print(f"\nTotal: ${self.total}")
        if payment_method.process_payment(self.total):
            print("Payment successful! Order confirmed.")
        else:
            print("Payment failed!")

# Test with different payment methods
cart1 = ShoppingCart()
cart1.add_item("Laptop", 999)
cart1.add_item("Mouse", 25)
cart1.checkout(CreditCard("1234-5678-9012"))

cart2 = ShoppingCart()
cart2.add_item("Book", 15)
cart2.checkout(PayPal("user@email.com"))

cart3 = ShoppingCart()
cart3.add_item("Coffee", 5)
cart3.checkout(Cryptocurrency("0x123abc"))

# Output shows polymorphism in action!
# Same checkout() method works with ANY payment type!
```

**Example 4: Shapes with Area Calculation**

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def describe(self):
        return f"Circle with radius {self.radius}"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def describe(self):
        return f"Rectangle {self.width}x{self.height}"

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def describe(self):
        return f"Triangle with base {self.base} and height {self.height}"

# Function that works with ANY shape!
def print_shape_info(shape):
    print(f"{shape.describe()}")
    print(f"Area: {shape.area():.2f}")
    print()

# Create shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8),
    Circle(10),
    Rectangle(5, 5)
]

# Process all shapes uniformly
total_area = 0
for shape in shapes:
    print_shape_info(shape)
    total_area += shape.area()

print(f"Total area of all shapes: {total_area:.2f}")
```

**Example 5: File Readers (No Inheritance Needed!)**

```python
class TextFileReader:
    def read(self, filename):
        print(f"Reading text from {filename}")
        return f"Text content from {filename}"

class CSVReader:
    def read(self, filename):
        print(f"Parsing CSV from {filename}")
        return f"CSV data from {filename}"

class JSONReader:
    def read(self, filename):
        print(f"Parsing JSON from {filename}")
        return f"JSON data from {filename}"

class XMLReader:
    def read(self, filename):
        print(f"Parsing XML from {filename}")
        return f"XML data from {filename}"

# Generic file processor
def process_file(reader, filename):
    # Works with ANY reader that has a read() method!
    content = reader.read(filename)
    print(f"Processing: {content}\n")

# Use different readers
process_file(TextFileReader(), "document.txt")
process_file(CSVReader(), "data.csv")
process_file(JSONReader(), "config.json")
process_file(XMLReader(), "settings.xml")
```

**The Power of Polymorphism:**

```python
# Without polymorphism - rigid and hard to extend
def process_payment_old(method, amount):
    if method == "credit_card":
        # credit card logic
        pass
    elif method == "paypal":
        # paypal logic
        pass
    elif method == "crypto":
        # crypto logic
        pass
    # Adding new method? Must modify this function!

# With polymorphism - flexible and extensible
def process_payment_new(payment_method, amount):
    payment_method.process_payment(amount)
    # Adding new method? Just create a new class with process_payment()!
    # No need to modify this function!
```

**Key Concepts:**

1. **Polymorphism** = same interface, different implementations
2. **Duck typing** = if it has the right methods, it works (no inheritance needed)
3. **Method overriding** = child classes provide different implementations
4. Write code that depends on **interfaces** (methods), not **types** (classes)
5. "Program to an interface, not an implementation"

**Benefits:**

- ✅ More flexible code
- ✅ Easier to extend (add new types)
- ✅ Follows "Open-Closed Principle" (open for extension, closed for modification)
- ✅ More maintainable

### 🎯 Practice Question

Create three unrelated classes: `Dog`, `Car`, and `Phone`. Each should have a `start()` method that prints something unique. Then write a function `activate(thing)` that calls `thing.start()`, demonstrating duck typing.

<details>
<summary>Click to see solution</summary>

```python
class Dog:
    def start(self):
        print("Dog starts barking!")

class Car:
    def start(self):
        print("Car engine starts!")

class Phone:
    def start(self):
        print("Phone boots up!")

def activate(thing):
    # Works with anything that has a start() method!
    thing.start()

dog = Dog()
car = Car()
phone = Phone()

activate(dog)    # Output: Dog starts barking!
activate(car)    # Output: Car engine starts!
activate(phone)  # Output: Phone boots up!

# This is duck typing and polymorphism in action!
```
</details>

---

## Chapter 13: Encapsulation - Private Attributes and Name Mangling

### 1️⃣ WHY

**Why do we need encapsulation?**

Imagine you have a bank account. You wouldn't want anyone to directly change your balance to a million dollars, right? You want controlled access through methods like `deposit()` and `withdraw()`.

**What problem does encapsulation solve?**

- **Data protection**: Prevent accidental modification of important data
- **Validation**: Control how data is accessed and modified
- **Implementation hiding**: Change internal code without breaking external code
- **Maintain invariants**: Ensure object stays in valid state

### 2️⃣ WHEN

**When to use encapsulation:**
- Data needs validation before being set
- You want to hide implementation details
- Protecting critical data (passwords, balances, internal state)
- When you might change how data is stored internally

**When it's less important:**
- Simple data containers
- Internal classes not exposed to users
- When transparency is more important than protection

### 3️⃣ HOW

**What is encapsulation?**

Encapsulation means:
1. **Bundling** data and methods together (we've been doing this!)
2. **Hiding** internal details (private attributes/methods)
3. **Controlling access** through public methods

**Python's privacy levels:**

1. **Public**: `name` - accessible everywhere
2. **Protected**: `_name` - "internal use, but not enforced" (convention only!)
3. **Private**: `__name` - name mangling makes it harder to access

**Note: Python doesn't have true private members! It's more like "please don't touch this" rather than "you absolutely can't touch this".**

**Example 1: Public vs Protected vs Private**

```python
class Example:
    def __init__(self):
        self.public = "I'm public - use me!"
        self._protected = "I'm protected - use carefully"
        self.__private = "I'm private - don't touch!"
    
    def get_private(self):
        # Methods inside the class CAN access private attributes
        return self.__private
    
    def set_private(self, value):
        self.__private = value

obj = Example()

# Public - works fine
print(obj.public)  # Output: I'm public - use me!

# Protected - works, but you shouldn't (just a convention)
print(obj._protected)  # Output: I'm protected - use carefully

# Private - doesn't work directly!
try:
    print(obj.__private)
except AttributeError as e:
    print(f"Error: {e}")
# Output: Error: 'Example' object has no attribute '__private'

# But you CAN access through methods
print(obj.get_private())  # Output: I'm private - don't touch!

# Name mangling: Python actually renames it!
print(obj._Example__private)  # Output: I'm private - don't touch!
# (But don't do this - it defeats the purpose!)
```

**Example 2: Practical Encapsulation - Bank Account**

```python
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner  # Public
        self.__balance = initial_balance  # Private!
        self.__transaction_history = []  # Private!
    
    # Public method to safely deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited: ${amount}")
            print(f"Deposited ${amount}. Balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive!")
    
    # Public method to safely withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew: ${amount}")
            print(f"Withdrew ${amount}. Balance: ${self.__balance}")
    
    # Public method to check balance (read-only)
    def get_balance(self):
        return self.__balance
    
    # Public method to view history
    def get_transaction_history(self):
        return self.__transaction_history.copy()  # Return a copy, not the original!

# Using the account
account = BankAccount("Alice", 1000)

# Can't directly modify balance (protected!)
# account.__balance = 1000000  # This won't work!

# Must use methods (controlled access)
account.deposit(500)     # Output: Deposited $500. Balance: $1500
account.withdraw(200)    # Output: Withdrew $200. Balance: $1300
account.withdraw(2000)   # Output: Insufficient funds!

# Can check balance (read-only)
print(f"Balance: ${account.get_balance()}")  # Output: Balance: $1300

# Can view history
for transaction in account.get_transaction_history():
    print(transaction)
# Output:
# Deposited: $500
# Withdrew: $200
```

**Why is this better?**
- Can't accidentally set balance to negative
- Can't set balance to invalid value
- All changes go through validation
- Can track all transactions

**Example 3: Protecting Data with Validation**

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = None  # Will be set through method
        self.set_age(age)  # Use method for validation
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name!")
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 150:
            self.__age = age
        else:
            print(f"Invalid age: {age}. Must be between 0 and 150.")
    
    def have_birthday(self):
        self.__age += 1
        print(f"Happy birthday! {self.__name} is now {self.__age}!")

person = Person("Alice", 25)

# Can't directly set invalid age
person.set_age(200)      # Output: Invalid age: 200. Must be between 0 and 150.
person.set_age(-5)       # Output: Invalid age: -5. Must be between 0 and 150.
person.set_age(30)       # Valid - no error

print(person.get_age())  # Output: 30

person.have_birthday()   # Output: Happy birthday! Alice is now 31!
```

**Example 4: Name Mangling in Inheritance**

```python
class Parent:
    def __init__(self):
        self.__private_var = "Parent's private"
        self._protected_var = "Parent's protected"
    
    def __private_method(self):
        return "Parent's private method"
    
    def _protected_method(self):
        return "Parent's protected method"
    
    def public_method(self):
        # Can access own private stuff
        print(self.__private_var)
        print(self.__private_method())

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private_var = "Child's private"  # Different from parent's!
    
    def test(self):
        # Can access protected
        print(self._protected_var)  # Works!
        
        # Can't access parent's private (name mangled differently)
        try:
            print(self.__private_var)  # This is CHILD's private, not parent's
        except AttributeError:
            print("Can't access parent's private")

child = Child()
child.public_method()
# Output:
# Parent's private
# Parent's private method

child.test()
# Output:
# Parent's protected
# Child's private
```

**Example 5: When Encapsulation Helps - Password Storage**

```python
class User:
    def __init__(self, username, password):
        self.username = username  # Public
        self.__password_hash = self.__hash_password(password)  # Private!
    
    def __hash_password(self, password):
        # Simplified hash (in reality, use proper hashing like bcrypt)
        return hash(password)
    
    def check_password(self, password):
        return self.__hash_password(password) == self.__password_hash
    
    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            if len(new_password) >= 8:
                self.__password_hash = self.__hash_password(new_password)
                print("Password changed successfully!")
            else:
                print("New password must be at least 8 characters!")
        else:
            print("Incorrect old password!")

user = User("alice", "secret123")

# Can't see the password!
# print(user.__password)  # Won't work!

# Can check if password is correct
print(user.check_password("wrong"))      # Output: False
print(user.check_password("secret123"))  # Output: True

# Can change password with validation
user.change_password("wrong", "new_pass")  # Output: Incorrect old password!
user.change_password("secret123", "short") # Output: New password must be at least 8 characters!
user.change_password("secret123", "newsecret123")  # Output: Password changed successfully!
```

**Guidelines for Encapsulation:**

```python
class GoodExample:
    def __init__(self):
        # Use public for simple, safe attributes
        self.id = 1
        self.name = "Example"
        
        # Use _protected for internal stuff (convention: "don't use unless you know what you're doing")
        self._internal_cache = {}
        
        # Use __private for truly sensitive data that needs protection
        self.__password = "secret"
    
    # Provide public methods for controlled access
    def get_password_hash(self):
        return hash(self.__password)
    
    def verify_password(self, password):
        return password == self.__password
```

**The truth about Python privacy:**

```python
class Secret:
    def __init__(self):
        self.__secret = "Hidden!"

obj = Secret()

# Python "privacy" is more like a suggestion
# You CAN access it if you really want (but you shouldn't!)
print(obj._Secret__secret)  # Output: Hidden!

# Python's philosophy: "We're all consenting adults here"
# Private attributes are to prevent accidents, not malicious access
```

**Key Points:**

1. **Public** (`name`) - use freely
2. **Protected** (`_name`) - internal use (convention only)
3. **Private** (`__name`) - name mangling makes it harder to access
4. Python doesn't enforce privacy strictly (unlike Java/C++)
5. Use encapsulation to:
   - Validate data
   - Hide implementation details
   - Maintain object invariants
6. Provide public methods (getters/setters) for controlled access

### 🎯 Practice Question

Create a `Rectangle` class with private attributes `__width` and `__height`. Provide methods:
- `set_width(w)` and `set_height(h)` that only accept positive numbers
- `get_area()` that calculates and returns the area
- `get_perimeter()` that calculates and returns the perimeter

<details>
<summary>Click to see solution</summary>

```python
class Rectangle:
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.set_width(width)
        self.set_height(height)
    
    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width must be positive!")
    
    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("Height must be positive!")
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def get_area(self):
        return self.__width * self.__height
    
    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

rect = Rectangle(5, 10)
print(f"Area: {rect.get_area()}")         # Output: Area: 50
print(f"Perimeter: {rect.get_perimeter()}")  # Output: Perimeter: 30

rect.set_width(-5)  # Output: Width must be positive!
rect.set_width(8)   # Valid
print(f"New area: {rect.get_area()}")     # Output: New area: 80
```
</details>

---

[Continuing in next part due to length...]

## Chapter 14: Properties - Getters and Setters with @property

### 1️⃣ WHY

**Why do we need properties?**

In Chapter 13, we used methods like `get_balance()` and `set_age()`. This works, but it's not very Pythonic:

```python
person.set_age(25)  # Feels clunky
balance = account.get_balance()  # Verbose
```

Wouldn't it be nicer to write:
```python
person.age = 25  # Clean!
balance = account.balance  # Simple!
```

**But wait!** If we make them public attributes, we lose validation and control!

**Solution: Properties!** They look like attributes but act like methods!

### 2️⃣ WHEN

**When to use properties:**
- You want attribute-like syntax with method-like control
- Adding validation to attribute access
- Computed attributes (calculated on-the-fly)
- Maintaining backward compatibility (turn attributes into properties)

**When regular attributes are fine:**
- Simple data with no validation needed
- No computation required
- Direct access is appropriate

### 3️⃣ HOW

**What is @property?**

The `@property` decorator lets you define methods that can be accessed like attributes. You get:
- **Getter** - reading the value
- **Setter** - setting the value (with validation!)
- **Deleter** - deleting the value (less common)

**Example 1: Basic Property**

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # Getter - makes it readable like an attribute
    @property
    def age(self):
        return self._age
    
    # Setter - makes it writable with validation
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer!")
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150!")
        self._age = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string!")
        self._name = value

# Use it like regular attributes!
person = Person("Alice", 25)

# Reading (calls getter)
print(person.age)   # Output: 25
print(person.name)  # Output: Alice

# Writing (calls setter with validation)
person.age = 30     # Works!
print(person.age)   # Output: 30

# Validation in action
try:
    person.age = -5  # Raises ValueError!
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Age must be between 0 and 150!

try:
    person.age = "thirty"  # Raises TypeError!
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: Age must be an integer!
```

**What's happening?**
- `person.age` looks like an attribute but calls the getter method
- `person.age = 30` looks like assignment but calls the setter method
- The setter validates the value before storing it!

**Example 2: Computed Properties (Calculated on Access)**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # These are computed properties - calculated when accessed
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    @property
    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

rect = Rectangle(5, 10)

# Look like attributes, but calculated each time!
print(f"Area: {rect.area}")         # Output: Area: 50
print(f"Perimeter: {rect.perimeter}")  # Output: Perimeter: 30
print(f"Diagonal: {rect.diagonal:.2f}")  # Output: Diagonal: 11.18

# Change dimensions - properties update automatically!
rect.width = 8
print(f"New area: {rect.area}")     # Output: New area: 80
```

**Why is this better than storing area as an attribute?**
- Area is always correct (automatically recalculated)
- No need to update area manually when width/height changes
- Saves memory (no need to store calculated values)

**Example 3: Temperature Converter**

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        # Computed from celsius
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        # Convert and store as celsius
        if value < -459.67:  # Absolute zero in Fahrenheit
            raise ValueError("Temperature below absolute zero!")
        self._celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        if value < 0:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value - 273.15

# Create temperature
temp = Temperature(25)
print(f"Celsius: {temp.celsius}")      # Output: Celsius: 25
print(f"Fahrenheit: {temp.fahrenheit}")  # Output: Fahrenheit: 77.0
print(f"Kelvin: {temp.kelvin}")        # Output: Kelvin: 298.15

# Set in Fahrenheit - automatically converts!
temp.fahrenheit = 100
print(f"Celsius: {temp.celsius:.2f}")  # Output: Celsius: 37.78

# Set in Kelvin - automatically converts!
temp.kelvin = 300
print(f"Celsius: {temp.celsius:.2f}")  # Output: Celsius: 26.85
print(f"Fahrenheit: {temp.fahrenheit:.2f}")  # Output: Fahrenheit: 80.33
```

**Example 4: Read-Only Property (No Setter)**

```python
import datetime

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    @property
    def age(self):
        # Read-only property (no setter)
        current_year = datetime.datetime.now().year
        return current_year - self.birth_year
    
    # If you try to set it, you'll get an error
    # @age.setter would allow setting, but we don't define it!

person = Person("Alice", 1995)
print(f"{person.name} is {person.age} years old")

# Age updates automatically based on current year
# Can't set age directly
try:
    person.age = 30  # Will fail!
except AttributeError as e:
    print(f"Error: can't set attribute")

# But can change birth_year
person.birth_year = 1990
print(f"Updated age: {person.age}")
```

**Example 5: Deleter (Bonus!)**

```python
class Email:
    def __init__(self, address):
        self._address = address
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        if '@' not in value:
            raise ValueError("Invalid email address!")
        self._address = value
    
    @address.deleter
    def address(self):
        print("Deleting email address...")
        del self._address

email = Email("user@example.com")
print(email.address)  # Output: user@example.com

# Delete the email
del email.address     # Output: Deleting email address...

# Now it's gone
try:
    print(email.address)  # Will error!
except AttributeError:
    print("Email address was deleted")
```

**Example 6: Real-World Use Case - Bank Account**

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self._transaction_count = 0
    
    @property
    def balance(self):
        # Read-only from outside, but we can access internally
        return self._balance
    
    # No balance setter - must use deposit/withdraw!
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self._balance += amount
        self._transaction_count += 1
        print(f"Deposited ${amount}. New balance: ${self._balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive!")
        if amount > self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount
        self._transaction_count += 1
        print(f"Withdrew ${amount}. New balance: ${self._balance}")
    
    @property
    def transaction_count(self):
        # Read-only property
        return self._transaction_count

account = BankAccount("Alice", 1000)

# Can read balance (looks like an attribute)
print(f"Balance: ${account.balance}")  # Output: Balance: $1000

# Can't set balance directly!
try:
    account.balance = 5000  # Won't work!
except AttributeError:
    print("Can't directly modify balance!")

# Must use methods
account.deposit(500)   # Output: Deposited $500. New balance: $1500
account.withdraw(200)  # Output: Withdrew $200. New balance: $1300

print(f"Transactions: {account.transaction_count}")  # Output: Transactions: 2
```

**Comparing Approaches:**

```python
# ❌ Bad: Public attributes (no validation)
class PersonBad:
    def __init__(self, name, age):
        self.age = age  # Anyone can set to invalid value!

# ❌ Awkward: Using methods
class PersonMethods:
    def __init__(self, name, age):
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age can't be negative!")
        self._age = age

# ✅ Best: Using properties
class PersonGood:
    def __init__(self, name, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age can't be negative!")
        self._age = age

# Usage comparison
p1 = PersonMethods("Alice", 25)
p1.set_age(30)  # Clunky
age = p1.get_age()

p2 = PersonGood("Bob", 25)
p2.age = 30  # Clean and Pythonic!
age = p2.age
```

**Key Points:**

1. **@property** makes methods look like attributes
2. **Getter** (`@property`) - read access
3. **Setter** (`@property_name.setter`) - write access with validation
4. **Deleter** (`@property_name.deleter`) - handle deletion
5. Properties can be **computed** (calculated) or **stored**
6. Read-only properties: define getter but no setter
7. Properties = attribute syntax + method control

**Mental Model:**

Properties are like a receptionist at a hotel:
- You ask for your room key (getter) - looks simple
- Behind the scenes, they check records, verify identity
- You want to change rooms (setter) - looks simple
- Behind the scenes, they validate availability, update records

### 🎯 Practice Question

Create a `Circle` class with:
- Private attribute `_radius`
- Property `radius` with getter and setter (setter validates radius > 0)
- Read-only properties `diameter`, `circumference`, and `area`

<details>
<summary>Click to see solution</summary>

```python
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive!")
        self._radius = value
    
    @property
    def diameter(self):
        return self._radius * 2
    
    @property
    def circumference(self):
        return 2 * math.pi * self._radius
    
    @property
    def area(self):
        return math.pi * self._radius ** 2

circle = Circle(5)
print(f"Radius: {circle.radius}")               # Output: Radius: 5
print(f"Diameter: {circle.diameter}")           # Output: Diameter: 10
print(f"Circumference: {circle.circumference:.2f}")  # Output: Circumference: 31.42
print(f"Area: {circle.area:.2f}")               # Output: Area: 78.54

circle.radius = 10
print(f"New area: {circle.area:.2f}")           # Output: New area: 314.16
```
</details>

---

## Chapter 15: Abstraction - Abstract Classes and the ABC Module

### 1️⃣ WHY

**Why do we need abstraction?**

Imagine you're creating a drawing application. You have:
- Circles
- Rectangles
- Triangles

They all need a `draw()` method. But what would a generic "Shape" look like? You can't actually draw a generic shape - it's an abstract concept!

**What problem does abstraction solve?**

- **Forces subclasses to implement required methods**
- **Creates contracts/interfaces** that classes must follow
- **Prevents instantiation of incomplete classes**
- **Documents requirements clearly**

### 2️⃣ WHEN

**When to use abstract classes:**
- Defining a common interface for multiple classes
- Creating a template that subclasses must follow
- You want to prevent direct instantiation of base class
- Framework/library design where others will extend your classes

**When NOT to use them:**
- Simple projects where duck typing is enough
- When you need multiple interface inheritance (use regular classes)
- Over-engineering simple problems

### 3️⃣ HOW

**What is abstraction?**

Abstraction means hiding complex implementation details and showing only the essential features. An **abstract class** is a blueprint that:
1. Cannot be instantiated directly
2. May contain abstract methods (must be implemented by subclasses)
3. May contain concrete methods (regular methods with implementation)

**Python's ABC Module:**

```python
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def required_method(self):
        pass  # Subclasses MUST implement this
```

**Example 1: Basic Abstract Class**

```python
from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        # Abstract method - no implementation
        # Subclasses MUST implement this
        pass
    
    @abstractmethod
    def move(self):
        # Another abstract method
        pass
    
    # Concrete method - has implementation
    def eat(self):
        print(f"{self.name} is eating")

# Try to create an Animal directly
try:
    animal = Animal("Generic")  # This will fail!
except TypeError as e:
    print(f"Error: {e}")
# Output: Error: Can't instantiate abstract class Animal with abstract methods move, speak

# Concrete subclass - implements all abstract methods
class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"
    
    def move(self):
        return f"{self.name} runs on four legs"

class Bird(Animal):
    def speak(self):
        return f"{self.name} says: Chirp!"
    
    def move(self):
        return f"{self.name} flies in the sky"

# Now we can create dogs and birds!
dog = Dog("Buddy")
bird = Bird("Tweety")

print(dog.speak())  # Output: Buddy says: Woof!
print(dog.move())   # Output: Buddy runs on four legs
dog.eat()           # Output: Buddy is eating

print(bird.speak()) # Output: Tweety says: Chirp!
print(bird.move())  # Output: Tweety flies in the sky
bird.eat()          # Output: Tweety is eating
```

**What happens if you forget to implement an abstract method?**

```python
class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"
    
    # Oops! Forgot to implement move()

try:
    cat = Cat("Whiskers")  # This will fail!
except TypeError as e:
    print(f"Error: {e}")
# Output: Error: Can't instantiate abstract class Cat with abstract method move
```

**Example 2: Shape Hierarchy**

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate and return the area"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter"""
        pass
    
    # Concrete method (all shapes can use this)
    def describe(self):
        return f"{self.__class__.__name__} - Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

# Create shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

# Process all shapes uniformly
for shape in shapes:
    print(shape.describe())

# Output:
# Circle - Area: 78.54, Perimeter: 31.42
# Rectangle - Area: 24.00, Perimeter: 20.00
# Triangle - Area: 6.00, Perimeter: 12.00
```

**Example 3: Payment Processing System**

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Process a payment of the given amount"""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id, amount):
        """Refund a payment"""
        pass
    
    # Concrete method - validation logic shared by all
    def validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        return True

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.validate_amount(amount)
        print(f"Processing ${amount} via Credit Card")
        # In real code: connect to payment gateway, etc.
        return {"status": "success", "transaction_id": "CC123"}
    
    def refund_payment(self, transaction_id, amount):
        self.validate_amount(amount)
        print(f"Refunding ${amount} to Credit Card (Transaction: {transaction_id})")
        return {"status": "refunded"}

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.validate_amount(amount)
        print(f"Processing ${amount} via PayPal")
        return {"status": "success", "transaction_id": "PP456"}
    
    def refund_payment(self, transaction_id, amount):
        self.validate_amount(amount)
        print(f"Refunding ${amount} to PayPal (Transaction: {transaction_id})")
        return {"status": "refunded"}

class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.validate_amount(amount)
        print(f"Processing ${amount} via Cryptocurrency")
        return {"status": "pending", "transaction_id": "CRYPTO789"}
    
    def refund_payment(self, transaction_id, amount):
        self.validate_amount(amount)
        print(f"Refunding ${amount} via Cryptocurrency (Transaction: {transaction_id})")
        return {"status": "refunded"}

# Function that works with ANY payment processor
def checkout(processor: PaymentProcessor, amount: float):
    print(f"\n--- Checkout: ${amount} ---")
    result = processor.process_payment(amount)
    print(f"Result: {result}")

# Use different processors
checkout(CreditCardProcessor(), 99.99)
checkout(PayPalProcessor(), 49.99)
checkout(CryptoProcessor(), 199.99)

# Output:
# --- Checkout: $99.99 ---
# Processing $99.99 via Credit Card
# Result: {'status': 'success', 'transaction_id': 'CC123'}
# 
# --- Checkout: $49.99 ---
# Processing $49.99 via PayPal
# Result: {'status': 'success', 'transaction_id': 'PP456'}
# 
# --- Checkout: $199.99 ---
# Processing $199.99 via Cryptocurrency
# Result: {'status': 'pending', 'transaction_id': 'CRYPTO789'}
```

**Example 4: Database Connection Interface**

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass
    
    def log(self, message):
        # Concrete method - shared logging
        print(f"[DB LOG] {message}")

class MySQLDatabase(Database):
    def connect(self):
        self.log("Connecting to MySQL...")
        # In real code: establish MySQL connection
        print("MySQL connected!")
    
    def disconnect(self):
        self.log("Disconnecting from MySQL...")
        print("MySQL disconnected!")
    
    def execute_query(self, query):
        self.log(f"Executing MySQL query: {query}")
        # In real code: run the query
        return {"result": "MySQL data"}

class PostgreSQLDatabase(Database):
    def connect(self):
        self.log("Connecting to PostgreSQL...")
        print("PostgreSQL connected!")
    
    def disconnect(self):
        self.log("Disconnecting from PostgreSQL...")
        print("PostgreSQL disconnected!")
    
    def execute_query(self, query):
        self.log(f"Executing PostgreSQL query: {query}")
        return {"result": "PostgreSQL data"}

class MongoDatabase(Database):
    def connect(self):
        self.log("Connecting to MongoDB...")
        print("MongoDB connected!")
    
    def disconnect(self):
        self.log("Disconnecting from MongoDB...")
        print("MongoDB disconnected!")
    
    def execute_query(self, query):
        self.log(f"Executing MongoDB query: {query}")
        return {"result": "MongoDB data"}

# Application code that works with any database!
def run_application(db: Database):
    db.connect()
    result = db.execute_query("SELECT * FROM users")
    print(f"Got: {result}")
    db.disconnect()

# Swap databases easily!
print("=== Using MySQL ===")
run_application(MySQLDatabase())

print("\n=== Using PostgreSQL ===")
run_application(PostgreSQLDatabase())

print("\n=== Using MongoDB ===")
run_application(MongoDatabase())
```

**Example 5: Abstract Properties**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @property
    @abstractmethod
    def max_speed(self):
        """Maximum speed of the vehicle"""
        pass
    
    @property
    @abstractmethod
    def fuel_type(self):
        """Type of fuel the vehicle uses"""
        pass
    
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    @property
    def max_speed(self):
        return 200
    
    @property
    def fuel_type(self):
        return "Gasoline"
    
    def start(self):
        print("Car engine starting...")

class Bicycle(Vehicle):
    @property
    def max_speed(self):
        return 30
    
    @property
    def fuel_type(self):
        return "Human power"
    
    def start(self):
        print("Start pedaling...")

car = Car()
bike = Bicycle()

print(f"Car: Max speed = {car.max_speed} km/h, Fuel = {car.fuel_type}")
print(f"Bike: Max speed = {bike.max_speed} km/h, Fuel = {bike.fuel_type}")

car.start()   # Output: Car engine starting...
bike.start()  # Output: Start pedaling...
```

**Comparison: Abstract Class vs Regular Class**

```python
# Regular class - can be instantiated even if incomplete
class RegularShape:
    def area(self):
        pass  # Empty implementation

shape = RegularShape()  # Works! But area() does nothing
print(shape.area())  # Output: None (not helpful!)

# Abstract class - prevents instantiation of incomplete classes
from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

# This FAILS - can't create abstract class instance
try:
    shape = AbstractShape()
except TypeError as e:
    print(f"Prevented: {e}")
```

**Key Points:**

1. **Abstract classes** can't be instantiated directly
2. Use `from abc import ABC, abstractmethod`
3. **@abstractmethod** decorator marks methods that subclasses MUST implement
4. Abstract classes can have:
   - Abstract methods (no implementation)
   - Concrete methods (with implementation)
   - Abstract properties
5. Subclasses must implement ALL abstract methods
6. Forces a contract - guarantees certain methods exist
7. Great for framework design and large applications

**When to use what:**

| Scenario | Use |
|----------|-----|
| Just need duck typing | No abstract class needed |
| Want to document expected methods | Regular class with NotImplementedError |
| Need to enforce implementation | Abstract class with ABC |
| Building frameworks/libraries | Abstract classes |

### 🎯 Practice Question

Create an abstract `Document` class with abstract methods:
- `open()` - open the document
- `save()` - save the document
- `close()` - close the document

Then create concrete classes `PDFDocument` and `WordDocument` that implement these methods.

<details>
<summary>Click to see solution</summary>

```python
from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, filename):
        self.filename = filename
    
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def close(self):
        pass

class PDFDocument(Document):
    def open(self):
        print(f"Opening PDF: {self.filename}")
    
    def save(self):
        print(f"Saving PDF: {self.filename}")
    
    def close(self):
        print(f"Closing PDF: {self.filename}")

class WordDocument(Document):
    def open(self):
        print(f"Opening Word document: {self.filename}")
    
    def save(self):
        print(f"Saving Word document: {self.filename}")
    
    def close(self):
        print(f"Closing Word document: {self.filename}")

# Use them
pdf = PDFDocument("report.pdf")
pdf.open()   # Output: Opening PDF: report.pdf
pdf.save()   # Output: Saving PDF: report.pdf
pdf.close()  # Output: Closing PDF: report.pdf

word = WordDocument("letter.docx")
word.open()  # Output: Opening Word document: letter.docx
word.save()  # Output: Saving Word document: letter.docx
word.close() # Output: Closing Word document: letter.docx
```
</details>

---

## 🎉 Congratulations! You've Completed Part 2!

You've mastered the **Four Pillars of OOP**:

✅ **Inheritance** - Creating classes from other classes  
✅ **Polymorphism** - Same interface, different behaviors  
✅ **Encapsulation** - Hiding internal details  
✅ **Abstraction** - Defining contracts and interfaces  

Plus bonus topics:
✅ Method overriding and `super()`  
✅ Multiple inheritance and MRO  
✅ Properties with `@property`  
✅ Abstract classes with ABC  

### 🚀 Ready for Magic Methods?

Head to **[Part 3: Magic Methods](Part_3_Magic_Methods.md)** to learn how to make your objects behave like built-in Python types!

You're doing amazing! 🌟 Keep going! 💪
