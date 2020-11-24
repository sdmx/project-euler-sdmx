# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def squareSum(input):
    sum = 0
    for i in range (1,int(input)+1,1):
        sum = sum+(i*i)
    return sum

def sumSquare(input):
    sum = 0
    for i in range (1,int(input)+1,1):
        sum = sum+i
    sum = (sum*sum)
    return sum

print(sumSquare(100) - squareSum(100))
