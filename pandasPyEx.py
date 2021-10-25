# --------------------------------------------------
# ---------------- Pandas Tutorial -----------------
# ----------- Panel Data/ Python Data Analysis -----


# Pandas is a Python library. Pandas is used to analyze data.

# General information

# Why Use Pandas?
# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# Relevant data is very important in data science.

# What Can Pandas Do?
# Pandas gives you answers about the data. Like:
# Is there a correlation between two or more columns?
# What is average value? Max value? Min value?

# ---------------------------------------------------------
# --------------- Pandas Getting Started ------------------


import pandas as pd

# ex 1
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

#     cars  passings
# 0    BMW         3
# 1  Volvo         7
# 2   Ford         2


# ex 2 - The version string is stored under __version__ attribute.

print(pd.__version__)  # 1.3.3

# ----------------------------------------------------
# --------------- What is a Series? ------------------

# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# ex 3 - Create a simple Pandas Series from a list:
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# 0    1
# 1    7
# 2    2
# dtype: int64


# -------------------- Labels --------------------------------

# ex 4 - Return the first value of the Series:

print(myvar[0])

# -------------------- Create Labels ------------------------

# ex 5 - Create you own labels:
a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)

# ex 6 - Return the value of "y":
print(myvar["y"])

# --------------- Key/Value Objects as Series ----------------

# ex 7 - Create a simple Pandas Series from a dictionary:
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# ex 8 - Create a Series using only data from "day1" and "day2":
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index=["day1", "day2"])

print(myvar)

# ex 9 - Create a DataFrame from two Series:
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

# --------------------------------------------------------
# ------------------ Pandas DataFrames -------------------

# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

# ex 10 - Create a simple Pandas DataFrame:
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)  # load data into a DataFrame object:

print(df)

# ****************** Locate Row **********************

# As you can see from the result above, the DataFrame is like a table with rows and columns.

# ex 11 -  Pandas use the loc attribute to return one or more specified row(s)
print(df.loc[0])
# refer to the row index: 420, 50

# ex 12 - Return row 0 and 1:
print(df.loc[[0, 1]])
# use a list of indexes: 420, 50; 380, 40

# ****************** Named Indexes *******************

# With the index argument, you can name your own indexes.

# ex 13 - Add a list of names to give each row a name:
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df)  # changes the rows on the uttermost left to days instaed of numbers

# ****************** Locate Named Indexes *******************

# ex 14 - Return "day2":
print(df.loc["day2"])  # refer to the named index: 380, 40

# ************* Load Files Into a DataFrame ******************* // CSV not downloaded on this laptop

# If your data sets are stored in a file, Pandas can load them into a DataFrame.

# ex 15 - Load a comma separated file (CSV file) into a DataFrame:
df = pd.read_csv('data.csv')

print(df)

# ------------------------------------------------------
# ------------------ Pandas Read CSV -------------------

# ex 16 - Load the CSV into a DataFrame:
df = pd.read_csv('data.csv')
print(df.to_string())  # will print everything

# ex 17 - Print a reduced sample:
df = pd.read_csv('data.csv')
print(df)  # only prints first and last 5 rows

# -------------------------------------------------------
# ------------------ Pandas Read JSON -------------------

# Big data sets are often stored, or extracted as JSON.

# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

# ex 18 - Load the JSON file into a DataFrame:
df = pd.read_json('data.json')
print(df.to_string())

# ************* Dictionary as JSON *******************

# If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:

# ex 19 - Load a Python Dictionary into a DataFrame:
data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}

df = pd.DataFrame(data)

print(df)
# ------------------------------------------------------------------
# ------------------ Pandas - Analyzing DataFrames------------------

# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# The head() method returns the headers and a specified number of rows, starting from the top.

# ex 20 - Get a quick overview by printing the first 10 rows of the DataFrame:
df = pd.read_csv('data.csv')
print(df.head(10))

# ex 21 - Print the first 5 rows of the DataFrame:
df = pd.read_csv('data.csv')
print(df.head())  # default = 5

# ex 22 - Print the last 5 rows of the DataFrame:
# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
print(df.tail())

# ************* Info About the Data *******************
# The DataFrames object has a method called info(), that gives you more information about the data set.

# ex 23 - Print information about the data:
print(df.info())
# --> there are 169 rows and 4 columns:
# --> name of each column, with the data type:
# --> null values may be present, remove = "cleaning data"
