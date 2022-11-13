import turtle as tr
import random as rd

def back(length):
    tr.penup()
    tr.back(length)
    tr.pendown()

def randomColor():
    colors = ['green', 'forestgreen', 'limegreen', 'darkgreen', 'lime']
    return colors[rd.randint(0, len(colors) - 1)]

def setRandomLeafColor():
    color = randomColor()
    tr.pencolor(color)
    tr.fillcolor(color)

def branchL(length):
    tr.forward(length)
    tr.left(120)
    tr.forward(length *1.6)
    tr.back(length *1.6)
    tr.right(120)
    if (length-5 >= 10):
        branchL(length-5)        
    tr.right(120)
    tr.forward(length*1.6)
    back(length*1.6)
    tr.left(120)
    back(length)

def branchR(length):
    tr.forward(length)
    tr.right(120)
    tr.forward(length *1.6)
    tr.back(length *1.6)
    tr.left(120)
    if (length -5 >= 10):
        branchL(length-5)           
    tr.left(120)
    tr.forward(length*1.6)
    back(length*1.6)
    tr.right(120)
    back(length)

def ChristmasTree(length):
    tr.pencolor('dark green')
    tr.forward(length)
    tr.left(110)
    branchL((length * 0.6))
    tr.right(220)
    branchR(length * 0.6)
    tr.left(110)
    if(length-10 >= 10):
        ChristmasTree(length-10)
    
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

def blatt(length):
    tr.right(30)
    setRandomLeafColor()
    tr.begin_fill()
    rightSide(1, length)
    tr.left(95)
    tr.begin_fill()
    leftSide(1, length)
    tr.right(65)

def baum (_stop, length, angle, switch):
    tr.pencolor("saddlebrown")
    tr.pensize(length/10)
    tr.forward(length)
    tr.left(angle)
    match switch:
        case 0:
            if(length - 10 >= _stop):
                baum(_stop, length-10, angle, switch)
            blatt(10 * rd.uniform(0.5, 1))
        case 1:
            if(length - 10 >= _stop):
                baum(_stop, length-10, angle, switch)
            else: blatt(10 * rd.uniform(0.5, 1))
    tr.right(angle*1.5)
    if(length - 10 >= _stop):
        baum(_stop, length-10, angle, switch)
    tr.right(angle*0.5)
    if(length - 10 >= _stop):
        baum(_stop, length-10, angle, switch)
    tr.left(angle)
    back(length)