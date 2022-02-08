#subtitle
print ("This project is for division as submission. \n")

#input
x = int (input ("Enter first number "))
y = int (input ("Enter second number "))

#the operation
mod = x
a = 0

for i in range (y):
    if mod >= y:
        a = a + 1
        mod = mod - y
    else:
        break

#output
print ("Outside the split part = ", a)
print ("Division remaining = ", mod)