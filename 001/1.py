import math

number = 1
total = 0

for number in range(1000):
	if (number%3 == 0 or number%5 == 0): total=number+total

print(total)
