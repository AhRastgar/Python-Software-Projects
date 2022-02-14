#subtitle
print ("This project is for draw a hollow rectangle.")

#input
x = int (input ("Enter a height for draw a rectangle "))
y = int (input ("Enter a wieght for draw a rectangle "))

#the operation
import turtle
t = turtle.Turtle ()

t.forward (x)
t.left (90)

t.forward (y)
t.left (90)

t.forward (x)
t.left (90)

t.forward (y)
t.left (90)