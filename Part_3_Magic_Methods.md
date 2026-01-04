# Part 3: Magic Methods (Dunder Methods) - Chapters 16-25

Welcome to Part 3! Get ready to unlock the **magic** of Python! ✨ Learn how to make your objects behave like built-in types!

---

## Chapter 16: Introduction to Magic Methods (Dunder Methods)

### 1️⃣ WHY

**Why do we need magic methods?**

Have you ever wondered:
- How does `len(my_list)` work?
- Why can you do `obj1 + obj2` with numbers but not your custom objects?
- How does `print(obj)` know what to display?

The answer: **Magic methods!** (Also called **dunder methods** because they have **d**ouble **under**scores)

**What problem do they solve?**

Without magic methods:
```python
my_obj.add_to(other_obj)  # Ugly
my_obj.get_length()       # Verbose
my_obj.to_string()        # Clunky
```

With magic methods:
```python
my_obj + other_obj  # Pythonic!
len(my_obj)         # Clean!
str(my_obj)         # Beautiful!
```

### 2️⃣ WHEN

**When to use magic methods:**
- Making custom objects behave like built-in types
- Supporting operators (+, -, *, /, etc.)
- Customizing how objects are printed, compared, or iterated
- Making objects work with Python's standard functions

**When to skip them:**
- Don't add them "just because"
- Only implement what makes sense for your class
- Keep them intuitive (don't make + do something weird!)

### 3️⃣ HOW

**What are magic methods?**

Magic methods are special methods with names like `__init__`, `__str__`, `__add__`, etc. They:
- Always have double underscores before and after the name
- Are called automatically by Python in specific situations
- Let your objects integrate with Python's syntax and built-in functions

**You've already used one!** The `__init__` method!

**Example 1: Common Magic Methods You'll Love**

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # __str__ - called by str() and print()
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # __repr__ - called by repr() and in the console
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # __len__ - called by len()
    def __len__(self):
        return self.pages
    
    # __eq__ - called by ==
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

book1 = Book("1984", "George Orwell", 328)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("Animal Farm", "George Orwell", 112)

# __str__ is used by print()
print(book1)  # Output: '1984' by George Orwell

# __repr__ is used when you just type the variable
print(repr(book1))  # Output: Book('1984', 'George Orwell', 328)

# __len__ is used by len()
print(len(book1))  # Output: 328

# __eq__ is used by ==
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False
```

**Magic! ✨** Python automatically calls these methods when you use built-in functions and operators!

**Example 2: Categories of Magic Methods**

```python
# There are MANY magic methods! Here are the main categories:

# 1. Initialization and Representation
__init__     # Initialize object
__str__      # Casual string representation
__repr__     # Official string representation
__format__   # Custom formatting

# 2. Comparison
__eq__       # ==
__ne__       # !=
__lt__       # <
__le__       # <=
__gt__       # >
__ge__       # >=

# 3. Arithmetic Operators
__add__      # +
__sub__      # -
__mul__      # *
__truediv__  # /
__floordiv__ # //
__mod__      # %
__pow__      # **

# 4. Container/Sequence Methods
__len__      # len()
__getitem__  # obj[key]
__setitem__  # obj[key] = value
__contains__ # item in obj
__iter__     # for item in obj

# 5. Callable
__call__     # obj()

# 6. Context Manager
__enter__    # with statement
__exit__     # with statement

# 7. Object Creation
__new__      # Create new instance (before __init__)
```

**Example 3: Simple Vector Class with Magic Methods**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        # Vector addition
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        # Scalar multiplication
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Look how natural this is!
v3 = v1 + v2  # Calls __add__
print(v3)  # Output: Vector(4, 6)

v4 = v1 * 3  # Calls __mul__
print(v4)  # Output: Vector(3, 6)

print(v1 == v2)  # Output: False (calls __eq__)
```

**The Magic Behind the Scenes:**

When you write `v1 + v2`, Python does:
1. Checks if `v1` has `__add__` method
2. Calls `v1.__add__(v2)`
3. Returns the result

It's not really magic - it's just Python being smart! 🧠

**Example 4: Understanding the Double Underscore Convention**

```python
# Regular method - you call it yourself
class Example:
    def regular_method(self):
        return "You called me!"
    
    # Magic method - Python calls it for you
    def __str__(self):
        return "Python called me!"

obj = Example()

# Regular method - explicit call
result = obj.regular_method()
print(result)  # Output: You called me!

# Magic method - implicit call
result = str(obj)  # Python calls __str__ automatically
print(result)  # Output: Python called me!
```

**Why "dunder"?**

"Dunder" = "Double Underscore"
- `__init__` = "dunder init"
- `__str__` = "dunder str"
- `__add__` = "dunder add"

Much easier to say than "double underscore init double underscore"! 😄

**Key Points:**

1. **Magic methods** have `__name__` format
2. Python calls them **automatically** in specific situations
3. Let your objects work with **operators** and **built-in functions**
4. Make your code more **Pythonic** and **intuitive**
5. Don't override them unless it makes sense for your class
6. Always keep them **intuitive** (+ should add, not delete!)

**Common Magic Methods Quick Reference:**

| Method | When it's called | Example |
|--------|------------------|---------|
| `__init__` | Creating object | `obj = MyClass()` |
| `__str__` | str() or print() | `print(obj)` |
| `__repr__` | repr() or console | `repr(obj)` |
| `__len__` | len() | `len(obj)` |
| `__add__` | + operator | `obj1 + obj2` |
| `__eq__` | == operator | `obj1 == obj2` |
| `__getitem__` | Indexing | `obj[key]` |
| `__call__` | Calling like function | `obj()` |

### 🎯 Practice Question

Think about what magic methods these scenarios would use:
1. Printing an object with `print(obj)`
2. Checking if two objects are equal with `obj1 == obj2`
3. Getting the length with `len(obj)`
4. Adding two objects with `obj1 + obj2`

<details>
<summary>Click to see answers</summary>

1. `__str__` (or `__repr__` if `__str__` isn't defined)
2. `__eq__`
3. `__len__`
4. `__add__`

</details>

---

## Chapter 17: Representation Methods: __str__, __repr__, __format__

### 1️⃣ WHY

**Why do we need representation methods?**

Without them, printing your objects is useless:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person)  # Output: <__main__.Person object at 0x7f8b4c0a7d30>
# Not helpful! 😢
```

With representation methods:
```python
print(person)  # Output: Person(name='Alice', age=25)
# Much better! 😊
```

### 2️⃣ WHEN

**When to use each:**

- **`__str__`**: Human-readable, casual representation (for end users)
- **`__repr__`**: Developer-friendly, unambiguous representation (for debugging)
- **`__format__`**: Custom formatting for f-strings and format()

**Rule of thumb:**
- `__str__` = what you'd show to a user
- `__repr__` = what you'd show to a developer (ideally code that recreates the object)

### 3️⃣ HOW

**Example 1: __str__ vs __repr__**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # __str__ - friendly, readable
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    # __repr__ - unambiguous, for debugging
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 25)

# print() uses __str__
print(person)  # Output: Alice, 25 years old

# str() uses __str__
print(str(person))  # Output: Alice, 25 years old

# repr() uses __repr__
print(repr(person))  # Output: Person(name='Alice', age=25)

# In the console, __repr__ is used
# >>> person
# Person(name='Alice', age=25)

# Lists/dicts use __repr__ for their contents
people = [Person("Bob", 30), Person("Charlie", 35)]
print(people)
# Output: [Person(name='Bob', age=30), Person(name='Charlie', age=35)]
```

**Key difference:**
- `__str__` aims for **readability**
- `__repr__` aims for **unambiguity**

**Example 2: When You Only Define __repr__**

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # Only defining __repr__
    def __repr__(self):
        return f"Product('{self.name}', ${self.price})"
    
    # No __str__ defined!

product = Product("Laptop", 999.99)

# If __str__ isn't defined, Python uses __repr__ as fallback
print(product)  # Output: Product('Laptop', $999.99)
print(str(product))  # Output: Product('Laptop', $999.99)
print(repr(product))  # Output: Product('Laptop', $999.99)
```

**Pro tip:** If you're only going to define one, define `__repr__`! Python will use it as a fallback for `__str__`.

**Example 3: __format__ for Custom Formatting**

```python
import datetime

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def __str__(self):
        return f"{self.name} from {self.city}"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age}, '{self.city}')"
    
    def __format__(self, format_spec):
        # Custom format codes:
        # 's' = short (name only)
        # 'f' = full (name, age, city)
        # 'a' = age only
        if format_spec == 's':
            return self.name
        elif format_spec == 'f':
            return f"{self.name}, {self.age} years old, from {self.city}"
        elif format_spec == 'a':
            return str(self.age)
        else:
            return str(self)

person = Person("Alice", 25, "New York")

# Regular print (uses __str__)
print(person)  # Output: Alice from New York

# Using format() and custom format specs
print(format(person, 's'))  # Output: Alice
print(format(person, 'f'))  # Output: Alice, 25 years old, from New York
print(format(person, 'a'))  # Output: 25

# Using f-strings with format specs
print(f"Name: {person:s}")  # Output: Name: Alice
print(f"Full: {person:f}")  # Output: Full: Alice, 25 years old, from New York
print(f"Age: {person:a}")   # Output: Age: 25
```

**Example 4: Complex __repr__ Example**

```python
class Rectangle:
    def __init__(self, width, height, color="white"):
        self.width = width
        self.height = height
        self.color = color
    
    def __repr__(self):
        # Goal: return code that could recreate this object
        return f"Rectangle(width={self.width}, height={self.height}, color='{self.color}')"
    
    def __str__(self):
        # User-friendly description
        return f"A {self.color} rectangle {self.width}x{self.height}"

rect = Rectangle(10, 20, "blue")

# For users
print(rect)  # Output: A blue rectangle 10x20

# For developers
print(repr(rect))  # Output: Rectangle(width=10, height=20, color='blue')

# The magic: you can often use repr() output to recreate the object!
rect2_code = repr(rect)
print(rect2_code)  # Output: Rectangle(width=10, height=20, color='blue')
# This is valid Python code that creates the same object!
```

**Example 5: Date Class with Multiple Representations**

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        # Casual, readable format
        return f"{self.month}/{self.day}/{self.year}"
    
    def __repr__(self):
        # Unambiguous, can recreate object
        return f"Date({self.year}, {self.month}, {self.day})"
    
    def __format__(self, format_spec):
        # Custom formatting
        # 'us' = US format (MM/DD/YYYY)
        # 'eu' = European format (DD/MM/YYYY)
        # 'iso' = ISO format (YYYY-MM-DD)
        if format_spec == 'us':
            return f"{self.month:02d}/{self.day:02d}/{self.year}"
        elif format_spec == 'eu':
            return f"{self.day:02d}/{self.month:02d}/{self.year}"
        elif format_spec == 'iso':
            return f"{self.year}-{self.month:02d}-{self.day:02d}"
        else:
            return str(self)

date = Date(2024, 3, 15)

print(date)              # Output: 3/15/2024 (uses __str__)
print(repr(date))        # Output: Date(2024, 3, 15) (uses __repr__)
print(f"{date:us}")      # Output: 03/15/2024
print(f"{date:eu}")      # Output: 15/03/2024
print(f"{date:iso}")     # Output: 2024-03-15
```

**Best Practices:**

```python
class GoodExample:
    def __init__(self, value):
        self.value = value
    
    # ✅ DO: Make __repr__ return code that could recreate object
    def __repr__(self):
        return f"GoodExample({self.value})"
    
    # ✅ DO: Make __str__ user-friendly
    def __str__(self):
        return f"Value: {self.value}"

class BadExample:
    def __init__(self, value):
        self.value = value
    
    # ❌ DON'T: Make __repr__ too casual
    def __repr__(self):
        return f"Some object with value"  # Not helpful!
    
    # ❌ DON'T: Make __str__ too technical
    def __str__(self):
        return f"BadExample object at {id(self)}"  # Use __repr__ for this!
```

**Quick Decision Guide:**

```python
# Need just one? Define __repr__
class OnlyRepr:
    def __repr__(self):
        return f"OnlyRepr(...)"  # Python uses this for str() too

# Need both? Think about your audience
class Both:
    def __str__(self):
        return "User-friendly message"  # For end users
    
    def __repr__(self):
        return "Both(...)"  # For developers

# Need fancy formatting? Add __format__
class Fancy:
    def __format__(self, spec):
        return "Custom formatted output"
```

### 🎯 Practice Question

Create a `Book` class with:
- `__str__` that returns "Title by Author"
- `__repr__` that returns "Book('Title', 'Author', pages)"
- `__format__` that supports 't' for title only and 'a' for author only

<details>
<summary>Click to see solution</summary>

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __format__(self, format_spec):
        if format_spec == 't':
            return self.title
        elif format_spec == 'a':
            return self.author
        else:
            return str(self)

book = Book("1984", "George Orwell", 328)

print(book)           # Output: 1984 by George Orwell
print(repr(book))     # Output: Book('1984', 'George Orwell', 328)
print(f"{book:t}")    # Output: 1984
print(f"{book:a}")    # Output: George Orwell
```
</details>

---

[Continuing with Chapters 18-25...]


## Chapter 18: Length and Container Methods: __len__, __getitem__, __setitem__, __contains__

### 1️⃣ WHY

**Why do we need container methods?**

Want your custom class to work like a list or dictionary?
- `len(my_obj)` ← __len__
- `my_obj[key]` ← __getitem__
- `my_obj[key] = value` ← __setitem__
- `item in my_obj` ← __contains__

Without these, your objects can't act like containers!

### 2️⃣ WHEN

**When to use container methods:**
- Building custom collection classes
- Wrapping existing containers with extra logic
- Creating specialized data structures
- When your object logically "contains" other objects

### 3️⃣ HOW

**Example 1: Custom List-Like Class**

```python
class PlayList:
    def __init__(self):
        self.songs = []
    
    # __len__ - makes len() work
    def __len__(self):
        return len(self.songs)
    
    # __getitem__ - makes indexing work: playlist[0]
    def __getitem__(self, index):
        return self.songs[index]
    
    # __setitem__ - makes assignment work: playlist[0] = "New Song"
    def __setitem__(self, index, value):
        self.songs[index] = value
    
    # __contains__ - makes 'in' work: "Song" in playlist
    def __contains__(self, song):
        return song in self.songs
    
    def add_song(self, song):
        self.songs.append(song)

playlist = PlayList()
playlist.add_song("Bohemian Rhapsody")
playlist.add_song("Stairway to Heaven")
playlist.add_song("Hotel California")

# Now it works like a list!
print(len(playlist))  # Output: 3 (uses __len__)

print(playlist[0])  # Output: Bohemian Rhapsody (uses __getitem__)

playlist[1] = "Imagine"  # Uses __setitem__
print(playlist[1])  # Output: Imagine

print("Imagine" in playlist)  # Output: True (uses __contains__)
print("Yesterday" in playlist)  # Output: False

# You can even iterate! (because __getitem__ enables it)
for song in playlist:
    print(f"♪ {song}")
```

**Example 2: Shopping Cart**

```python
class ShoppingCart:
    def __init__(self):
        self.items = {}  # {product_name: quantity}
    
    def __len__(self):
        # Total number of items
        return sum(self.items.values())
    
    def __getitem__(self, product):
        # Get quantity of a product
        return self.items.get(product, 0)
    
    def __setitem__(self, product, quantity):
        # Set quantity of a product
        if quantity <= 0:
            # Remove if quantity is 0 or negative
            self.items.pop(product, None)
        else:
            self.items[product] = quantity
    
    def __contains__(self, product):
        # Check if product is in cart
        return product in self.items
    
    def __str__(self):
        if not self.items:
            return "Empty cart"
        return "\n".join(f"{prod}: {qty}" for prod, qty in self.items.items())

cart = ShoppingCart()

# Add items using []
cart["Apple"] = 5
cart["Banana"] = 3
cart["Orange"] = 2

print(f"Total items: {len(cart)}")  # Output: Total items: 10

print(f"Apples: {cart['Apple']}")  # Output: Apples: 5

print("Banana" in cart)  # Output: True
print("Grape" in cart)   # Output: False

# Change quantity
cart["Apple"] = 10
print(f"Apples now: {cart['Apple']}")  # Output: Apples now: 10

# Remove item (set to 0)
cart["Orange"] = 0
print("Orange" in cart)  # Output: False

print(cart)
# Output:
# Apple: 10
# Banana: 3
```

**Example 3: Grade Book**

```python
class GradeBook:
    def __init__(self):
        self.grades = {}
    
    def __setitem__(self, student, grade):
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number!")
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100!")
        self.grades[student] = grade
    
    def __getitem__(self, student):
        if student not in self.grades:
            raise KeyError(f"No grade for {student}")
        return self.grades[student]
    
    def __contains__(self, student):
        return student in self.grades
    
    def __len__(self):
        return len(self.grades)
    
    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

gradebook = GradeBook()

# Add grades
gradebook["Alice"] = 95
gradebook["Bob"] = 87
gradebook["Charlie"] = 92

print(f"Alice's grade: {gradebook['Alice']}")  # Output: Alice's grade: 95

print(f"Students: {len(gradebook)}")  # Output: Students: 3

if "Bob" in gradebook:
    print(f"Bob's grade: {gradebook['Bob']}")  # Output: Bob's grade: 87

print(f"Class average: {gradebook.average():.2f}")  # Output: Class average: 91.33

# Validation works!
try:
    gradebook["David"] = 150  # Too high!
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Grade must be between 0 and 100!
```

**Example 4: Slicing Support**

```python
class CustomList:
    def __init__(self, items=None):
        self.items = items or []
    
    def __getitem__(self, key):
        # Supports both indexing and slicing!
        if isinstance(key, slice):
            return CustomList(self.items[key])
        return self.items[key]
    
    def __setitem__(self, key, value):
        self.items[key] = value
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return f"CustomList({self.items})"

clist = CustomList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(clist[0])     # Output: 1 (single item)
print(clist[2:5])   # Output: CustomList([3, 4, 5]) (slice)
print(clist[::2])   # Output: CustomList([1, 3, 5, 7, 9]) (step)
print(clist[-1])    # Output: 10 (negative index)
```

### 🎯 Practice Question

Create a `Stack` class that implements:
- `__len__` to return number of items
- `__getitem__` to peek at items
- `push(item)` to add items
- `pop()` to remove items

<details>
<summary>Click to see solution</summary>

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __str__(self):
        return f"Stack({self.items})"
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            raise IndexError("Pop from empty stack!")
        return self.items.pop()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(len(stack))  # Output: 3
print(stack[0])    # Output: 1
print(stack.pop()) # Output: 3
print(stack)       # Output: Stack([1, 2])
```
</details>

---

## Chapter 19: Arithmetic Operator Overloading

### 1️⃣ WHY

**Why overload arithmetic operators?**

Want to do `vector1 + vector2` or `fraction1 * fraction2`? You need to tell Python what + and * mean for your objects!

### 2️⃣ WHEN

Use when your class represents something that can be added, subtracted, multiplied, etc. (numbers, vectors, matrices, fractions).

### 3️⃣ HOW

**Example: Vector Class**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Addition: v1 + v2
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Subtraction: v1 - v2
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Multiplication: v1 * scalar
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Division: v1 / scalar
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    
    # Reverse multiplication: scalar * v1
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)  # Output: Vector(4, 6)

v4 = v2 - v1
print(v4)  # Output: Vector(2, 2)

v5 = v1 * 3
print(v5)  # Output: Vector(3, 6)

v6 = 2 * v2  # Reverse multiplication
print(v6)  # Output: Vector(6, 8)

v7 = v2 / 2
print(v7)  # Output: Vector(1.5, 2.0)
```

**Example 2: Money Class**

```python
class Money:
    def __init__(self, dollars, cents=0):
        self.total_cents = dollars * 100 + cents
    
    def __str__(self):
        dollars = self.total_cents // 100
        cents = self.total_cents % 100
        return f"${dollars}.{cents:02d}"
    
    def __add__(self, other):
        result = Money(0)
        result.total_cents = self.total_cents + other.total_cents
        return result
    
    def __sub__(self, other):
        result = Money(0)
        result.total_cents = self.total_cents - other.total_cents
        return result
    
    def __mul__(self, multiplier):
        result = Money(0)
        result.total_cents = int(self.total_cents * multiplier)
        return result

price1 = Money(10, 50)  # $10.50
price2 = Money(5, 25)   # $5.25

total = price1 + price2
print(total)  # Output: $15.75

difference = price1 - price2
print(difference)  # Output: $5.25

doubled = price1 * 2
print(doubled)  # Output: $21.00
```

**All Arithmetic Operators:**

- `__add__` (self + other)
- `__sub__` (self - other)
- `__mul__` (self * other)
- `__truediv__` (self / other)
- `__floordiv__` (self // other)
- `__mod__` (self % other)
- `__pow__` (self ** other)
- `__radd__` (other + self - reverse)
- `__iadd__` (self += other - in-place)

### 🎯 Practice Question

Create a `Fraction` class with `__add__` and `__mul__` methods.

<details>
<summary>Click to see solution</summary>

```python
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def __mul__(self, other):
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

f1 = Fraction(1, 2)  # 1/2
f2 = Fraction(1, 3)  # 1/3

f3 = f1 + f2
print(f3)  # Output: 5/6

f4 = f1 * f2
print(f4)  # Output: 1/6
```
</details>

---

## Chapter 20: Comparison Methods

### 1️⃣ WHY

Want to compare objects with ==, <, >, etc.? You need comparison magic methods!

### 2️⃣ WHEN

Use when it makes sense to compare your objects (numbers, dates, strings, priorities).

### 3️⃣ HOW

**Example: Person Class with Age Comparison**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
    # Equal: ==
    def __eq__(self, other):
        return self.age == other.age
    
    # Not equal: !=
    def __ne__(self, other):
        return self.age != other.age
    
    # Less than: <
    def __lt__(self, other):
        return self.age < other.age
    
    # Less than or equal: <=
    def __le__(self, other):
        return self.age <= other.age
    
    # Greater than: >
    def __gt__(self, other):
        return self.age > other.age
    
    # Greater than or equal: >=
    def __ge__(self, other):
        return self.age >= other.age

alice = Person("Alice", 25)
bob = Person("Bob", 30)
charlie = Person("Charlie", 25)

print(alice == charlie)  # Output: True (same age)
print(alice == bob)      # Output: False
print(alice < bob)       # Output: True
print(bob > alice)       # Output: True

# Now you can sort people by age!
people = [bob, charlie, alice]
people.sort()
for person in people:
    print(person)
# Output: Alice (25), Charlie (25), Bob (30)
```

**Example 2: Product with Price Comparison**

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price}"
    
    def __eq__(self, other):
        return self.price == other.price
    
    def __lt__(self, other):
        return self.price < other.price
    
    def __le__(self, other):
        return self.price <= other.price
    
    def __gt__(self, other):
        return self.price > other.price
    
    def __ge__(self, other):
        return self.price >= other.price

laptop = Product("Laptop", 999)
mouse = Product("Mouse", 25)
keyboard = Product("Keyboard", 75)

products = [laptop, keyboard, mouse]
products.sort()  # Sort by price

for product in products:
    print(product)
# Output: Mouse: $25, Keyboard: $75, Laptop: $999

print(laptop > keyboard)  # Output: True
print(min(products))      # Output: Mouse: $25
```

### 🎯 Practice Question

Create a `Temperature` class that compares temperatures by Celsius value.

---

## Chapter 21: The __call__ Method - Making Objects Callable

### 1️⃣ WHY

Want to use an object like a function? `obj()`? Use `__call__`!

### 2️⃣ WHEN

Use for objects that represent actions, callbacks, or function-like objects.

### 3️⃣ HOW

**Example: Counter**

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # Output: 1 (called like a function!)
print(counter())  # Output: 2
print(counter())  # Output: 3
```

**Example 2: Multiplier**

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

---

## Chapter 22: Iterator Protocol: __iter__ and __next__

### 1️⃣ WHY

Want your object to work in for loops? Implement the iterator protocol!

### 2️⃣ WHEN

Use when creating custom sequences or collections.

### 3️⃣ HOW

**Example: Countdown Iterator**

```python
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in Countdown(5):
    print(num)
# Output: 5, 4, 3, 2, 1
```

**Example 2: Range-like Class**

```python
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for i in MyRange(0, 5):
    print(i)
# Output: 0, 1, 2, 3, 4
```

---

## Chapter 23: Context Manager Protocol: __enter__ and __exit__

### 1️⃣ WHY

Want your object to work with `with` statements? Implement context manager protocol!

### 2️⃣ WHEN

Use for resource management: files, database connections, locks.

### 3️⃣ HOW

**Example: Timer Context Manager**

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.4f} seconds")
        return False

with Timer():
    # Code to time
    sum([i**2 for i in range(1000000)])
# Output: Elapsed time: 0.1234 seconds
```

**Example 2: File Manager**

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False

with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
# File automatically closed!
```

---

## Chapter 24: Object Creation Deep Dive: __new__ vs __init__

### 1️⃣ WHY

**What's the difference?**
- `__new__` creates the object
- `__init__` initializes the object

### 2️⃣ WHEN

Rarely need `__new__`. Use for:
- Singleton pattern
- Immutable types
- Customizing object creation

### 3️⃣ HOW

**Example: Singleton Pattern**

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.value = "I'm a singleton"

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True (same object!)
```

---

## Chapter 25: Other Useful Magic Methods

### __del__ - Object Destruction

```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Creating {name}")
    
    def __del__(self):
        print(f"Destroying {name}")

r = Resource("MyResource")
del r  # Triggers __del__
```

### __hash__ - Make Objects Hashable

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)

# Can use in sets and as dict keys!
points = {p1, p2}
print(len(points))  # Output: 1 (same hash)
```

### __bool__ - Truth Value

```python
class Empty:
    def __init__(self, items):
        self.items = items
    
    def __bool__(self):
        return len(self.items) > 0

e1 = Empty([1, 2, 3])
e2 = Empty([])

if e1:
    print("Not empty")  # This prints

if not e2:
    print("Empty")  # This prints
```

---

## 🎉 Congratulations! You've Completed Part 3!

You've mastered **Magic Methods**:

✅ Representation methods (__str__, __repr__)  
✅ Container methods (__len__, __getitem__)  
✅ Arithmetic operators  
✅ Comparison operators  
✅ Callable objects  
✅ Iterators  
✅ Context managers  
✅ And more!  

### 🚀 Ready for the Final Part?

Head to **[Part 4: Best Practices](Part_4_Best_Practices.md)** to learn real-world applications and common mistakes!

You're almost there! 🌟 Keep going! 💪
