# -*- coding: utf-8 -*-
"""15 - Classes and Objects.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kwr_Tz2kP0snSuDesxavvIKzrWTEttl0

# Beginner
"""

# Classes and objects
class dog():
  def bark(self):
    print("Woof!")

max = dog()
max.bark()

# create an Attribute
class car():
  def __init__(self, brand):
    self.brand = brand

car1 = car("Suzuki")
print(car1.brand)

# Multiple attributes
class cls():
  def __init__(self, name, age):
    self.name = name
    self.age = age
sec1 = cls("Mohan -", 28)
sec2 = cls("Raj -", 18)
print(sec1.name, sec1.age)
print(sec2.name, sec2.age)

# methods and attributes
class area():
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def rectangle_area(self):
    return self.width * self.height

rectangle1 = area(3, 7)
rectangle2 = area(15, 3)
print(rectangle1.rectangle_area())
print(rectangle2.rectangle_area())

# Modify object attributes
class circle():
  def __init__(self, radius):
    self.radius = radius

  def changes_radius(self, new_radius):
    self.radius = new_radius

circle1 = circle(3)
print(circle1.radius)

circle1.changes_radius(10)
print(circle1.radius)

# Class with Default values
class book():
  def __init__(self, title, author = "Unknown"):
    self.title=  title
    self.author = author

  def book_details(self):
    return f"The Title of the Book is '{self.title}' and the Auther name is '{self.author}'"

book1 = book("Lords of the Rings", "mohanraj")
print(book1.book_details())

book2 = book("National Geography")
print(book2.book_details())

# Clas Inheritence
class animal():
  def speak(self):
    print("Animal Sound")

class cat(animal):
  def speak(self):
    print("Mewo")
animal1 = animal()
animal1.speak()
animal2 = cat()
animal2.speak()

# Multiple methods in a class
class bank():
  def __init__(self, balance = 0):
    self.balance = balance

  def deposite(self, amount):
    self.balance = self.balance + amount

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance = self.balance - amount
    else:
      print("Insufficient balance")
account1 = bank()
print(account1.balance)

account1.withdraw(10)

account1.deposite(100)
print(account1.balance)
account1.deposite(200)
print(account1.balance)
account1.deposite(500)
print(account1.balance)

account1.withdraw(400)
print(account1.balance)

# Encapsulation
class privateAccount():
  def __init__(self, balance = 0):
    self.__balance = balance
  def get_balance(self):
    return self.__balance
  def deposite(self, amount):
    self.__balance = self.__balance + amount

p_acc1 = privateAccount()
print(p_acc1.get_balance())
p_acc1.deposite(100)
print(p_acc1.get_balance())

# Static method
class maths():
  @staticmethod
  def add(a, b):
    return a + b
result = maths.add(7, 7)
print(result)

"""#Intermediate"""

# Class methods to count objects
class Counter():
  obj_count = 0
  def __init__(self):
    Counter.obj_count = Counter.obj_count + 1

  @classmethod
  def get_count(cls):
    return cls.obj_count

counter1 = Counter()
print(counter1.get_count())
counter2 = Counter()
print(counter2.get_count())
counter3 = Counter()
print(counter3.get_count())

# Operator Overloading
class point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return self.x + other.x, self.y + other.y

  def __repr__(self):
    return f"Points are : {self.x}, {self.y}"

a = point(1, 5)
b = point(2, 10)
res = a + b
print("The Points are ", res)

# Inheritence with method overriding
class employee():
  def __init__(self, salary):
    self.salery = salary
  def get_salery(self):
    return self.salery

class manager(employee):
  def __init__(self, salery, bonus):
    super().__init__(salery)
    self.bonus = bonus
  def get_salery(self):
    return self.salery + self.bonus

emp1 = employee(10000)
print(emp1.get_salery())

emp2 = manager(20000, 5000)
print(emp2.get_salery())

# Class composition
class Engine():
  def start(self):
    return "Engine Started"

class car():
  def __init__(self, engine):
    self.engine = engine

  def my_car(self):
    return self.engine.start()

engine1 = Engine()
car1 = car(engine1)
print(car1.my_car())

# Static method

class math():
  @staticmethod
  def even(number):
    return number % 2 == 0
print(math.even(3))
print(math.even(10))
print(math.even(2))
print(math.even(78))

# Classmethods for alternative constrctors
class Date():
  def __init__(self, day):
    self.day = day

  @classmethod
  def str_from(cls, str_date):
    day = int(str_date)
    return cls(day)

day1 = Date(10)
print(day1.day)

day2 = Date.str_from("27")
print(day2.day)

# Property Decorators
class Product():
  def __init__(self, price):
    self._price = price
  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, value):
    if value < 0:
      raise ValueError("Please put a positive Value")
    self._price = value

p = Product(100)
print(p.price)

p.price = 250

print(p.price)

# Multiple Inheritence
class bird():
  def fly(self):
    return "I can Fly"

class swimmer():
  def swim(self):
    return "I can Swim"

class penguin(bird, swimmer):
  def fly(self):
    return "Penguins can't fly"

animal1 = bird()
animal2 = swimmer()
animal3 = penguin()
print(animal1.fly())
print(animal2.swim())
print(animal3.swim())
print(animal3.fly())

# Abstaract method and class
from abc import ABC, abstractmethod

class shape(ABC):
  @abstractmethod
  def area(self):
    pass

class circle(shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius * self.radius

class square(shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side * self.side

circle = circle(4)
square = square(20)

print(circle.area())
print(square.area())