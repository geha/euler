#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def isPrime(number):
	ret = True
	if (number == 2):
		ret = True

	elif (number == 1 or any (number % i == 0 for i in range(2, math.ceil(math.sqrt(number)) + 1))):
		ret = False

	return ret

def rotate (string):
	temp = string[0]
	string = string[1:]
	string += temp

	return string

def isCircular(number, primes):
	ret = True
	number = str(number)

	for i in range (0, len(number)):
		number = rotate(number)
		if (int(number) not in primes):
			ret = False

	return ret



def main():

	primes = set()

	for i in range (2, 10**6):
		if (isPrime(i)):
			primes.add(i)

		if (i % 100000 == 0):
			print(i)


	print ("Prime calculation finished")
	print()

	count = 0

	for i in primes:
		if (isCircular(i, primes)):
			count += 1

		if (i % 100 == 0):
			print (i)

	print(count)


	return 0

if __name__ == '__main__':
	main()

