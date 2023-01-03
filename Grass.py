import Trees as ts
import turtle as tr
import math as mt
import random as rd

#Generator for the grass. Will create a bunch of grass leafes over a pre determind length
def grass(length, grassPara):
    ts.back(length)
    current_length = 0
    while (current_length < length * 2):
        rd_length = rd.uniform(grassPara[0][0], grassPara[0][1])
        rd_height = rd.uniform(grassPara[1][0], grassPara[1][1])
        current_length += rd_length
        ts.setRandomLeafColor()
        tr.begin_fill()
        grasLeafe(rd_length, rd_height)
        tr.end_fill()
    ts.back(length)

#Generator for the grass leafes which will form the grass section in the end
def grasLeafe(length, height):
    angle = mt.degrees(mt.atan(height/(length/2)))
    hypotenuse = mt.sqrt(pow(length/2, 2) + pow(height, 2))
    tr.forward(length)
    ts.back(length)
    tr.left(angle)
    tr.forward(hypotenuse)
    tr.right(180 - 2*(90 - angle))
    tr.forward(hypotenuse)
    tr.left(angle)