# -----------------------------------------------
# ----------------Python Lists------------------
# -----------------------------------------------

# ---------------------Access Items---------------

# ex 1 - create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# ex 2 - print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# ex 3 - Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# ex 4 - Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# ex 5 - This example returns the items from the beginning to, but NOT including, "kiw
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# ex 6 - This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# ex 7 - This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# ex 8 - To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# ---------------------Change List Items---------------

# ex 9 - Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# ex 10 - Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# ex 11 - Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# ex 12 - Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# ex 13 - Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# ---------------------Add List Items---------------

# ex 14 - Using the append() method to append an item: (adds at end)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# ex 15 - Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# ex 16 - extend() method to append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# ex 18 - Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# ---------------------Add List Items---------------
# ex 19 - Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# ex 21 - The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# ex 22 - Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# ex 23 - The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# ex 24 - Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# ex 25 - Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
# ex 26 - Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
