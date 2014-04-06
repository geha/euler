#!/usr/bin/env python

def square_sum(number):
	return sum([int(x)**2 for x in str(number)])

count = 0
square_set = set()

# calculate all possible sum for numbers 1 to 10**7
for i in range (1, 568):
	number = i
	while True:
		if number == 89:
			square_set.add(i)
			break

		number = square_sum(number)


for i in range(1, 10**7+1):
	if square_sum(i) in square_set:
		count += 1
	if (i % 10**4) == 0:
		print (i)


print(count)
