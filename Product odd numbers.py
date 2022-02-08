#subtitle
print ("This project is for product between numbers.")

#input
x = int (input ("Enter first number "))
y = int (input ("Enter second number "))

#the operation
prd = 1

for i in range (x , y):
    if i % 2 == 1:
        prd = prd * i

#output
print ("Product odd numbers = ", prd)