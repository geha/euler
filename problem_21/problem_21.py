#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def divsum(number):
	sum = 1
	for i in range(2, math.floor(math.sqrt(number))):
		if ((number/i) % 1 == 0):
			sum += i + number/i
	
	return int(sum)
	
	
def amicable(a):
	b = divsum(a)
	if (a != b and divsum(b) == a):
		return True
	else:
		return False
	

def main():
	pairs = 0
	for i in range(1,10000):
		if (amicable(i)):
			print(i)
			pairs += i
	
	print()
	print(pairs)
	return 0
	
if __name__ == '__main__':

	main()

