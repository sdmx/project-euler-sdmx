# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math

index=1
counter=1

def isPrime(input):
    input = int(input)
    for i in range(int(round(input/3)),1,-1):
        if input%i==0:
            return False
    return True

while counter<10001:
    index+=2
    if isPrime(index)==True:
        counter+=1

print (index, counter)
