#subtitle
print ("This project is for draw a hollow triangle.")

#input
x = int (input ("Enter a number for side of triangle "))
dir = str (input ("Enter a direction between (up, down, left, right)"))

#the operaion
import turtle
t = turtle.Turtle ()

if dir == 'up':
    t.forward (x)
    t.left (60)

    t.forward (x)
    t.left (60)

    t.forward (x)
    t.left (60)

if dir == 'down':
    t.forward (x)
    t.right (60)

    t.forward (x)
    t.right (60)

    t.forward (x)
    t.right (60)

if dir == 'left':
    t.left (90)
    t.forward (x)
    t.left (120)

    t.forward (x)
    t.left (120)

    t.forward (x)
    t.left (120)

if dir == 'right':
    t.left (90)
    t.forward (x)
    t.right (120)

    t.forward (x)
    t.right (120)

    t.forward (x)
    t.right (120)