#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
    n = -n
    print(f"Last digit of {number:d} is {n:d} and is", end=" ")
    if n > 5:
        print(F"greatr than 5")
    elif n == 0:
        print(F"0")
    else:
        print(F"less than 6 and not 0")
elif number == 0:
    print(f"Last digit of {number:d} is {n:d} and is 0")
else:
    print(f"Last digit of {number:d} is {n:d} and is", end=" ")
    if n > 5:
        print(F"greatr than 5")
    elif n == 0:
        print(F"0")
    else:
        print(F"less than 6 and not 0")
