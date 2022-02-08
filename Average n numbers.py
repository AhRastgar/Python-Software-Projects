#subtitle
print ("This project is for Average between n numbers.")

#input
x = int (input ("Enter a number for number of number "))

#the operation
sum = 0

for i in range (x):
    y = int (input ("Enter a number "))
    sum = sum + y

#output
print ("Average is = ", sum/x)