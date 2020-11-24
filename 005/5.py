# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import math

def batteryCheck(input):
    for check in range (20,1,-1):
        if not input%check == 0:
            return False
    print("success: " + str(input))
    exit()

index = 20
while True:
    batteryCheck(index)
    index += 20
