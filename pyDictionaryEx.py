# -----------------------------------------------
# ----------------Python Dictionaries------------
# -----------------------------------------------

# General information:
#
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and does not allow duplicates.

# ex 1 - Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# ex 2 - Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# ex 3 - Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# ex 4 - Print the number of items in the dictionary:
print(len(thisdict))

# ex 5 - String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# ex 6 - Print the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# --------------------- Accessing Items ------------------------------

# ex 7 - Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# ex 8 - Get the value of the "model" key:
x = thisdict.get("model")

# ex 9 - The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()

# ex 10 - Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


# ex 11 - The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

# ex 12 - Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# ex 13 - Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

# ex 14 - Get a list of the key:value pairs
x = thisdict.items()

# ex 15 - adding a new item to the dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

# ex 16 - Get a list of the values:Get a list of the values:Get a list of the values:
x = thisdict.values()

# ex 17 - Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change, will print updated

# ex 18 - Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change, adds new catagory

# ex 19 - Get a list of the key:value pairs
x = thisdict.items() # will print in pairs

# ex 20 - Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["year"] = 2020

# ex 21 - Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

# ex 22 - Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# --------------------- Change Dictionary Items ------------------------------
# You can change the value of a specific item by referring to its key name:

# ex 23 - Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018


# ex 24 - Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# --------------------- Add Dictionary Items ------------------------------
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# ex 25 - general method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# ex 26 - The update() method will update the dictionary with the items from a given argument.
# If the item does not exist, the item will be added.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# --------------------- Remove Dictionary Items ------------------------------
# ex 27 - The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# ex 28 - The popitem() method removes the last inserted item:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# ex 29- The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"] # can also delete a list completely ("del thisdict")
print(thisdict)

# ex 30 - The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# --------------------- Loop through Dictionary ------------------------------
# ex 31 - Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

# ex 32 - Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])

# ex 33 - You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

# ex 34 - You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)

# ex 35 - Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

# --------------------- Copy a Dictionary ------------------------------
# ex 36 - Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# ex 37 - Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# --------------------- Nested Dictionaries ------------------------------
# ex 38 - Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# ex 39 - Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
