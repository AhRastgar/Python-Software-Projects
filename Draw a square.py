# #subtitle
print ("This project is for draw a square.")

# draw Square in Python Turtle
import turtle

#variable
t = turtle.Turtle()

#input
s = int(input("Enter the length of the side of square: "))

#the operation & output
for _ in range(4):
    t.forward(s)
    t.left(90)