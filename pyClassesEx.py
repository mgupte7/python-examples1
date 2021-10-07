# ------------------------------------------------
# ----------------Python Classes------------------
# ------------------------------------------------

# Python is an object oriented programming language.
#
# Almost everything in Python is an object, with its properties and methods.
#
# A Class is like an object constructor, or a "blueprint" for creating objects.

# ex 1 - Create a class named MyClass, with a property named x:
class MyClass:
  x = 5
# ex 2 - Create Object
p1 = MyClass()
print(p1.x)

# ex 3 - The_init_() Function
class Person:
  def __init__(self, name, age): #called automatically every time the class is being used to create a new object
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# ex 4 - Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# ex 5 - The self Parameter -> a reference to the current instance of the class, and is used to access variables that belongs to the class
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# ex 6 - Modify Object Properties
p1.age = 40

# ex 7 - Delete Object Properties
del p1.age

# ex 8 - Delete Objects
del p1

# ex 9 - The pass Statement
class Person:
  pass
# ex 10