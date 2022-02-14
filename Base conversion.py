#subtitle
from unicodedata import decimal


print ("This project is for base conversion.")

#input
x = int (input ("Enter a number for base conversion "))
fb = input ("Chose a character between (binory, octal, decimal, hexadecimal) for first base ")
sb = input ("Chose a character between (binory, octal, decimal, hexadecimal) for second base ")

#variables
num = int (x)

#the operation
if fb == 'decimal':
    if sb == 'binory':
        print (x, "in binory", bin (num))

    if sb == 'octal':
        print (x, "in octal", oct (num))

    if sb == 'hexadecimal':
        print (x, "in hexadecimal", hex (num))

if fb == 'hexadecimal':
    if sb == 'binory':
        print (x, "in binory", bin (num))

    if sb == 'octal':
        print (x, "in octal", oct (num))

    if sb == 'decimal':
        print (x, "in decimal", decimal (num))

if fb == 'octal':
    if sb == 'binory':
        print (x, "in binory", bin (num))

    if sb == 'decimal':
        print (x, "in decimal", decimal (num))

    if sb == 'hexadecimal':
        print (x, "in hexadecimal", hex (num))

if fb == 'binory':
    if sb == 'octal':
        print (x, "in octal", oct (num))

    if sb == 'decimal':
        print (x, "in decimal", decimal (num))

    if sb == 'hexadecimal':
        print (x, "in hexadecimal", hex (num))