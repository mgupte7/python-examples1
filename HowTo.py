# ------------------------------------------------
# ---------------- How to ------------------------
# ------------------------------------------------

# --------------------------------------------------------------------
# ---------------- Remove any duplicates from a List: ----------------
# (ex 1)
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist)) # dictionaries cannot have duplicate values
print("ex 1")
print(mylist)

# (ex 2) - Create a Function
def my_function(x): # function with list as an argument
  return list(dict.fromkeys(x)) # list -> dictionary -> list

mylist = my_function(["a", "b", "a", "c", "c"]) # call function, with list as parameter

print(mylist)

# -----------------------------------------------------------------------------------------------------
# ---------------- How to Reverse a String in Python How to Reverse a String in Python ----------------

# (ex 3) Reverse the string "Hello World":

txt = "Hello World"[::-1] # slice the string backwards
print("ex 3")
print(txt)

# ---------------- Create a Function ----------------

def my_function(x): # create function
  return x[::-1] # slice string/ return

mytxt = my_function("I wonder how this text looks like backwards") # call function

print(mytxt) # print result

# ------------------------------------------------------------------
# ---------------- How to Add Two Numbers in Python ----------------

# (ex 4- use the + opperator to add two numbers)
x = 5
y = 10
print("ex 4")
print(x + y)

# ---------------- Add Two Numbers with User Input ----------------

# (ex 5- get two inputs from the user then print the sum)

x = input("Type a number: ")
y = input("Type another number: ")

sum = int(x) + int(y)

print("ex 5")
print("The sum is: ", sum)


