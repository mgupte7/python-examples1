# -----------------------------------------------
# ----------------Python Strings-----------------
# -----------------------------------------------

# example 22 - String are Arrays
a = "ex22- strings are arrays"
print(a[1])

# example 23 - Looping through a string

for x in "ex23- looping example":
  print(x)

# ex 24 - String length

a = "ex 24 - string length"
print(len(a))

# ex 25 - Check String

txt = "ex25- The best things in life are free!"
print("free" in txt)

# ex 26 - Check String in If statement

txt = "The best things in life are free!"
if "free" in txt:
  print("ex 26 - Yes, 'free' is present.")

# ex 27 - Check if NOT

txt = "The best things in life are free!"
print("example 27 NOT check" not in txt)

# -----------------------------------------------
# ----------------Slicing Strings-----------------
# -----------------------------------------------

# ex 28 - slicing

b = "ex28 - Hello, World!"
print(b[2:5]) # starts at index 0, does not include last element in range

# ex 29 - slice from start
b = "ex 29- Hello, World!"
print(b[:5]) # Get the characters from the start to position 5 (not included):

# ex 30 - slide to the end
b = "Hello, World!"
print(b[2:]) # Get the characters from position 2, and all the way to the end:

# ex 31 - negative indexing
b = "Hello, World!"
print(b[-5:-2])

# -----------------------------------------------
# ----------------Modify Strings-----------------
# -----------------------------------------------

# ex 32 - upper case
a = "ex32- Hello, World!"
print(a.upper())

# ex 33 - lower case
a = "ex33- Hello, World!"
print(a.lower())

# ex 34 - remove whitespace
a = "ex34- Hello, World! "
print(a.strip()) # returns "ex 34 - hello, World!"

# ex 35 - replace string
a = "ex35- Hello, World!"
print(a.replace("H", "J"))

# ex 36 - split string
a = "ex36- Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# -----------------------------------------------
# ----------------String Concatenation-----------
# -----------------------------------------------

# ex 37 - Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

# ex 38 - To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# -----------------------------------------------
# ----------------Format - Strings--------------
# -----------------------------------------------

# ex 39 - cannot combine strings and numbers
age = 36
txt = "ex 39- My name is John, I am " + age
print(txt)

# ex 40 - use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# ex 41 - The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# ex 42 - You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# -----------------------------------------------
# ----------------Escape Character--------------
# -----------------------------------------------

# ex 43 - double quotes
txt = "ex43- We are the so-called \"Vikings\" from the north."
# ex 44 - escape characters
txt = "ex 44- single quote \' backslash \\ new line \n carriage return \r tab \t backspace \b "

# -----------------------------------------------
# ----------------String Methods--------------
# -----------------------------------------------

# string built-in methods:

      # capitalize()	Converts the first character to upper case
      # casefold()	Converts string into lower case
      # center()	Returns a centered string
      # count()	Returns the number of times a specified value occurs in a string
      # encode()	Returns an encoded version of the string
      # endswith()	Returns true if the string ends with the specified value
      # expandtabs()	Sets the tab size of the string
      # find()	Searches the string for a specified value and returns the position of where it was found
      # format()	Formats specified values in a string
      # format_map()	Formats specified values in a string
      # index()	Searches the string for a specified value and returns the position of where it was found
      # isalnum()	Returns True if all characters in the string are alphanumeric
      # isalpha()	Returns True if all characters in the string are in the alphabet
      # isdecimal()	Returns True if all characters in the string are decimals
      # isdigit()	Returns True if all characters in the string are digits
      # isidentifier()	Returns True if the string is an identifier
      # islower()	Returns True if all characters in the string are lower case
      # isnumeric()	Returns True if all characters in the string are numeric
      # isprintable()	Returns True if all characters in the string are printable
      # isspace()	Returns True if all characters in the string are whitespaces
      # istitle()	Returns True if the string follows the rules of a title
      # isupper()	Returns True if all characters in the string are upper case
      # join()	Joins the elements of an iterable to the end of the string
      # ljust()	Returns a left justified version of the string
      # lower()	Converts a string into lower case
      # lstrip()	Returns a left trim version of the string
      # maketrans()	Returns a translation table to be used in translations
      # partition()	Returns a tuple where the string is parted into three parts
      # replace()	Returns a string where a specified value is replaced with a specified value
      # rfind()	Searches the string for a specified value and returns the last position of where it was found
      # rindex()	Searches the string for a specified value and returns the last position of where it was found
      # rjust()	Returns a right justified version of the string
      # rpartition()	Returns a tuple where the string is parted into three parts
      # rsplit()	Splits the string at the specified separator, and returns a list
      # rstrip()	Returns a right trim version of the string
      # split()	Splits the string at the specified separator, and returns a list
      # splitlines()	Splits the string at line breaks and returns a list
      # startswith()	Returns true if the string starts with the specified value
      # strip()	Returns a trimmed version of the string
      # swapcase()	Swaps cases, lower case becomes upper case and vice versa
      # title()	Converts the first character of each word to upper case
      # translate()	Returns a translated string
      # upper()	Converts a string into upper case
      # zfill()	Fills the string with a specified number of 0 values at the beginning









