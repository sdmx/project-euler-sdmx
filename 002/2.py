# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import math

global value1
value1 = 1
global value2
value2 = 1
global limit
limit = 4000000
global result
result = 0
global increment

while value1 < limit and value2 < limit:
    increment = value1 + value2
    if value1 > value2:
        value2 = increment
    elif value2 > value1:
        value1 = increment
    else:
        value2 = increment
    if increment%2 == 0:
        result = result + increment
        print(result)
