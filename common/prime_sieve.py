#!/usr/bin/env python
# -*- coding: utf-8 -*-

def prime_sieve(limit):
	primes = [True] * (limit+1)
	primes[0] = False
	primes[1] = False

	for i in range(2, int(limit**0.5)+1):
		if (primes[i]):
			for j in range(i*i, limit+1, i):
				primes[j] = False

		i += 1

	return primes


def isPrime(number):
	if (number < 2):
		ret = False
	else:
		ret = prime_sieve(number)[number]

	return ret

def primes(limit):
	sieve = prime_sieve(limit)
	primes = []
	for i in range(len(sieve)):
		if sieve[i] is True:
			primes.append(i)

	return primes


def main():


	print(isPrime(3797))

	return 0

if __name__ == '__main__':
	main()
