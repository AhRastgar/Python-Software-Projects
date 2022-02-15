#subtitle
print ("This project is for draw a 4 shape.")


#input
x = int (input ("Enter a size of square side "))
y = int (input ("Enter a number for width "))

#the operation
#square
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

#the operation & output
#rectangle
t.forward (x)
t. left (90)

t.forward (y)
t. left (90)

t.forward (x)
t. left (90)

t.forward (y)
t. left (90)

#the operation & output
#triangle
t.forward (x)
t.left (120)

t.forward (x)
t.left (120)

t.forward (x)
t.left (120)

#the operation & output
#circle
t.circle (x)