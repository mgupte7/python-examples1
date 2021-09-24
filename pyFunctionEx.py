# -----------------------------------------------
# ----------------Python Booleans----------------
# -----------------------------------------------

# ex1
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# ex 2 - can evaluate any value using bool
print(bool("Hello"))
print(bool(15))

# ex 3
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# ex 4 - values that yield false

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# ex 5 - You can execute code based on the Boolean answer of a function:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# ex 6 - Check if an object is an integer or not:
x = 200
print(isinstance(x, int))