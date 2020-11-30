from turtle import *
from random import *

tree_1 = Turtle()
tree_2 = Turtle()
tree_3 = Turtle()
tree_4 = Turtle()

trees = [tree_1, tree_2, tree_3, tree_4]
x = -470

for tree in trees:
    tree.speed(90)
    tree.left(90) # Pen is looking up
    tree.color("brown")
    tree.pu() # Pull the pen up – no drawing when moving
    x += randint(140, 220)
    tree.goto(x, randint(-200, -50))
    tree.pd() # Pull the pen down – drawing when moving


def branch(tree, branch_length):
    angle = randint(20,30)
    shrink_factor = uniform(0.6, 0.8)
    branch_size = int(branch_length / 12)
    tree.pensize(branch_size)

    # Tree leafs
    if branch_length < 20:
        tree.color("green")
        tree.stamp()
        tree.color("brown")

    # Tree trunk and branches
    if branch_length > 10:
        tree.forward(branch_length)
        tree.left(angle)
        branch(tree, branch_length * shrink_factor)
        tree.right(angle * 2)
        branch(tree, branch_length * shrink_factor)
        tree.left(angle)
        tree.backward(branch_length)


for tree in trees:
    branch(tree, 120)