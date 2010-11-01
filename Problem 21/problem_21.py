#!/usr/bin/env python
# -*- coding: utf-8 -*-

def divsum(number):
	sum = 0
	for i in range(1,number):
		if ((number/i) % 1 == 0):
			sum += i
	
	return sum
	
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
			
	print(pairs)
	return 0
	
if __name__ == '__main__':

	main()

