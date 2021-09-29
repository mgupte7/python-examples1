# -----------------------------------------------
# ----------------Python Lambda------------------
# -----------------------------------------------

# A lambda function is a small anonymous function.
#
# A lambda function can take any number of arguments, but can only have one expression.

# ex 1 - Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# ex 2 - Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

# ex 3 - Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# ex 4 - takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n

# ex 5 - Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# ex 6 - same function definition to make a function that always triples the number you send in:
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# ex 7 - same function definition to make both functions, in the same program:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# ex 8
# ex 9
# ex 10
# ex 12
# ex 13
# ex 14
# ex 15
# ex 16
# ex 17
# ex 18
# ex 19
# ex 20
