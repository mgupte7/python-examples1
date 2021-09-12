if __name__ == '__main__':
    print('PyCharm')

# example 1 - syntax (indentation)

if 5 > 2:
    print("Five is greater than two")

# example 2 - variables

x = 5
y = "hello world"

print(y)

# example 3 - python variable types

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# example 4 - legal variable names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# example 5 - multiple values to multiple variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# example 6 - one value to multiple variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

# example 7 - unpack a collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# examples 8-9 - output variables

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

x = 5
y = 10
print(x + y)







