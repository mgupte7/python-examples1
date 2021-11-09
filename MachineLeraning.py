# ------------------------------------------------
# --------------- Python Machine Learning --------
# ------------------------------------------------

# -------------------- Basics --------------------

# Discrete Data
# Numbers that are limited to integers.
# Example: The number of cars passing by.

# Continuous Data
# numbers that are of infinite value.
# Example: The price of an item, or the size of an item

# Categorical
# Data are values that cannot be measured up against each other.
# Example: a color value, or any yes/no values.

# Ordinal
# Data are like categorical data, but can be measured up against each other.
# Example: school grades where A is better than B and so on.

# --------------- Mean, Median, and Mode ---------

# --- Mean ---
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print("ex 1- mean")
print(x) # 89.77

# --- Median ---
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print("ex 2- median")
print(x) # 86.5

# --- Mode ---
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print("ex 3- mode")
print(x) #ModeResult Object = mode number (86), and count (3)

# -------------- Standard Deviation -------------

# Standard deviation is a number that describes how spread out the values are.
#
# A low standard deviation means that most of the numbers are close to the mean (average) value.
#
# A high standard deviation means that the values are spread out over a wider range.

# (ex 4 ) - Use the NumPy std() method to find the standard deviation:
import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print("ex 4- standard deviation")
print(x)

# (ex 5) - if you take the square root of the variance, you get the standard deviation
import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print("ex 5 - variance")
print(x)


# --------------- Machine Learning - Percentiles ---------

# (ex 6) - Use the NumPy percentile() method to find the percentiles:


ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print("ex 6 - percentle 75")
print(x) # The answer is 43, meaning that 75% of the people are 43 or younger.


# (ex 7) - What is the age that 90% of the people are younger than?


ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)

print("ex 7- percentile 90")
print(x)

# --------------- Machine Learning - Data Distribution ---------

# To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.

# (ex 8) - Create an array containing 250 random floats between 0 and 5:
x = numpy.random.uniform(0.0, 5.0, 250)

print("ex 8- random floats")
print(x)

# (ex 9) - To visualize the data set we can draw a histogram with the data we collected.

import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

# (ex 10) - Create an array with 100000 random numbers, and display them using a histogram with 100 bars:
x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

# --------------- Machine Learning - Normal Data Distribution ---------

# (ex 11) - A typical normal data distribution:
x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

# ------------------ Machine Learning - Scatter Plot ------------

# (ex 12) - Use the scatter() method to draw a scatter plot diagram:
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

# (ex 13) - A scatter plot with 1000 dots:
x = numpy.random.normal(5.0, 1.0, 1000) # the mean set to 5.0 with a standard deviation of 1.0
y = numpy.random.normal(10.0, 2.0, 1000) # mean set to 10.0 with a standard deviation of 2.0

plt.scatter(x, y)
plt.show()

# ------------------ Machine Learning - Linear Regression ------------

# (ex 14 - line of Linear Regression)
from scipy import stats

# Create the arrays that represent the values of the x and y axis:
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Create a function that uses the slope and intercept values to return a new value.
# This new value represents where on the y-axis the corresponding x value will be placed:
def myfunc(x):
  return slope * x + intercept

# Run each value of the x array through the function.
# This will result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, x))

# Draw the original scatter plot:
plt.scatter(x, y)
# Draw the line of linear regression:
plt.plot(x, mymodel)
# Display the diagram:
plt.show()

# ------------------- R for Relationship ------------------

# (ex 15- R - How well does my data fit in a linear regression?)

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print("ex 15 - finding R")
print(r)

# ------------------- Predict Future Values -------------------

# (ex 16) - Predict the speed of a 10 years old car:
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print("ex 16 - predict future values")
print(speed)

# (ex 17) - These values for the x- and y-axis should result in a very bad fit for linear regression:
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# (ex 18) - You should get a low R value for the LR above
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)

# ------------------- Machine Learning - Polynomial Regression -------------------

# (ex 19) - Polynomial Regression

# Create the arrays that represent the values of the x and y axis:
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# NumPy has a method that lets us make a polynomial model:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Then specify how the line will display, we start at position 1, and end at position 22:
myline = numpy.linspace(1, 22, 100)

# Draw the original scatter plot:
plt.scatter(x, y)
# Draw the line of polynomial regression:
plt.plot(myline, mymodel(myline))
# Display the diagram:
plt.show()

# ----------- R squared values ------------

# The relationship is measured with a value called the r-squared.
#
# The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

# (ex 20) - How well does my data fit in a polynomial regression?
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3)) # find a poly to the third degree

print(r2_score(y, mymodel(x)))

# ----------- Predict Future Values ------------

# (ex 21 - Predict the speed of a car passing at 17 P.M)

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

speed = mymodel(17)
print(speed)

# ------------------ Bad Fit? -------------------
# (ex 22 - These values for the x- and y-axis should result in a very bad fit for polynomial regression:)

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# (ex 23 - You should get a very low r-squared value.)


x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

# --------- Machine Learning - Multiple Regression ----------------

# (ex 24- Multiple Regression model)

import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv") # The Pandas module allows us to read csv files and return a DataFrame object.

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg,
# and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

# (ex 25 - Print the coefficient values of the regression object)
df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print("ex 25 - coefficient values of regression object")
print(regr.coef_)
# These values tell us that if the weight increase by 1kg,
# the CO2 emission increases by 0.00755095g.

# And if the engine size (Volume) increases by 1 cm3,
# the CO2 emission increases by 0.00780526 g.

# (ex 26 - Copy the example from before, but change the weight from 2300 to 3300)
df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)

# ---------------- Machine Learning - Scale ----------------

# The standardization method uses this formula: z = (x-u) / speed
# Where z = new value, x = original value, u = mean and s = standard deviation.

# (ex 27 - Scale all values in the Weight and Volume columns)
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

# ---------------- Predict CO2 Values ----------------

# (ex 28 - Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms)

scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)

# ---------------- Machine Learning - Train/Test ----------------

# (ex 29 - Start with a dataset)

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

# (ex 30 - Split into Train/ Test)
# training = random 80% of og data, testing = 20%

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# (ex 31 - display testing dataset)
plt.scatter(train_x, train_y)
plt.show()

# (ex 32 - display testing set)
plt.scatter(test_x, test_y)
plt.show()

# ---------------- Fit the Data Set ----------------

# (ex 33 - Draw a polynomial regression line through the data points)

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# (ex 34 - How well does my training data fit in a polynomial regression?)
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))

print(r2)

# ---------------- Bring in the Testing Set ----------------

# (ex 35 - Let us find the R2 score when using testing data)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x)) # using testing data instead

print(r2)

# ------------------- Predict Values -------------------

# (ex 36 - How much money will a buying customer spend, if she or he stays in the shop for 5 minutes?)

print(mymodel(5))

# ---------- Machine Learning - Decision Tree ----------

# (ex 37 - Read and print the data set)
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

print(df)

# To make a decision tree, all data has to be numerical.

# (ex 38 - Change string values into numerical values)
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df)

# (ex 39 - X is the feature columns, y is the target column)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)

# ( ex 40 - Create a Decision Tree, save it as an image, and show the image):
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()

# Rank <= 6.5 means that every comedian with a rank of 6.5 or lower will follow the True arrow (to the left), and the rest will follow the False arrow (to the right).
#
# gini = 0.497 refers to the quality of the split, and is always a number between 0.0 and 0.5, where 0.0 would mean all of the samples got the same result, and 0.5 would mean that the split is done exactly in the middle.
# Gini = 1 - (x/n)^2 - (y/n)^2
#
# samples = 13 means that there are 13 comedians left at this point in the decision, which is all of them since this is the first step.
#
# value = [6, 7] means that of these 13 comedians, 6 will get a "NO", and 7 will get a "GO".

# -------------------- Predict Values --------------------

# (ex 41 - Example: Should I go see a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of 7?)

# Use predict() method to predict new values:
print(dtree.predict([[40, 10, 7, 1]]))

# What would the answer be if the comedy rank was 6?
print(dtree.predict([[40, 10, 6, 1]]))

