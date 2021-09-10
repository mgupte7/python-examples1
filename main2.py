# examples 10 - output variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# exmaple 11 - variable inside a function

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# example 12 - global keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# example 13 - global keyword (2)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# example 14 - data types

x = 5
print(type(x))

# example 15 - numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# example 16 - ints

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# example 17 - floats

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# example 18 - complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# example 19 - type conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# example 20 - random number

import random

print(random.randrange(1, 10))