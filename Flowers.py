import turtle as tr
import random as rd
import Trees as ts
import math as mt

def randomFlowerColor():
    colors = ['red', 'purple', 'blue', 'yellow']
    return colors[rd.randint(0, len(colors) - 1)]

def setFlowerColor():
    color = randomFlowerColor()
    tr.pencolor(color)
    tr.fillcolor(color)

# Leafs are divided in two kinds a and b
def FlowerLeafsA(color_f):
    color = randomFlowerColor()
    tr.pencolor(color)
    tr.fillcolor(color)
    tr.begin_fill()
    tr.right(90)
    tr.circle(5)
    tr.end_fill()
    tr.left(90)
    tr.pencolor(color_f)

def FlowerLeafsB(length):
    setFlowerColor()
    tr.begin_fill()
    for i in range(4):
        tr.circle(length, extent=180)
        tr.left(90)
    tr.end_fill()

def OuterFlowerLeaf(length): # has to be make more efficient
    tr.right(90)
    setFlowerColor()
    tr.begin_fill()
    tr.circle(length/2)
    tr.end_fill()
    tr.left(90)
    ts.back(-length/2)
    ts.back(-mt.sqrt(pow(length, 2) + pow(length, 2)))
    tr.left(135)
    FlowerLeafsB(length)
    tr.left(45)
    ts.back(-mt.sqrt(pow(length, 2) + pow(length, 2)))
    tr.penup()
    for i in range(2):
        tr.left(90)
        ts.back(-length)
    tr.left(90)
    FlowerLeafsB(length)
    tr.penup()
    for i in range(2):
        tr.right(90)
        ts.back(length)
    tr.left(90)
    ts.back(length/2)
    tr.pendown()

def FlowerLeafs(length, color):
     if (length == 20):
        FlowerLeafsA(color)
     else:
        ts.blatt((length/10)*2)

def FlowerA(length, color):
    tr.pencolor(color)
    tr.forward(length)
    tr.left(20)
    if (length > 20):
        FlowerA(length - 5, color)
    FlowerLeafs(length, color)
    tr.right(40)
    if (length > 20):
        FlowerA(length - 5, color)
    tr.left(20)
    tr.back(length)

def FlowerB(length):
    tr.forward(length/2)
    tr.left(20)
    ts.blatt(5)
    tr.left(280)
    ts.blatt(5)
    tr.left(60)
    tr.forward(length/1.5)
    OuterFlowerLeaf(length * 0.33)
    tr.back(length/2+length/1.5)