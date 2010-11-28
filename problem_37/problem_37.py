#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("D:\\Projects\\Project Euler")

from common import prime_sieve

def isTruncatable (value, primeList):
	ret = True
	value = str(value)

	if (len(value) <= 1):
		ret = False
	else:
		for i in range(0, len(value)):
			if (int(value[i:]) not in primeList):
				ret = False
				break
			elif (int(value[:i+1]) not in primeList):
				ret = False
				break

	return ret

def main():

	count = 0
	primes = prime_sieve.prime_sieve(10**6)

	prime_set = set()
	for i in range(0, len(primes)):
		if (primes[i] == True):
			prime_set.add(i)

	for number in prime_set:
		if isTruncatable(number, prime_set):
			count += number

	print(count)

	return 0

if __name__ == '__main__':
	main()
