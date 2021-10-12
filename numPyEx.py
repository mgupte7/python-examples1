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
# ex 12 -
# ex 13 -
# ex 14 -
# ex 15 -
# ex 16 -
# ex 17 -
# ex 18 -
# ex 19 -

