#subtitle
from cmath import sqrt


print ("This project is for diameter of square.")

#input
x = int (input ("Enter a number for side of square "))

#the operation
num = int (x)

y = 1.4142135623730950488016887242097 * num

import turtle
t = turtle.Turtle ()

t.forward (x)
t.left (90)

t.forward (x)
t.left (90)

t.forward (x)
t.left (90)

t.forward (x)

t.left (135)
t.forward (y)

t.left (135)
t.forward (x)

t.left (135)
t.forward (y)