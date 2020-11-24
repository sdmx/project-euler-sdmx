# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def checkPalendrome(input):
    standard = str(input)
    reverse = str(input)[::-1]

    if standard == reverse:
        return input
    else:
        return 0

largest = 1

for first in range(999,1,-1):
     for second in range(999,1,-1):
         result = first*second
         palendrome = checkPalendrome(result)
         if palendrome > largest:
             largest = palendrome

print(largest)
