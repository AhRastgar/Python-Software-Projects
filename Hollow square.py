#subtitle
print ("This project is for draw a hollow square.")

#input
x = int (input ("Enter a size of square side "))

#the operation
import turtle
t = turtle.Turtle ()

t.forward (x)
t.left (90)

t.forward (x)
t.left (90)

t.forward (x)
t.left (90)

t.forward (x)
t.left (90)