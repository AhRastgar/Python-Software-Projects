#subtitle
print ("This project is for divisor against.")

#input
x = int (input ("Enter a number "))

#the operation
num = x

for i in range (1 , x + 1):
    if num % i == 0:
        print ("divide your number is" , i)