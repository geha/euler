#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def sumDevisors (number):
	sum = 1
	for i in range(2, int(math.sqrt(number))+1):
		if (number % i == 0):
			sum += i + int(number/i)

		if (i == math.sqrt(number)):
			sum -= i

	return sum

def isAbundant (number):
	ret = False
	if (sumDevisors(number) > number):
		ret = True

	return ret

def isSumOfAbundant (number, abundantList):
	ret = False

	if (any (number - i in abundantList for i in abundantList)):
		ret = True

	return ret

def main():
	abundantList = set()

	for i in range(1, 20162):
		if (isAbundant(i)):
			abundantList.add(i)

	sum = 0
	for i in range (1, 20162):
		if (not(isSumOfAbundant(i, abundantList))):
			sum += i

		if (i % 1000 == 0):
			print (i)

	print()
	print (sum)

	return 0

if __name__ == '__main__':
	main()

