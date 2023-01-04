import turtle as tr
import random as rd

# To make it easier to switch positions without having to draw a line across the picture
def back(length):
    tr.penup()
    tr.back(length)
    tr.pendown()

# Also gets used in other parts of the code
def randomColor():
    colors = ['green', 'forestgreen', 'limegreen', 'darkgreen', 'lime']
    return colors[rd.randint(0, len(colors) - 1)]

# Also gets used in other parts of the code
def setRandomLeafColor():
    color = randomColor()
    tr.pencolor(color)
    tr.fillcolor(color)

# Main function for drawing the tree
def tree (_stop, length, angle, switch):
    tr.pencolor("saddlebrown")
    tr.pensize(length/10)
    tr.forward(length)
    tr.left(angle)
    match switch:
        case 0: # Places leafs everywhere
            if(length - 10 >= _stop):
                tree(_stop, length-10, angle, switch)
            leaf(10 * rd.uniform(0.5, 0.7))
        case 1: # Only places them at the end
            if(length - 10 >= _stop):
                tree(_stop, length-10, angle, switch)
            else: leaf(10 * rd.uniform(0.5, 1))
        case 2:
            if(length - 10 >= _stop):
                tree(_stop, length-10, angle, switch)
            elif (length == _stop): 
                leaf(10 * rd.uniform(0.5, 1))
            randomLeaf()
    tr.right(angle*1.25)
    if(length - 10 >= _stop):
        tree(_stop, length-10, angle, switch)
    tr.right(angle*0.75)
    if(length - 10 >= _stop):
        tree(_stop, length-10, angle, switch)
    tr.left(angle)
    back(length)

# Decides on a random base if a leaf is drawen or not
def randomLeaf():
    threshhold = rd.randint(0, 10)
    if (threshhold < 5):
        leaf(10 * rd.uniform(0.5, 1))

# Main function for leafs
def leaf(length):
    tr.right(30)
    setRandomLeafColor()
    tr.begin_fill()
    rightSide(1, length)
    tr.left(95)
    tr.begin_fill()
    leftSide(1, length)
    tr.right(65)
    randomFruit()
# leafs are split up in 2 sides left and right
def rightSide(i, length):
    tr.left(10 * i)
    tr.forward(length)
    if (i < 4):
        rightSide(i + 1, length)
    tr.end_fill()
    back(length)
    tr.right(i* 10)
    
def leftSide(i, length):
    tr.right(10 * i )
    tr.forward(length)
    if (i < 4):
        leftSide(i + 1, length)
    tr.end_fill()
    back(length)
    tr.left(i * 10)

# Decides on a random base if a fruit is drawn or not
def randomFruit():
    threshhold = rd.randint(0, 10)
    if (threshhold < 5):
        fruit(10 * rd.uniform(0.5, 1))

def fruit():
    threshhold = rd.randint(0, 10)
    if (threshhold < 5):
        tr.pencolor("red")
        tr.fillcolor("red")
        tr.begin_fill()
        tr.circle(rd.randint(3, 5))
        tr.end_fill()
