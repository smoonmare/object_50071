from turtle import *
from random import *

speed(85)
left(90)

def branch(step):
    angle = randint(20,30)
    shrink_factor = uniform(0.6, 0.8)

    if step > 10:
        forward(step)
        left(angle)
        branch(step*shrink_factor)
        right(angle*2)
        branch(step*shrink_factor)
        left(angle)
        backward(step)


branch(100)