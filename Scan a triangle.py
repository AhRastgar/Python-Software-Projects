# subtitle
print ("This project is for scan a triangle. \n")

# input
x = int (input ("Enter a chord of triangle "))
y = int (input ("Enter a height of triangle "))
z = int (input ("Enter a base of triangle "))

# the operation
if x <= y + z:
    print ("yes, This is a triangle.")
else:
    print ("no, This is not a triangle.")