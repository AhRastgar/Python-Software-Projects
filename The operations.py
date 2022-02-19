#subtitle
from ast import Num
from cmath import sqrt

print ("This project is for the operations.")

#input
x = int (input ("Enter a number for number of numbers "))

#the operation
stash = 0
sum = 0
avg = 0
firstInit = 0
sum2 = 0

for i in range (x):
    b = int (input ("Enter a number "))
    sum += b

for j in range (x):
    a = int (input ("Enter a number "))

    if j == 0:
        min = a
        max = a

    if a < min:
        min = a

    if a > max:
        max = a

for r in range (x):
    c = int (input ("Enter a number "))
    avg = sum / x

for h in range (x):
    d = int (input ("Enter a number "))
    stash = d - avg
    sum2 += pow (stash , 2)
    stdDev = sqrt (sum2 / 5)

#output
print ("Minimum = ", min)
print ("Maximum = ", max)
print ("Sum = ", sum)
print ("Avg = ", avg)
print ("Standard deviation = ", stdDev)