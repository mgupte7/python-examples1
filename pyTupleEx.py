# -----------------------------------------------
# ----------------Python Tuple------------------
# -----------------------------------------------

# general notes:
# Tuple items are ordered, UNCHANGEABLE, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# ex 1 - Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# ex 2 - Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# ex 3 - Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# ex 4 - One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# ex 5 - String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# ex 6 - A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

# ex 7 - What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
# ex 8 - Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# ---------------------- Access Tuple Items -------------------------

# ex 9 - Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# ex 10 - Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# ex 11 - Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# ex 12 - This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# ex 13 - This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# ex 14 - This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# ex 15 - Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# ---------------------- Update Tuples -------------------------
# ex 16 - Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# ex 17 - Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# ex 18 - Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# ex 19 - Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# ex 20 - The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# ---------------------- Unpack Tuples -------------------------

# ex 21 - Packing a tuple:
fruits = ("apple", "banana", "cherry")

# ex 22 - Unpacking a tuple: (extract the values back into variables)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# ex 23 - Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# ex 24 - Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

