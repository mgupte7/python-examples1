# ------------------------------------------------
# ----------------Python Read Files---------------
# ------------------------------------------------

# ex 1 - The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())

# ex 2 - Open a file on a different location:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

# ex 3 - Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))

# ex 4 - Read one line of the file:
f = open("demofile.txt", "r")
print(f.readline())

# ex 5 - Read two lines of the file:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# ex 6 - Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)

# ex 7 - Close the file when you are finish with it:
f = open("demofile.txt", "r")
print(f.readline())
f.close()

# ex 8
# ex 9
# ex 10