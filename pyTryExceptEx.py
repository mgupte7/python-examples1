# --------------------------------------------------
# ---------------- Python Try Except ---------------
# --------------------------------------------------

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# --------------- Exception Handling --------------

# ex 1- The try block will generate an exception, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")

# ----------------------------- Many Exceptions ------------------

# ex 2 - Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# ----------------------------- Else ----------------------------
# ex 3 - In this example, the try block does not generate any error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# ----------------------------- Finally ----------------------------
# ex  4 - The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# ex 5 - Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# ----------------------------- Raise an exception ----------------------------

# ex 5 - Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# ex 6 - Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

