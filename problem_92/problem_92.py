#!/usr/bin/env python

def square_sum(number):
	return sum([int(x)**2 for x in str(number)])

count = 0
table = [None]*568

for i in range (1, 568):
	number = i
	while True:
		if number == 89:
			table[i] = True
			break
		if number == 1:
			table[i] = False
			break

		number = square_sum(number)


for i in range(1, 10**7+1):
	count += table[square_sum(i)]
	if (i % 10**4) == 0:
		print (i)


print(count)
