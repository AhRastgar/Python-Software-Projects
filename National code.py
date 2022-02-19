#subtitle
from ast import Mod
from operator import mod


print ("This project is for check a national code.")

#input
n = int (input ("Enter your national code "))

#the operation
num = n
import math

a = math.fmod (n, 10)
n = n / 10
b = (n % 10) * 2
n = n / 10
b = b + (n % 10) * 3
n = n / 10
b = b + (n % 10) * 4
n = n / 10
b = b + (n % 10) * 5
n = n / 10
b = b + (n % 10) * 6
n = n / 10
b = b + (n % 10) * 7
n = n / 10
b = b + (n % 10) * 8
n = n / 10
b = b + (n % 10) * 9
c = b % 11

if n != 1111111111:
    if n != 2222222222:
        if n != 3333333333:
            if n != 4444444444:
                if n != 5555555555:
                    if n != 6666666666:
                        if n != 7777777777:
                            if n != 8888888888:
                                if n != 9999999999:
                                    print ("This national code is true.")
if c == 0:
    if a == c:
        if c == 1:
            if a == 1:
                if c > 1:
                    if a == 11 - c:
                        print ("This national code is true.")