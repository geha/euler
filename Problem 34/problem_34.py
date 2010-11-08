#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def isFacSum(number, faclist):
	ret = False
	sum = 0
	string = str(number)
	for i in range(0, len(string)):
		sum += faclist[int(string[i])]

	if (number == sum):
		ret = True

	return ret

def main():
	faclist = [1]
	for i in range(1,10):
		faclist.append(math.factorial(i))

	sum = 0
	for i in range(3, 2903041):
		if (isFacSum(i, faclist)):
			sum += i
			print(i)


	print(sum)

	return 0

if __name__ == '__main__':
	main()

