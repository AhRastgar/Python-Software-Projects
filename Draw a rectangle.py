#subtitle
print ("This project is for draw a rectangle.")

# draw Rectangle in Python Turtle
import turtle

t = turtle.Turtle()

# input & variables
l = int(input("Enter the length of the Rectangle: "))
w = int(input("Enter the width of the Rectangle: "))

# the operation & output
t.forward(l)
t.left(90)

t.forward(w)
t.left(90)

t.forward(l)
t.left(90)

t.forward(w)
t.left(90)