# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math

problem = 600851475143
division = (problem+1)/2

# def isprime(number):
#     for i in range(2,600851475143):
#         if number%i == 0:
#             print(str(i) + ": Yes")

def findFactor(input):
    number = int(input)
    for divisor in range(2,number,1):
        if number%divisor==0:
            print(isPrime(divisor))

def isPrime(input):
    number = int(input)
    for divisor in range(number-1,2,-1):
        if number%divisor==0:
            return False
    return input

findFactor(problem)
