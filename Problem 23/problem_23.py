#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def sumDevisors (number):
	sum = 1
	for i in range(2, math.ceil(math.sqrt(number))):
		if ((number/i) % 1 == 0):
			sum += i + int(number/i)

	return sum

def isAbundant (number):
	ret = False
	if (sumDevisors(number) > number):
		ret = True

	return ret

def isSumOfAbundant (number, abundantList):
	ret = False
	for i in range(0, len(abundantList)):
		if (abundantList[i] > number or ret):
			break

		for j in range(i, len(abundantList)):
			if (abundantList[j] > number):
				break

			if (abundantList[i] + abundantList[j] > number):
				break

			if (abundantList[i] + abundantList[j] == number):
				ret = True
				break

	return ret


def main():
	abundantList = []

	for i in range (1, 28124):
		if (isAbundant(i)):
			abundantList.append(i)

	print("Calculation of List finished")

	sum = 0
	for i in range (1, 28124):
		if (not(isSumOfAbundant(i, abundantList))):
			sum += i

		if (i % 100 == 0):
			print (i)



	print()
	print (sum)

	return 0

if __name__ == '__main__':
	main()

