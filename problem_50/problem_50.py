#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../")

from common.prime_sieve import *

limit = 10**6

primes = primes(limit)
primeset = set(primes)

max_count = 0
max_start = 0
max_sum = 0

for i in range(len(primes)):
	sum = primes[i]
	count = 1
	for j in range(i+1, len(primes)):
		sum += primes[j]
		if sum > limit:
			break
		count += 1
		if sum in primeset and count > max_count:
				max_count = count
				max_start = primes[i]
				max_sum = sum

print("longest sequence: ", max_count)
print("first prime: ", max_start)
print("sum of sequence: ", max_sum)

