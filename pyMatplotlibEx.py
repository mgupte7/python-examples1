# ------------------------------------------------
# ----------------Python Matplotlib---------------
# ------------------------------------------------


# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

import matplotlib.pyplot as plt
import numpy as np

# ex 1 - Draw a line in a diagram from position (0,0) to position (6,250):
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

# ---------- plotting without a line ----------

# ex 2 - Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# ---------- Default X-Points: 0, 1, 2, 3, ... ----------

# ex 3 - Plotting without x-points:
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# ------------- Markers -----------------

# ex 4 - Mark each point with a circle:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


# ex 5 - mark each point with a star

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*')
plt.show()

# ---------- Format Strings fmt ----------

# syntax format: marker|line|color

# ex 6 - Mark each point with a circle:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()


# ---------- Marker Size ----------

# ex 7 - Set the size of the markers to 20:

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# ---------- Marker Color ----------

# ex 8 - Set the EDGE color to red:

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# ex 9 - change FACE color
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r') # can use hex values (ex 4CAF50)

# ex 10 - change FACE and EDGE

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')

# ---------- Linestyle ----------

# ex 11 - Use a dotted line:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# ex 12 - dashed line
plt.plot(ypoints, linestyle = 'dashed')
plt.show()

# ---------- shorter syntax ----------

# ex 13 - shorter
plt.plot(ypoints, ls = ':')

# ---------- line color ----------

# ex 14 - Set the line color to red:

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

# ex 15 - change the line width
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()

# ex 16 - Draw two lines by specifying a plt.plot() function for each line:
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

# ex 17 - can add x and y values as arrays
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

# ---------- Create Labels for a Plot ----------
# With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.

# ex 18 - Add labels to the x- and y-axis:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# ---------- Create a Title for a Plot ----------

# ex 19 - Add a plot title and labels for the x- and y-axis:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# ------ Set Font Properties for Title and Labels ----------

# ex 20 - Set font properties for the title and labels:

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()

# ----------- Position the Title --------------

# You can use the loc parameter in title() to position the title.
# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

# ex 21 - Position the title to the left:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()

# ---------- Add Grid Lines to a Plot ----------

# ex 22 - Add grid lines to the plot:

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()

# ---------- Specify Which Grid Lines to Display ----------

# ex 23 - Display only grid lines for the x-axis:

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()

# ex 24 - Display only grid lines for the y-axis:

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'y')

plt.show()

# ---------- Set Line Properties for the Grid ----------

# ex 25 - Set the line properties of the grid:

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

# ---------- Display Multiple Plots ----------

# ex 26 - draw two subplots
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()

# ---------- Subplots Function ----------


# The subplots() function takes three arguments that describes the layout of the figure.
#
# The layout is organized in rows and columns, which are represented by the first and second argument.
#
# The third argument represents the index of the current plot.

plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.

#  ex 27 - Draw 2 plots on top of each other:

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()


# ex 28 - Draw 6 plots:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1) # 2 row, 3 col, 1st graph
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()

# ---------- Title ----------

# ex 29 - 2 plots, with titles:
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")
plt.show()

# ex 30 - Add a title for the entire figure:
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()

# ---------- Creating Scatter Plots ----------

# With Pyplot, you can use the scatter() function to draw a scatter plot.

# The scatter() function plots one dot for each observation. It needs two
# arrays of the same length, one for the values of the x-axis, and one for
# values on the y-axis:


# ex 31 - simple scatter plot
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

# ---------- Compare Plots ----------

# ex 32 - two plots on the same figure

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

# ---------- Color ----------

# ex 33 - Set your own color of the markers:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink') # change color

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()

# ---------- Color Each Dot ----------

# ex 34 - Set your own color of the markers:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()

# // skipped information about colormap and size of dots

# -------------------------------------
# ---------- Matplotlib Bars ----------

# ---------- Creating Bars ----------

# ex 35 - Draw 4 bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


# ex 36 - catagories will be first and second arguments of array
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)

# ---------- Horrizontal Bars ----------

# ex 37 - Draw 4 horizontal bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

# ---------- Bar Color ----------

# ex 38 - Draw 4 red bars:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()

# ex 39 - Draw 4 "hot pink" bars:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()

# ---------- Bar Width ----------

# ex 40 - Draw 4 very thin bars:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

# ---------- Bar Height ----------

# ex 41 - Draw 4 very thin bars:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()

# -------------------------------------------
# ---------- Matplotlib Histograms ----------


# ex 42 - A Normal Data Distribution by NumPy:
x = np.random.normal(170, 10, 250)

print(x)


# ex 43 - A simple histogram:

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()

# -------------------------------------------
# ---------- Matplotlib Pie Charts ----------

# ---------- Creating Pie Charts ----------

# ex 44 - A simple pie chart:
y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

# -------------------- Labels --------------------

# Add labels to the pie chart with the label parameter.
#
# The label parameter must be an array with one label for each wedge:

# ex 45 - A simple pie chart:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()

# ex 46 - Start the first wedge at 90 degrees:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

# ex 47 - Pull the "Apples" wedge 0.2 from the center of the pie:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

# -------------------- Shadow --------------------

# ex 48 - Add a shadow:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()

# -------------------- Colors --------------------

# You can set the color of each wedge with the colors parameter.
#
# The colors parameter, if specified, must be an array with one value for each wedge:

# ex 49 - Specify a new color for each wedge:

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()


# -------------------- Legend --------------------
# ex 50 - Add a legend:

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()


# ---------- Legend With Header ---------------

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 