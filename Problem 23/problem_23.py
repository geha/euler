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
	for i in range(0, len(abundantList)):
		if (abundantList[i] >= number or ret):
			break

		diff = number - abundantList[i]

		if (diff in abundantList):
			ret = True
			break

	return ret

def main():
	abundantList = []

	for i in range(1, 20162):
		if (isAbundant(i)):
			abundantList.append(i)

	sum = 0
	for i in range (1, 20162):
		if (not(isSumOfAbundant(i, abundantList))):
			sum += i

		if (i % 100 == 0):
			print (i)

	print()
	print (sum)

	return 0

if __name__ == '__main__':
	main()

