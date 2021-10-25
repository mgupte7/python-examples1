# --------------------------------------------------
# ---------------- NumPy- Number Python ------------
# --------------------------------------------------

# NumPy provides an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions
# that make working with ndarray very easy

# ----------------- Getting Started -----------------

# ex 1
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

# ex 2 - NumPy package can be referred to as np instead of numpy.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# ex 3 - The version string is stored under __version__ attribute.
print(np.__version__)

# ----------------- Creating Arrays -----------------

# ex 4 - We can create a NumPy ndarray object by using the array() function.
arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

# ex 5 - Use a tuple to create a NumPy array:
arr = np.array((1, 2, 3, 4, 5))

print(arr)

# ----------------- Dimensions in Arrays -----------------
# ex 6 - Create a 0-D array (Scalar) with value 42
arr = np.array(42)

print(arr)

# ex 7 - Create a 1-D array containing the values 1,2,3,4,5:
arr = np.array([1, 2, 3, 4, 5])

print(arr)

# ex 8 - Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

# ex 9 - Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

# ----------------- Check Number of Dimensions -----------------

# ex 10 - Check how many dimensions the arrays have:
a = np.array(42) # 0
b = np.array([1, 2, 3, 4, 5]) # 1
c = np.array([[1, 2, 3], [4, 5, 6]]) # 2
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# ----------------- Higher Dimensional Arrays -----------------

# ex 11 - Create an array with 5 dimensions and verify that it has 5 dimensions:
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
# ----------------- NumPy Array Indexing -----------------
# ex 12 - Get the first element from the following array:
arr = np.array([1, 2, 3, 4])
print(arr[0])

# ex 13 - Get the second element from the following array.
arr = np.array([1, 2, 3, 4])
print(arr[1])

# ex 14 - Get third and fourth elements from the following array and add them.
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

# ex 15 - Access the 2nd element on 1st dim:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1]) # array first, element second

# ex 16 - Access the 5th element on 2nd dim:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd dim: ', arr[1, 4])

# ex 17 - Access the third element of the second array of the first array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# ex 18 - (negative indexing) Print the last element from the 2nd dim:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# ----------------- NumPy Array Slicing -----------------
# ex 19 - Slice elements from index 1 to index 5 from the following array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# ex 20 - Slice elements from index 4 to the end of the array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

# ex 21 - Slice elements from the beginning to index 4 (not included):
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

# ex 22 - (Negative Slicing) Slice from the index 3 from the end to index 1 from the end:
print("example 22")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

# ex 23 - (STEP) Return every other element from index 1 to index 5:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
# ex 24 - Return every other element from the entire array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2]) # starts from first element

# ex 25 - (Slicing 2-D Arrays) From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

# ex 26 - From both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

# ex 27 - From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

# ----------------- NumPy Data Types -----------------

# ex 28 - Get the data type of an array object:
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# ex 29 - Get the data type of an array containing strings:
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# (Creating Arrays With a Defined Data Type)

# ex 30 -Create an array with data type string:
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# ex 31 - Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# ----------------- NumPy Array Copy vs View -----------------

# copy owns the data and any changes made to the copy will not affect original array
# view does not own the data and any changes made to the view will affect the original array

# ex 32 - Make a copy, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

# ex 33 - Make a view, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

# ex 34 - Print the value of the base attribute to check if an array owns it's data or not:

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base) # print "none" because copy
print(y.base)

# ----------------- NumPy Array Shape -----------------

# NumPy arrays have an attribute called "shape" that returns a tuple with each index having the number of corresponding elements.

# ex 35 - Print the shape of a 2-D array:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) # (2,4)

# ex 36 - Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr) # [[[[[1 2 3 4]]]]]
print('shape of array :', arr.shape)

# ----------------- NumPy Array Reshaping -----------------

# *** Reshape From 1-D to 2-D ***

# ex 37 - Convert the following 1-D array with 12 elements into a 2-D array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) # The outermost dimension will have 4 arrays, each with 3 elements:
print(newarr)

# ex 38 - Convert the following 1-D array with 12 elements into a 3-D array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2) # The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
print(newarr)

# *** Returns Copy or View? ***

# ex 39 - Check if the returned array is a copy or a view:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) # will print original value if view

# *** Unknown Dimension ***

# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.

# ex 40 - Convert 1D array with 8 elements to 3D array with 2x2 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1) # will organize elements into 2x2x2
print(newarr)

# *** Unknown Dimension ***
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.

# ex 41 - Convert the array into a 1D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

# ----------------- NumPy Array Iterating -----------------

# ex 42 - Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

# ex 43 - Iterating 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

# ex 44 - Iterate on each scalar element of the 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)

# ex 45 - Iterate on the elements of the following 3-D array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)

# ex 46 - Iterate down to the scalars:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr: # will convert to scalar when nesting loops
  for y in x:
    for z in y:
      print(z)

# ex 47 - Iterate through the following 3-D array:
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr): # other form of changing to scalar
  print(x)

# *** Iterating Array With Different Data Types ***

# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
# We need to do this because NumPy does not change the data type of the element in-place

# ex 48 - Iterate through the array as a string:
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']): # extra space = buffer, enable it in nditer() by passing flags=['buffered'].


  print(x)

# *** Iterating Array With Different Data Types ***

# ex 49 - Iterate through every scalar element of the 2D array skipping 1 element:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

# *** Enumerated Iteration Using ndenumerate() ***

# ex 50 - Enumerate on following 1D arrays elements:
print("example 50")
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# ex 51 - Enumerate on following 2D array's elements:
print("example 51")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# ----------------- NumPy Joining Array -----------------

# ex 52 - Join two arrays

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr) # [1 2 3 4 5 6]

# ex 53 - Join two 2-D arrays along rows (axis=1):

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

#[[1 2 5 6]
# [3 4 7 8]]

print(arr)

# *** Joining Arrays Using Stack Functions ***

# ex 54 - We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

# [[1 4]
#  [2 5]
#  [3 6]]

print(arr)

# *** Stacking Along Rows ***

# ex 55 - NumPy provides a helper function: hstack() to stack along rows.

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

# [1 2 3 4 5 6]

print(arr)

# *** Stacking Along Columns ***

# ex 56 - NumPy provides a helper function: vstack()  to stack along columns.

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

# [[1 2 3]
#  [4 5 6]]

print(arr)

# *** Stacking Along Height (depth) ***

# ex 57 - NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

# [[[1 4]
#   [2 5]
#   [3 6]]]

print(arr)

# ----------------- NumPy Splitting Array -----------------

# Joining merges multiple arrays into one and Splitting breaks one array into multiple.

# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

# ex 58 - Split the array in 3 parts:

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr) # [array([1, 2]), array([3, 4]), array([5, 6])]

# ex 59 - Split the array in 4 parts:
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4) # [array([1, 2]), array([3, 4]), array([5]), array([6])]

print(newarr)

# *** Split Into Arrays ***

# The return value of the array_split() method is an array containing each of the split as an array.

# If you split an array into 3 arrays, you can access them from the result just like any array element:

# ex 60 - Access the splitted arrays:
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0]) # [1 2]
print(newarr[1]) # [3 4]
print(newarr[2]) # [5 6]

# *** Splitting 2-D Arrays ***

# Use the same syntax when splitting 2-D arrays.

# Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

# ex 61 - Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

# [array([[1, 2],
#        [3, 4]]), array([[5, 6],
#        [7, 8]]), array([[ 9, 10],
#        [11, 12]])]

# ex 62 - Split the 2-D array into three 2-D arrays along rows.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

# ex 63 - Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)

# ----------------- NumPy Searching Arrays -----------------

# You can search an array for a certain value, and return the indexes that get a match.

# To search an array, use the where() method.

# ex 64 - Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x) # (array([3, 5, 6]),)

# ex 65 - ind the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x) # (array([1, 3, 5, 7]),)

# ex 66 - Find the indexes where the values are odd:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)

# *** Search Sorted ***

# The searchsorted() method is assumed to be used on sorted arrays.

# ex 67 - Find the indexes where the value 7 should be inserted:

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

# *** Search From the Right Side ***

# ex 68 - Find the indexes where the value 7 should be inserted, starting from the right:
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

# *** Multiple Values ***

# To search for more than one value, use an array with the specified values.

# ex 69 - Find the indexes where the values 2, 4, and 6 should be inserted:
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x) # [1 2 3]

# ----------------- NumPy Sorting Arrays -----------------

# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

# The NumPy ndarray object has a function called sort(), that will sort a specified array.

# ex 70 - Sort the array:
arr = np.array([3, 2, 0, 1])

print(np.sort(arr)) # [0 1 2 3]

# ex 71 - Sort the array alphabetically:
arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr)) # ['apple' 'banana' 'cherry']

# ex 72 - Sort a boolean array:
arr = np.array([True, False, True])

print(np.sort(arr)) # [False True True]

# *** Sorting a 2-D Array ***

# If you use the sort() method on a 2-D array, both arrays will be sorted:

# ex 73 - Sort a 2-D array:
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

# [[2 3 4]
#  [0 1 5]]

# ----------------- Filtering Arrays -----------------

# Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, you filter an array using a boolean index list.

# ex 74 - Create an array from the elements on index 0 and 2:
arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr) # [41 43]

# *** Creating the Filter Array ***
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.

# ex 75 - Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr) # [False, False, True, True]
print(newarr) # [43 44]

# ex 76 - Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr) # [False, True, False, True, False, True, False]
print(newarr) # [2 4 6]

# *** Creating Filter Directly From Array ***
# The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.

# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

# ex 77 - Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr) # [False False  True  True]
print(newarr) # [43 44]

# ex 78 - Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr) # [False  True False  True False  True False]
print(newarr) # [2 4 6]

