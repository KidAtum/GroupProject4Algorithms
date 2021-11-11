# Group G
# SCS 341 Algorithms Analysis
# Group Project 4

# imports
import matplotlib.pyplot as plt
import numpy as np

# read in image
img = plt.imread("venv/Images/GroupProject4FloorPlan.png")
# make plots
fig, ax = plt.subplots()

# take user input for sqr of house
# height or Y axis
print("Please Input the Height of the floor plan (input: 800 for this specific floor plan)")
sqrFootH = input()
sqrFootH = int(sqrFootH)
# width or X axis
print("Please Input the Width of the floor plan (input: 1400 for this specific floor plan)")
sqrFootW = input()
sqrFootW = int(sqrFootW)
# put user input into plot
plt.axis([0, sqrFootW, 0, sqrFootH])  # Modified axis

# Displaying grid
plt.grid()

# FIRST ROW
# first list is X axis and second list is Y axis (red for the actually router / extender)
# minus 10-20 for each because i want them to overlap
plt.plot([700, 560, 840, 910, 400, 180, 1185],
         [743, 743, 743, 743, 743, 743, 743], 'ro')
# plotting blue dots for how far the connection goes from the red dot
plt.plot([550, 850, 922.5, 410, 250, 1060],
         [743, 743, 743, 743, 743, 743], 'bo')
# plotting green dots for how far the connection goes from the red dot in a south direction on graph
plt.plot([700, 560, 840, 910, 400, 180, 1185],
         [593, 593, 593, 593, 593, 593, 593], 'go')

# SECOND ROW
# first list here is the second row of starting router / extender (color cyan) (co)
plt.plot([700, 560, 840, 910, 400, 180, 1185],
         [525, 525, 525, 525, 525, 525, 525], 'co')
# plotting magenta to show how far the connection goes from the cyan dot east west (mo)
plt.plot([550, 850, 922.5, 410, 250, 1060 - 72.5, 1025],
         [525, 525, 525, 525, 525, 525, 525], 'mo')
# plotting yellow to show how far the connection goes from the cyan dot north south (yo)
plt.plot([700, 560, 840, 910, 400, 180, 1185, 700, 560, 840, 910, 400, 180, 1185, 1030],
         [675, 675, 675, 675, 675, 600.5, 675, 375, 375, 375, 452.5, 452.5, 452.5, 452.5, 452.5], 'yo')

# THIRD ROW
# first list here is the second row of starting router / extender (color red) (ro)
plt.plot([700, 560, 840, 910, 400, 180, 1185],
         [375, 375, 375, 375, 375, 375, 375], 'ro')
# plotting blue to show how far the connection goes from the red dot east west (bo)
plt.plot([550, 850, 922.5, 410, 250, 1060 - 72.5, 1099],
         [375, 375, 375, 375, 375, 375, 375], 'bo')
# plotting green to show how far the connection goes from the red dot north south (go)
plt.plot([700, 560, 840, 910, 400, 180, 1185, 700, 560, 840, 910, 400, 180, 1185, 1030],
         [525, 525, 525, 525, 525, 525, 525, 225, 225, 225, 225, 303.5, 303.5, 225, 225], 'go')

# FINAL ROW
# first list here is the second row of starting router / extender (color cyan) (co)
plt.plot([700, 560, 840, 910, 400, 180, 1185],
         [88, 88, 88, 88, 88, 88, 88], 'co')
# plotting magenta to show how far the connection goes from the cyan dot east west (mo)
plt.plot([550, 850, 922.5, 410, 250, 1060 - 72.5, 1025],
         [88, 88, 88, 88, 88, 88, 88], 'mo')
# plotting yellow to show how far the connection goes from the cyan dot north south (yo)
plt.plot([700, 560, 840, 910, 400, 180, 1185],
         [238, 238, 238, 238, 238, 238, 238], 'yo')

# showing image
ax.imshow(img)
plt.imshow(np.flipud(img), cmap='gray', origin='lower')

# show plots
plt.show()
# print what it means
# top section
print("""
Top Section : 
Red nodes are the starting routers
Blue nodes show how far left and right the connection goes
Green nodes show how far down the connections goes""")
# 2nd section
print("""
2nd Section : 
Cyan nodes are the starting routers
Magenta nodes show how far left and right the connection goes
Yellow nodes show how far up and down the connections goes""")
# 3rd section
print("""
3rd Section : 
Red nodes are the starting routers
Blue nodes show how far left and right the connection goes
Green nodes show how far up and down the connections goes""")
# Final section / bottom
print("""
Last / Bottom Section : 
Cyan nodes are the starting routers
Magenta nodes show how far left and right the connection goes
Yellow nodes show how far up and down the connections goes
""")
# print done
print("Calculating...")
print()
print("28 Routers / Extenders needed to cover whole house..")
