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

# ex 5 - This example returns the items from the beginning to, but NOT including, "kiwi"
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

# ---------------------List Loops---------------
# ex 27 - print all items one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# ex 28 - loop through the index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# ex 29 - loop using a while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# ex 31 - loop list using list comprehension (short hand for for-loop)
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# ---------------------List Comprehension-----------------------

# ex 32 - long syntax example (for reference)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# ex 33 - shortened with one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# generic syntax: newlist = [expression for item in iterable if condition == True]

# ex 34 - the condition is like a filter that only accepts the items that valuate to True
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# ex 35 - don't need a conditional statement
newlist = [x for x in fruits]

# ex 36 - You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

# ex 37 - Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

# ex 38 - Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

# ex 39 - Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

# ex 40 - Return "orange" instead of "banana": (replacing every instance)
newlist = [x if x != "banana" else "orange" for x in fruits]

# ----------------------- Sort Lists -----------------------

# ex 41 - Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# ex 42 - Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# ex 43 - Sort the list descending: (alphabetically)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# ex 44 - Sort the list descending: (numeric)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# ex 45 - Sort the list based on how close the number is to 50: (custom sort function)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# ex 46 - Case sensitive sorting can give an unexpected result: (because of uppercase)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# ex 47 - Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# ex 48 - Reverse the order of the list items:
#     (QUESTION- thought it should be "cherry", "banana", "Orange", "Kiwi"
#     answer was "cherry", "Kiwi", "Orange", "banana"
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# --------------------- Copy List -----------------------

# without simply creating new list with same reference

# ex 49 - Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# ex 50 - Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# --------------------- Join Lists -----------------------
# this section goes over how to concatenate lists using the "+" operator
# ex 51 - Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# ex 52 - Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# ex 53 - Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# ex 54
# ex 55
# ex 56
# ex 57
# ex 58
# ex 59



